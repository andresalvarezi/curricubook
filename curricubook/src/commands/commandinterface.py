from abc import ABC, abstractmethod

class Command(ABC):

    name = ""
    description = ""

    def __init__(self, settings):
        self.settings = settings
        
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def help(self):
        pass
