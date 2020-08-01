import re

from json_helper import keyboard_json
from util import translate_key

def parse_tmux(filename, verbose, export_filename):

    file = open(filename, 'r')
    jsondata = keyboard_json("tmux", "1.0", "linux", ["CONTROL", "ALT"], "Global", verbose)

    tmux_regex = re.compile(r"^\s*bind-key(\s+-.)*(\s+(?P<context>copy-mode-vi|edit-mode-vi))?\s+(?P<mod>([^-]-)*)(?P<key>[^ ]+)\s+(?P<command>.+)")

    for line in file:

        match = tmux_regex.search(line)

        if match is not None:

            key = match.group("key")
            command = match.group("command")
            context = match.group("context")
            mod = match.group("mod")

            if context is None:
                context = "Global"
            else:
                if context == "copy-mode-vi":
                    context = "Copy"
                elif context == "edit-mode-vi":
                    context = "Edit"

            if mod is None:
                mod = []
            else:
                _mod = []

                if "C" in mod:
                    _mod.append("CONTROL")
                if "M" in mod:
                    _mod.append("ALT")

                mod = _mod

            if(len(key) == 1):
                key = key.upper()
            else:
                key = translate_key(key)
                if key == "":
                    continue

            if verbose > 1:
                print(context + " " + str(mod) + " " + key + " " + command)

            #jsondata.insert_shortcut_key(context, key, mod, command)

    #if verbose > 0:
        #jsondata.print_json()

    jsondata.export_json(export_filename)

if __name__ == "__main__":

    parse_tmux("../tests/tmux.conf", 2, "../content/generated/tmux_1.0_linux.json")

