from tinydb import TinyDB, Query
from enum import Enum


class ErrorMessage(Enum):
    EXTENSION_ALREADY_EXISTS = 0
    NO_REDIRECT = 1
    MULTIPLE_REDIRECTS_ERROR = 2

#TODO remake the database less shit

class RedirectManager():
    def __init__(self):
        self.db = TinyDB("db.json")

    def add_redirect(self, target, extension):
        link = Query()
        results = self.db.search(link.extension == extension)
        if len(results) > 0:
            return ErrorMessage.EXTENSION_ALREADY_EXISTS

        self.db.insert({"extension": extension, "target": target})

        return 200

    def get_redirect(self, extension):
        link = Query()

        results = self.db.search(link.extension == extension)
        print(str(results))

        if len(results) == 0:
            return ErrorMessage.NO_REDIRECT

        if len(results) > 1:
            return ErrorMessage.MULTIPLE_REDIRECTS_ERROR

        return results[0]["target"]