import os
from pathlib import Path
import sys
import toml

from src.appcli import AppCLI
from src.utils import Utils

class GeneratorHTML:
    def __init__(self, cli, curricubook_settings):
        self.cli = cli
        self.curricubook_settings = curricubook_settings

    def generate(self):
        '''
        short_curricubook = self.initialize_short_curricubook()
        long_curricubook = self.initialize_curricubook()

        for element_type in [ "personal", "education", "work", "extra" ]:
            current_elements = Utils.load_elements(self.cli, self.cli.args.path, element_type)

            if len(current_elements) > 0:
                for elem in current_elements:
                    self.add_element_to_short_curricubook(short_curricubook, element_type, elem)
                    self.add_element_to_curricubook(long_curricubook, element_type, elem)

        self.finalize_short_curricubook(short_curricubook)
        self.finalize_curricubook(long_curricubook)
        '''
