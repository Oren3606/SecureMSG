"""

"""
import socket
from secrets import token_hex
from argparse import ArgumentParser


def encrypt():
    pass


def decrypt():
    pass


if __name__ == "__main__":
    tk = token_hex()[:32]

    parser = ArgumentParser(prog="Secure.MSG", usage="secmsg [start | connect HEX] [-name NAME]",
                            description="A console-based encrypted communication utility"
                            )

    parser.add_argument("action", help="what to do", type=str, nargs='?')
    parser.add_argument("target", help="connection target", type=str, nargs='?')
    parser.add_argument("-name", help="Name to use for session. Default: Anonymous", type=str, default="Anonymous")

    args = parser.parse_args()

    # If an action was not given
    if not args.action:
        parser.print_help()

    # If start option was given with a target
    if args.action == 'start' and args.target:
        print('"start" action cannot be used with "target" option')

    # If connect action was given with no target
    if args.action == 'connect' and not args.target:
        print('"connect" action requires usage of "target" option')

    print("\n[DEBUG]: args -", args)

'''
examples for reference for self- 

secmsg connect hex

secmsg start

notes for self on usage examples-
"" - given command
>> - console output

"secmsg connect 6682b11e079fc91f -name tom"
>> now connecting...

"secmsg listen name tom"
>> hash generated:
>> h458e9ff
>> now listening for connections...
>> new connection: tom
'''
