from src.appcli import AppCLI

class Utils():

    @staticmethod
    def print_if_verbose(cli, message):
        if cli.args.verbose:
            print(message)
