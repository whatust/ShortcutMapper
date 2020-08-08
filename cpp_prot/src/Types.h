#ifndef TYPES_H_
#define TYPES_H_

#include<iostream>
#include<fstream>
#include<string>

enum _modkey { NONE=0, CTRL = 1, SHIFT = 2, ALT = 4, SUPER = 8, LEADER = 16};
enum _vimmodes { NORMAL = 0, INSERT = 1, VISUAL = 2, REPLAE = 3, ALL = 4 };

class Modkey {
    public:
        int code;

        Modkey() : code(0) {};
        Modkey& operator+=(const enum _modkey& mk);
        Modkey& operator=(const enum _modkey& mk);
        friend std::ostream& operator<<(std::ostream& os, const Modkey& mk);
};

class VimMode {
    private:
        int mode;
    public:
        VimMode() : mode(0) {};
        VimMode& operator=(const enum _vimmodes& vm);
        friend std::ostream& operator<<(std::ostream& os, const VimMode& mk);
};

class Shortcut {
    public:
        std::string key;
        std::string command;
        Shortcut(std::string _key, std::string _cmd);
};

#endif //TYPES_H_
