import argparse
import logging

from libs.grabber import Grabber
from libs.helper import CatchBaseException


class TextFormat:
    pass


class Settings:
    pass


def create_parser():
    parser = argparse.ArgumentParser(description='Text parser from web-page')
    parser.add_argument('--url', type=str, help='url of web-page')
    return parser


@CatchBaseException
def main(args):
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] %(levelname).1s %(message)s',
                        datefmt='%Y.%m.%d %H:%M:%S')
    logging.info("Program started")
    gb = Grabber()
    gb.handle()


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    main(args)
