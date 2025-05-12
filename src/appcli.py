import argparse
import sys

class CustomArgParser(argparse.ArgumentParser):
    def error(self, message):
        AppCLI.print_initial_banner()

        print(message)
        print()

        self.print_help()
        print()
        
        sys.exit(2)

class AppCLI:
    version = "0.1.0"

    def __init__(self):
        self.parser = CustomArgParser(description="Tool to generate fancy work and education documents in several formats, lengths and styles")

        self.parser.add_argument(
            "-v", "--verbose",
            help="Print verbose output",
            action="store_true"
        )

        self.parser.add_argument(
            "-p", "--path",
            help="Project files path",
            default="demo",
            type=str
        )
        
        self.parser.add_argument(
            "command",
            help="The command to execute: init, add <element>, display, generate"
        )

        self.args, self.command_args = self.parser.parse_known_args()

    @staticmethod
    def print_initial_banner():
        print()
        print(f"Curricubook {AppCLI.version}")
        print("Tool to generate fancy work and education documents in several formats, lengths and styles")
        print("Andrés Álvarez Iglesias (andres@alvarezperello.com)")
        print()

    def print_help(self):
        self.parser.print_help()
        print()

        print("Write \"command help\" to get a detailed help of each command")
        print()