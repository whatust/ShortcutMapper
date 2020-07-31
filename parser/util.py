import sys

def eprint(message, message_type):
    if message_type == "warning":
        print(_color.WARNING + "[WARNING]" + _color.END + message, file=sys.stderr)
    if message_type == "error":
        print(_color.ERROR + "[ERROR]" + _color.END + message, file=sys.stderr)
    if message_type == "log":
        print(_color.LOG + "[LOG]" + _color.END + message, file=sys.stderr)
    if message_type == "success":
        print(_color.SUCCESS + "[SUCCESS]" + _color.END + message, file=sys.stderr)

class _color:

    WARNING = "\033[93m"
    ERROR = "\033[91m"
    LOG = "\033[34m"
    SUCCESS = "\033[92m"
    END = "\033[0m"
