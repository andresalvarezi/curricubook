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
        
        self.curricubook_settings = Utils.load_curricubook_settings(self.cli, Path(self.cli.args.path) / "curricubook.toml")

        if self.curricubook_settings is None:
            print("...curricubook.toml not found!")
            print()
            sys.exit()

        print(f"Displaying current elements...")
        self.display_elements()
        print()

    def display_elements(self):
        path = Path(self.cli.args.path)
        if not path.is_dir():
            print("...target folder not found!")
            print()
            sys.exit()

        for element_type in [ "education", "work", "personal", "extra" ]:
            current_elements = Utils.load_elements(self.cli, self.cli.args.path, element_type)

            if len(current_elements) > 0:
                print()
                print(f"{element_type.upper()} ({len(current_elements)} elements):")
                print()
                
                for elem in current_elements:
                    print(f"  {elem['title']} ({elem['date']})")
                    print(f"   - Metadata file: {str(elem['metadata'])}")
                    print(f"   - Content file: {str(elem['content'])}")

    def help(self):
        print("The DISPLAY command all elements on the current Curricubook")
        print()
