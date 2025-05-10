from src.appcli import AppCLI
from src.commandfactory import CommandFactory

def main():
    cli = AppCLI()
    AppCLI.print_initial_banner()

    command = CommandFactory.generateCommand(cli)
    if command != None:
        command.execute()
    else:
        cli.print_help()
        
if __name__ == "__main__":
    main()
