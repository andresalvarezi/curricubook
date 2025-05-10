import argparse

class Settings:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Tool to generate fancy work and education documents in several formats, lengths and styles")

        self.parser.add_argument(
            "-v", "--verbose",
            help="Print verbose output",
            action="store_true"
        )

        self.parser.add_argument(
            "-p", "--path",
            help="Project files path",
            default="files",
            type=str
        )
        
        parser.add_argument(
            "command",
            help="The command to execute: init, add <element>, display, generate"
        )


        self.cli_args = parser.parse_args()
