import os
from pathlib import Path
import sys

from src.commands.commandinterface import Command
from src.appcli import AppCLI
from src.utils import Utils

class DisplayCommand(Command):

    name = "display"
    description = "Display all resources on this Curricubook"
    
    def execute(self, cli):
        self.cli = cli

        if "help" in cli.args.command_args:
            self.help()
            return
        
        print(f"Displaying current elements...")
        selft.display_elemenst()
        print()

    def display_elements(self):
        Utils.print_if_verbose(self.cli, "...checking target folder...")

        path = Path(self.cli.args.path)
        if not path.is_dir():
            print("...target folder not found!")
            print()
            sys.exit()

        # ...

        print("...done!")

    def help(self):
        print("The DISPLAY command all elements on the current Curricubook")
        print()

