from flask import Flask, send_from_directory, request, redirect
from flask.templating import render_template
import redirects

app = Flask(__name__)

redirector = redirects.RedirectManager()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/assets/<path:path>")
def send_assets(path):
    return send_from_directory("assets/", path)


@app.route("/r/<extension>")
def redirect(extension):
    result = redirector.get_redirect(extension)

    if result == redirects.ErrorMessage.NO_REDIRECT:
        return "No redirect", 400

    if result == redirects.ErrorMessage.MULTIPLE_REDIRECTS_ERROR:
        return "Unexpected error"

    return redirect(result)

@app.route("/add_redirect", methods=["POST"])
def add_redirect():
    target = request.headers.get("target")

    extension = request.headers.get("extension")

    result = redirector.add_redirect(target, extension)

    if result == redirects.ErrorMessage.EXTENSION_ALREADY_EXISTS:
        return "Extension already exists", 409

    return "Done", 200

app.run(host="0.0.0.0", port=7040)
