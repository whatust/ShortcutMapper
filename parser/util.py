import sys

def eprint(message, message_type):
    if message_type == "warning":
        print(_color.WARNING + "[WARNING]" + _color.END + message, file=sys.stderr)

class _color:

    WARNING = "\033[93m"
    END = "\033[0m"
