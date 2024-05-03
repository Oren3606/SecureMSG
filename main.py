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
    print(token_hex()[:32])
    parser = ArgumentParser(prog="Secure.MSG", usage="secmsg MODE [OPTIONS] NAME",
                            description="An encrypted console-based communication utility",
                            argument_default='--help'
                            )

    parser.add_argument("mode", help="Mode of operation", type=str, choices=['connect', 'start'])
    parser.add_argument("-name", help="Name to use for session", type=str, default="Anonymous", nargs=1)
    parser.add_argument("-hash", help="Peer hash to connect to", type=str)

    print(parser.parse_args())

'''

secmsg connect fehgerwg


notes for self on usage examples-
"" - given command
>> - console output
 
--------------------------------

"secmsg connect h458e9ff name tom"
>> now connecting...

"secmsg listen name tom"
>> hash generated:
>> h458e9ff
>> now listening for connections...
>> new connection: tom

"secmsg listen name tom hash=h458e9ff" 
>> trying to use hash...
>> success:
>> h458e9ff
>> now listening for connections...
>> new connection: tom
'''
