import os
from pathlib import Path
import sys
import toml

from src.commands.commandinterface import Command
from src.appcli import AppCLI
import datetime
from src.utils import Utils

class AddCommand(Command):

    name = "add"
    description = "Add a new resource to this Curricubook"
    
    def execute(self, cli):
        self.cli = cli

        element_type = None
        if len(cli.args.command_args) > 0:
            element_type = (cli.args.command_args[0] if cli.args.command_args[0] in [ "personal", "education", "work", "extra" ] else None)

        if not element_type or "help" in cli.args.command_args:
            self.help()
            return
        
        self.curricubook_settings = Utils.load_curricubook_settings(self.cli, Path(self.cli.args.path) / "curricubook.toml")

        if self.curricubook_settings is None:
            print("...curricubook.toml not found!")
            print()
            sys.exit()

        print(f"Adding a new {element_type} element...")
        self.add_element(element_type)
        print()

    def add_element(self, element_type):
        path = Path(self.cli.args.path)
        if not path.is_dir():
            print("...target folder not found!")
            print()
            sys.exit()

        filename_fragment = self.generate_name()

        with open(os.path.join(self.cli.args.path, element_type, f"{element_type}_{filename_fragment}.toml"), "w") as element_file:
            element_file.write(self.default_element_file_metadata_content(element_type))
        
        with open(os.path.join(self.cli.args.path, element_type, f"{element_type}_{filename_fragment}_brief.md"), "w") as element_file:
            element_file.write(self.default_element_file_content_brief(element_type))
        
        with open(os.path.join(self.cli.args.path, element_type, f"{element_type}_{filename_fragment}_long.md"), "w") as element_file:
            element_file.write(self.default_element_file_content_long(element_type))
        
        Utils.print_if_verbose(self.cli, "")
        print(f"...new element created!")
        print()

        target_dir = Path(self.cli.args.path) / element_type
        metadata_file = toml.load(Path(self.cli.args.path) / element_type / f"{element_type}_{filename_fragment}.toml")

        print(f"{metadata_file['metadata']['title']} ({metadata_file['metadata']['date']})")
        print(f" - Metadata file: {Path(self.cli.args.path)}/{element_type}/{element_type}_{filename_fragment}.toml")
        print(f" - Content file (brief): {Path(self.cli.args.path)}/{element_type}/{element_type}_{filename_fragment}_brief.toml")
        print(f" - Content file (long): {Path(self.cli.args.path)}/{element_type}/{element_type}_{filename_fragment}_long.toml")

    def generate_name(self):
        timestamp_numeric = datetime.datetime.now().timestamp()
        return str(timestamp_numeric).replace(".", "_")

    def generate_datebased_name(self):
        now = datetime.datetime.now()
        new_name = f"{now.year}{now.month:02d}{now.day:02d}_{now.hour:02d}{now.minute:02d}{now.second:02d}_{now.microsecond // 1000:03d}"
        return new_name

    def default_element_file_content_brief(self, element_type):
        now = datetime.datetime.now()

        content  = f"# New {element_type} (brief format)\n\n"
        content += Utils.generate_lorem_ipsum(1)

        return content

    def default_element_file_content_long(self, element_type):
        now = datetime.datetime.now()

        content  = f"# New {element_type} (long format)\n\n"
        content += Utils.generate_lorem_ipsum(5)

        return content

    def default_element_file_metadata_content(self, element_type):
        now = datetime.datetime.now()

        content  = f"[metadata]\n"
        content += f"title = \"New {element_type}\"\n"
        content += f"date = \"{now.year}-{now.month:02d}-{now.day:02d}, {now.hour:02d}:{now.minute:02d}:{now.second:02d}\"\n"

        return content

    def help(self):
        print("The ADD adds a new element to the current curricubook")
        print()
        print("options:")
        print("  type: the type of element to be added: personal, education, work or extra")
        print()
