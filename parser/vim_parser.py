from os.path import basename
from os.path import join
import re

from json_helper import keyboard_json
from json_helper import update_apps
from util import translate_key
from util import command_truncate

def parse_vim(filename, verbose, directory_path):

    application = "vim"
    file = open(filename, 'r')
    jsondata = keyboard_json(application, ["CONTROL", "SHIFT", "ALT"], "Global", verbose)

    ver_regex = re.compile(r"^\"VERSION:(?P<version>[^\s]+)")
    os_regex = re.compile(r"^\"OS:(?P<os>[^\s]+)")
    leader_regex = re.compile(r"^let\s+mapleader\s+=\s+\"(?P<leader>.)\"")

    vim_regex = re.compile(r"^\s*(?P<context>[nvi])?(nore)?map\s+(?P<leader><Leader>)?(<silent>)?\s*(<expr>)?\s*<?(?P<mod>[CAS]-[CAS]|[CAS])?-?(?P<key>[^\s>-]*)>?\s+(?P<command>.*)")

    _context = {'g':"Global", 'v':"Verbose", 'n':"Normal", 'i':"Insert"}

    for line in file:

        match = os_regex.search(line)
        if match is not None:
            jsondata.json["os"] = match.group("os")

        match = ver_regex.search(line)
        if match is not None:
            jsondata.json["version"] = match.group("version")

        match = leader_regex.search(line)
        if match is not None:
            leader = match.group("leader")
            leader = translate_key(leader)
            jsondata.json["mods_used"].append(leader)

        match = vim_regex.search(line)
        if match is not None:
            key = match.group("key")
            mod = match.group("mod")

            if match.group("leader"):
                mod = "L"

            context = match.group("context")
            command = command_truncate(match.group("command"))

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
                if "L" in mod:
                    _mod.append(leader)

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

    parse_vim("../tests/init.vim", 0, "../content/generated")

