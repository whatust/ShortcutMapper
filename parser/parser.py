import argparse
import sys

from vim_parser import parse_vim
from dwm_parser import parse_dwm

def controler(args):

    #config_type = config_identify(args.file);
    config_type = "dwm"

    if config_type == "vim":
        parse_vim(args.file, args.verbose)

    if config_type == "dwm":
        parse_dwm(args.file, args.verbose)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Extract shortkey - command pairs from configuration files");

    parser.add_argument("--file", type=str, required=True, help="Path to the configuration file")
    parser.add_argument("--verbose", type=int, default=0, help="Verbose level")

    args = parser.parse_args()

    controler(args)

