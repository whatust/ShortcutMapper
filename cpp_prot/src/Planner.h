#ifndef _PLANNER_H_
#define _PLANNER_H_

#include<string>
#include<vector>

#include"Aplication.h"

class Planner {
    private:
        std::string keyboard_layout;
        std::vector<Aplication> configs;
    public:
        Planner(std::string _layout) : keyboard_layout(_layout) {};
};

#endif // _PLANNER_H_

