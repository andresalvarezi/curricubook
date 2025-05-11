from src.appcli import AppCLI
from src.commandfactory import CommandFactory

def main():
    cli = AppCLI()
    AppCLI.print_initial_banner()

    command = CommandFactory.generateCommand(cli.args.command)
    if command != None:
        command.execute(cli)
    else:
        cli.print_help()
        
if __name__ == "__main__":
    main()
