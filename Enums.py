from enum import Enum


class App(Enum):
    Web = 1
    Mobile = 2


class Browser(Enum):
    Chrome = 1
    Firefox = 2
    Safari = 3


class OS(Enum):
    NA = 0
    Android = 1
    IOS = 2
    Windows = 3
    Linux = 4


class ElementIDType(Enum):
    XPATH = 1
    ID = 2
    Text = 3
    ClassName = 4
    Name = 5
