A library is a "file" which contains compiled code from various "object files"

# ======================================================================
For example, suppose "pthread" library

"pthread" library is "file" or "multiple files" 
which are composed of files and functions related to threading

# ======================================================================
Library can be categorized into 2 types
- Shared library (or dynamic library)
- Static library (or archive file)

# ======================================================================
Static library: links files at compile time

# https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_11:36:11.png

Linker links all files (current project object files, external libraries, .o files, etc)

All files are contained into single excutable file

# ======================================================================
How to create and use an archiev file (or static library)

You use "ar" command for this

- Compile C source files
gcc -c func1.c
gcc -c func2.c

to create func1.o and func2.o files

- Create single archiev file from multiple object files
# r: put func1.o and func2.o files into libfuncs.a static library file
# v: verbose
ar rv libfuncs.a func1.o func2.o

Now, libfuncs.a static library file contains func1.o and func2.o

- When you want to use functions 
which are defined in func1.o and func2.o on myapp.c file in static library way
you can use following command
# -L.: search library in current directory at compile time
# -lfuncs: link libfuncs.a static library file with object file
# -o myapp: specify executable file name
gcc myapp.c -L. -lfuncs -o myapp

# ======================================================================
You can use nm 
to see whether a static library file really contains 
functions and symbols and defined variables
which you had created 

# libfuncs.a: files like library, executable, object file
# print all symbols (function name, variable name) in that file
nm -s libfuncs.a
