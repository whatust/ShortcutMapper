import argparse
import sys

from vim_parser import parse_vim
from dwm_parser import parse_dwm
from tmux_parser import parse_tmux

def controler(filename, config_type,  verbose):

    directory_path = "../content/generated"

    if config_type == "vim":
        parse_vim(args.file, args.verbose, directory_path)

    if config_type == "dwm":
        parse_dwm(args.file, args.verbose, directory_path)

    if config_type == "tmux":
        parse_tmux(args.file, args.verbose, directory_path)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Extract shortkey - command pairs from configuration files");

    parser.add_argument("--file", type=str, required=True, help="Path to the configuration file")
    parser.add_argument("--verbose", type=int, default=0, help="Verbose level")

    args = parser.parse_args()

    #config_type = config_identify(args.file);

    controler(args.file, "vim", args.verbose)
    #controler(args.file, "dwm", args.verbose)
    #controler(args.file, "tmux", args.verbose)

