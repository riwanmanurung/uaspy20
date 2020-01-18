from view.view_book import *
from view.input_book import *
from core.baseapp import BaseApp
from core.search_helper import SearchHelper

class MainApp(BaseApp):
    def __init__(self):
        self.books = []

    def list_book(self):
        ViewBook.list()

    def add_book(self):
        InputBook.input()


if __name__ == "__main__":
    app = MainApp()
    app.run()

