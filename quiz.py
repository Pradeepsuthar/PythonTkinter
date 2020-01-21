from tkinter import *
import json

import features

class MainApp():
    FILE_NAME = "database.json"

    def __init__(self):
        features.HomeApp()

    def database(self):
        fr = open(MainApp.FILE_NAME)
        data = json.load(fr)
        fr.close()

MainApp()


