from abc import ABC, abstractmethod

class Command(ABC):

    name = ""
    description = ""

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def help(self):
        pass
