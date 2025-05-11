from src.commands.initcommand import InitCommand
from src.commands.displaycommand import DisplayCommand
from src.commands.addcommand import AddCommand
from src.commands.generatecommand import GenerateCommand

class CommandFactory:

    @staticmethod
    def generateCommand(command):
        if command == "init":
            return InitCommand()
        elif command == "display":
            return DisplayCommand()
        elif command == "add":
            return AddCommand()
        elif command == "generate":
            return GenerateCommand()
        return None
