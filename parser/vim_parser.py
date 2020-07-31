import json
import re

def parse_vim(filename, verbose):

    file = open(filename, 'r')

    vim_regex = re.compile(r"^\s*(?P<context>[nvi])*(nore)?map\s+((<silent>)?\s*(<expr>)?\s*<(?P<mod>[CAS]-[CAS]|[CAS])?-?(?P<key>[^\s-]*))>\s+(?P<command>.*)")

    for line in file:

        match = vim_regex.search(line)

        if match is not None:
            context = match.group("context")
            key = match.group("key")
            command = match.group("command")
            mod = match.group("mod")

            if context is None:
                context = "None"

            if mod is None:
                mod = "None"

            if verbose > 0:
                print(context + " " + mod + " " + key + " " + command)

