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
    checkoutParser.add_argument("name", nargs="?", help="Branch name or commit ID")
    checkoutParser.add_argument("-b", dest="new_branch", help="Create and switch to a new branch")

    branchParser = subparser.add_parser("branch")
    branchParser.add_argument("bname", nargs="?", help="Name of the new branch.")

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
            if args.new_branch:
                checkout.checkout("-b", args.new_branch)
            elif args.name:
                checkout.checkout(args.name)
            else:
                print("Usage: mygit checkout [-b <branch>] <commit|branch>")
        
        case "log":
            log.log()

        case "branch":
            if args.bname:
                branch.branch(bname=args.bname)
            else:
                branch.branch()