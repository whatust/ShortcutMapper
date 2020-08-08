//#include"Planner.h"
#include"Parser.h"

int main(int argc, char* argv[]) {

    Parser parser;

    //parser.parse("../test/init.vim", "nvim");
    //parser.parse("../test/tmux.conf", "tmux");
    parser.parse("../test/config.h", "dwm");

    return 0;
}
