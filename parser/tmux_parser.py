from os.path import join
from os.path import basename
import re

from json_helper import keyboard_json
from json_helper import update_apps
from util import translate_key
from util import command_truncate

def parse_tmux(filename, verbose, directory_path):

    application = "tmux"
    file = open(filename, 'r')
    jsondata = keyboard_json("tmux", ["CONTROL", "ALT"], "Global", verbose)

    ver_regex = re.compile(r"\#\s*VERSION:(?P<version>[^\s]+)")
    os_regex = re.compile(r"\#\s*OS:(?P<os>[^\s]+)")
    tmux_regex = re.compile(r"^\s*bind-key(\s+-.)*(\s+(?P<context>copy-mode-vi|edit-mode-vi))?\s+(?P<mod>([^-]-)*)(?P<key>[^ ]+)\s+(?P<command>.+)")

    for line in file:

        match = os_regex.search(line)
        if match is not None:
            jsondata.json["os"] = match.group("os")

        match = ver_regex.search(line)
        if match is not None:
            jsondata.json["version"] = match.group("version")

        match = tmux_regex.search(line)
        if match is not None:

            key = match.group("key")
            command = command_truncate(match.group("command"))
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

            jsondata.insert_shortcut_key(context, key, mod, command)

    if verbose > 0:
        jsondata.print_json()

    export_filename = application+"_"+jsondata.json["version"]+"_"+\
                        jsondata.json["os"]+".json"

    jsondata.export_json(join(directory_path, export_filename))

    update_apps(join(directory_path, "apps.js"), application,
                jsondata.json["version"], jsondata.json["os"], export_filename)

if __name__ == "__main__":

    parse_tmux("../tests/tmux.conf", 0, "../content/generated")

