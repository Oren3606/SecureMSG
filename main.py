"""

"""
import socket
from secrets import token_hex
from argparse import ArgumentParser
import initiator

# todo use cryptography lib?


def encrypt():
    pass


def decrypt():
    pass


if __name__ == "__main__":
    parser = ArgumentParser(prog="Secure.MSG",
                            usage="secmsg [--target <HEX>] [--name <USERNAME>]",
                            description="A console-based encrypted communication utility.",
                            )

    parser.add_argument("-t", "--target", help="Connection target hex. Multiple may be provided",
                        type=str, action='append'
                        )
    parser.add_argument("-n", "--name", help="Name to use for session. Defaults to Anonymous <num>",
                        type=str, default="Anonymous"
                        )

    args = parser.parse_args()

    # Target not provided
    if not args.target:
        print("\n[DEBUG]: listen mode")
        ...
    # Target provided
    else:
        for target in args.target:
            print("\n[DEBUG]: connect mode, connecting to ", target)
            ...

    print("[DEBUG]: args -", args)
