import os
from pathlib import Path
import sys
import shutil

from src.commands.commandinterface import Command
from src.appcli import AppCLI
from src.utils import Utils

class InitCommand(Command):

    name = "init"
    description = "Initializes a new Curricubook"
    
    def execute(self, cli):
        self.cli = cli

        if "help" in cli.args.command_args:
            self.help()
            return
        
        print(f"Initializing new project in: {self.cli.args.path}")
        self.initialize_project()
        print()

    def help(self):
        print("The INIT command initializes a new curricubook in the folder choosen with the --path argument")
        print()
        print("options:")
        print("  --force: overwrite the given path if not empty")
        print()

    def initialize_project(self):
        path = Path(self.cli.args.path)
        if path.is_dir():
            if any(path.iterdir()):
                if "--force" in self.cli.args.command_args:
                    print("...target folder found, removing current contents...")
                    shutil.rmtree(self.cli.args.path)

                else:
                    print("...target folder found, but is not empty! Use --force to remove the current contents")
                    print("...done!")
                    print()
                    sys.exit()

            else:
                Utils.print_if_verbose(self.cli, "...empty target folder found!")

        else:
            Utils.print_if_verbose(self.cli, "...target folder not found!")
    
        Utils.print_if_verbose(self.cli, "...initializing project files...")
        path.mkdir(parents=True, exist_ok=True)

        Path(os.path.join(self.cli.args.path, "personal")).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(self.cli.args.path, "education")).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(self.cli.args.path, "work")).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(self.cli.args.path, "extra")).mkdir(parents=True, exist_ok=True)
             
        with open(os.path.join(self.cli.args.path, "curricubook.toml"), "w") as project_file:
            project_file.write(self.default_project_file_content())
        
        Utils.print_if_verbose(self.cli, "")
        print("New Curricubook initialized!")

    def default_project_file_content(self):
        content = "[curricubook]\n"
        content += "name = \"My Curricubook\"\n"
        content += "author_name = \"Your name\"\n"
        content += "author_email = \"your@email.com\"\n"
        content += "\n"

        content += "[generation]\n"
        content += "template = \"Default\"\n"
        content += "generate_pdf = true\n"
        content += "generate_html = true\n"
        content += "\n"

        return content