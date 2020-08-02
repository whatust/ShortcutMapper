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

def command_truncate(command):

    if(len(command) > 15):
        command = command[:12] + "..."

    return command

def translate_key(key):

    if key.lower() in key_translation:
        return key_translation[key.lower()]

    eprint("Unsupported key:{}".format(key), "warning")

    return ""

key_translation = {
        "bs":"BACKSPACE",
        "tab":"TAB",
        "return":"RETURN",
        "space":"SPACE",
        "bslash":"BACKSLASH",
        "del":"DELETE",
        "up":"UP_ARROW",
        "down":"DOWN_ARROW",
        "left":"LEFT_ARROW",
        "right":"RIGHT_ARROW",
        "f1":"F1",
        "f2":"F2",
        "f3":"F3",
        "f4":"F4",
        "f5":"F5",
        "f6":"F6",
        "f7":"F7",
        "f8":"F8",
        "f9":"F9",
        "f10":"F10",
        "f11":"F11",
        "f12":"F12",
        "insert":"INSERT",
        "home":"HOME",
        "pageup":"PAGE_UP",
        "pagedown":"PAGE_DOWN",
        "comma":"COMMA",
        "period":"PERIOD",
        "semicolon":"SEMICOLON",
        "bracketleft":"LEFT_BRACKET",
        "bracketright":"RIGHT_BRACKET",
        "backslash":"BACKSLASH",
        "equal":"EQUAL",
        "minus":"MINUS",
        "backspace":"BACKSPACE",
        "grave":"ACCENT_GRAVE",
        "page_up":"PAGE_UP",
        "page_down":"PAGE_DOWN",
        "print":"PRINT_SCREEN",
        ",":"COMMA",
        "num_lock":"NUMLOCK"
        }

