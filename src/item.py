from random import random
from enum import Enum

class Item:
    def __init__(self, name = "Item", value = 0, x = -1, y = -1):
        self.name = name
        self.value = value
