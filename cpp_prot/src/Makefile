CXX=g++

LD=$(CXX)
AR=ar

DEBUG=-ggdb
CXXFLAGS=-O3 -Wall $(DEBUG) -std=c++17
LDFLAGS=-O3 $(DEBUG) -L.

LIBSOURCES=Aplication.cpp Parser.cpp Types.cpp Planner.cpp Util.cpp

LIBOBJS=$(LIBSOURCES:%.cpp=%.o)

MAINS=$(wildcard main*.cpp)
TARGETS=$(MAINS:%.cpp=%)

.PHONY: all clean

.SUFFIXES: .cpp .o

all: $(TARGETS)

.deps: *.cpp *.h
	$(CXX) $(CXXFLAGS) -MM *.cpp > .deps

$(TARGETS): %: %.o libmal.a
	$(LD) $^ -o $@ $(LDFLAGS)

libmal.a: $(LIBOBJS)
	$(AR) rcs $@ $^

.cpp.o:
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf *.o $(TARGETS) libmal.a .deps

-include .deps
