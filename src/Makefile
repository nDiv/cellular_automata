# define the C compiler to use
CC = g++

# define any compile-time flags
CFLAGS = -Wall -g -std=c++0x -I.

# define target folder
#BINDIR = -I../bin

# define any directories containing header files other than /usr/include
#
INCLUDES = -I../include

# define the CPP source files
SRCS = test.cpp automata.cpp 

# define the C object files 
#
# This uses Suffix Replacement within a macro:
#   $(name:string1=string2)
#         For each word in 'name' replace 'string1' with 'string2'
# Below we are replacing the suffix .c of all words in the macro SRCS
# with the .o suffix
#
OBJS = $(SRCS:.c=.o)

# define the executable file 
MAIN = test

.PHONY: depend clean

all: $(MAIN)
	@echo  "Successfully compiled!"

$(MAIN): $(OBJS) 
	$(CC) $(CFLAGS) $(INCLUDES) -o $(MAIN) $(OBJS)

# this is a suffix replacement rule for building .o's from .c's
# it uses automatic variables $<: the name of the prerequisite of
# the rule(a .c file) and $@: the name of the target of the rule (a .o file) 
# (see the gnu make manual section about automatic variables)
.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	$(RM) *.o *~ $(MAIN)

depend: $(SRCS)	
	makedepend $(INCLUDES) $^

# DO NOT DELETE THIS LINE -- make depend needs it
