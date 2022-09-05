import argparse
from os import chdir, path
import sys

from net.server_protocol import run_server
from chat_client import run_client


def main(args: argparse.Namespace):
    host = args.host if args.host else "127.0.0.1"
    port = args.port if args.port else 5001
    test = args.test

    if args.server:
        print("starting server:")
        run_server(host, port)
        return
    run_client(host=host, port=port, test=test)


if __name__ == "__main__":
    chdir(path.dirname(path.abspath(__file__)))

    # set up command line arguments
    # python main.py -s to start server
    # python main.py -t to start client in testing mode

    parser = argparse.ArgumentParser()
    parser.add_argument("--server", "-s", default=False, action="store_true")
    parser.add_argument("--test", "-t", default=True,
                        action="store_true", help="Start chat client in testing mode")
    parser.add_argument("--host", type=str,
                        help="Specify host name for client/server")
    parser.add_argument("--port", "-p", type=int,
                        help="Specify port for client/server")
    arguments = parser.parse_args(sys.argv[1:])
    main(args=arguments)
