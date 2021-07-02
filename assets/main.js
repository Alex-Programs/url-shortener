function createLink() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4  && this.status == 200) {
            alert("Done-ish-maybe?")
        }
    }

    xhttp.open("POST", "/add_redirect")
    xhttp.setRequestHeader("target", document.getElementById("targetInput").value)
    xhttp.setRequestHeader("extension", document.getElementById("extensionInput").value)
    xhttp.send()
}