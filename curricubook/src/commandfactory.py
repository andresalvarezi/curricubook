from src.commands.initcommand import InitCommand
from src.commands.displaycommand import DisplayCommand
from src.commands.addcommand import AddCommand
from src.commands.generatecommand import GenerateCommand

class CommandFactory:

    @staticmethod
    def generateCommand(cli):
        if cli.args.command == "init":
            return InitCommand(cli)
        elif cli.args.command == "display":
            return DisplayCommand(cli)
        elif cli.args.command == "add":
            return AddCommand(cli)
        elif cli.args.command == "generate":
            return GenerateCommand(cli)
        return None
