import argparse
from src import init, add, commit, log, checkout, branch, status


def main():

    # main parser
    parser = argparse.ArgumentParser(prog="mygit")

    # subparser for individual commands
    subparser = parser.add_subparsers(dest="command")

    for cmd in ["init", "status", "log"]:
        subparser.add_parser(cmd)

    # subparser for add command
    addParser = subparser.add_parser("add")
    addParser.add_argument("fileName")

    # subparser for commit command
    commitParser = subparser.add_parser("commit")
    commitParser.add_argument("-m", "--message", required=True)

    # subparser for checkout command
    checkoutParser = subparser.add_parser("checkout")
    checkoutParser.add_argument("commitID")
    # checkoutParser.add_argument("-b", action="store_true", help="Create a new branch")


    # parse the arguments
    args = parser.parse_args()

    # execute the commands
    match args.command:

        case "init":
            init.init()

        case "add":
            add.add(args.fileName)

        case "commit":
            commit.commit(args.message)

        case "status":
            status.status()

        case "checkout":
            # print(f"Switching to existing branch: {args.commitID}")
            checkout.checkout(args.commitID)
        
        case "log":
            log.log()