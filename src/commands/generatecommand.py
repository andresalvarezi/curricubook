import os
from pathlib import Path
import sys

from src.commands.commandinterface import Command
from src.appcli import AppCLI
from src.utils import Utils

class GenerateCommand(Command):

    name = "generate"
    description = "Generate the short and long version of this Curricubook"
    
    def execute(self, cli):
        self.cli = cli

        if "help" in cli.args.command_args:
            self.help()
            return
        
        print(f"Generating current Curricubook...")
        selft.generate()
        print()

    def generate(self):
        Utils.print_if_verbose(self.cli, "...checking target folder...")

        path = Path(self.cli.args.path)
        if not path.is_dir():
            print("...target folder not found!")
            print()
            sys.exit()

        # ...

        print("...done!")

    def help(self):
        print("The GENERATE command generates the current Curricubook")
        print()

