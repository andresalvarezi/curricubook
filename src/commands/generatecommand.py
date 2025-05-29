import os
from pathlib import Path
import sys
import toml

from src.commands.commandinterface import Command
from src.appcli import AppCLI
from src.utils import Utils
from src.generators.generatorpdf import GeneratorPDF
from src.generators.generatorhtml import GeneratorHTML

class GenerateCommand(Command):

    name = "generate"
    description = "Generate the short and long version of this Curricubook"
    
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

        self.generate()
        print()

    def generate(self):
        path = Path(self.cli.args.path)
        if not path.is_dir():
            print("...target folder not found!")
            print()
            sys.exit()

        if self.curricubook_settings['generation_pdf']:
            Utils.print_if_verbose(self.cli, "")
            print(f"Generating current Curricubook PDF document with template {self.curricubook_settings['generation_pdf']['template']}...")
            generator = GeneratorPDF(self.cli, self.curricubook_settings)
            generator.generate()

        if self.curricubook_settings['generation_html']:
            Utils.print_if_verbose(self.cli, "")
            print(f"Generating current Curricubook HTML document with template {self.curricubook_settings['generation_html']['template']}...")
            generator = GeneratorHTML(self.cli, self.curricubook_settings)
            generator.generate()

        Utils.print_if_verbose(self.cli, "")
        print("Curricubook generated!")

    def help(self):
        print("The GENERATE command generates the current Curricubook")
        print()

