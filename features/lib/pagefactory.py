import importlib
from features.lib.pages import *


def on(page_class):
    if (page_class in globals().keys()):
        page = globals()[page_class]()
    else:
        print("Page Object:" + page_class + " does not exist")
    return page

