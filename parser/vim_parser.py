import re

from json_helper import keyboard_json
from util import translate_key

def parse_vim(filename, verbose, export_filename):

    file = open(filename, 'r')
    jsondata = keyboard_json("vim", "1.0", "linux", ["CONTROL", "SHIFT"], "Global", verbose)

    vim_regex = re.compile(r"^\s*(?P<context>[nvi])?(nore)?map\s+(<silent>)?\s*(<expr>)?\s*<?(?P<mod>[CAS]-[CAS]|[CAS])?-?(?P<key>[^\s>-]*)>?\s+(?P<command>.*)")

    _context = {'g':"Global", 'v':"Verbose", 'n':"Normal", 'i':"Insert"}

    for line in file:

        match = vim_regex.search(line)

        if match is not None:
            context = match.group("context")
            key = match.group("key")
            command = match.group("command")
            mod = match.group("mod")

            if context is None:
                context = "g"
            context = _context[context]

            if mod is None:
                mod = []
            else:
                _mod = []

                if "C" in mod:
                    _mod.append("CONTROL")
                if "A" in mod:
                    _mod.append("ALT")
                if "S" in mod:
                    _mod.append("SHIFT")

                mod = _mod

            if(len(key) == 1):
                key = key.upper()
            else:
                key = translate_key(key)
                if key == "":
                    continue

            if verbose > 1:
                print(context + " " + str(mod) + " " + key + " " + command)

            jsondata.insert_shortcut_key(context, key, mod, command)

    if verbose > 0:
        jsondata.print_json()

    jsondata.export_json(export_filename)

if __name__ == "__main__":

    parse_vim("../tests/init.vim", 1, "../content/generated/vim_1.0_linux.json")

