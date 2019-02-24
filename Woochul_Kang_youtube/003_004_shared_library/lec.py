# ======================================================================
# https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_11:51:03.png

# ======================================================================
There are some points 
which you should be careful when you create shared library files
unlike when you create archiev files (static library files)

# ======================================================================
1. Functions in shared library files should be "reentrant"

"Reentrant" means 
that you shouldn't use "global variables" in shared library files

Imagine 2 executables can point to one shared library file at the same time,
and if shared library file has global variable x, 
global variable x can be changed by exe1,
then exe2 reference different unexpectedly changed global variable x

# https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_11:55:34.png

# ======================================================================
2. Codes in shared library files should be "position-independent".

When shared library file is loaded onto memory,
you can't predict the address of the memory place 
where shared library file is loaded.

So, you shouldn't write any codes 
in executable files, object fiels, shared library files, etc,
with supposing a specific address 
where shared library files are loaded onto the memory.

You shouldn't suppose you can jump or call 
to the fixed address when writing codes.

You shouldn't suppose you can access data 
at the fixed locations when writing codes.

# ======================================================================
Shared library naming rule

# 1.0: version infomation
libmyfuncs.so.1.0: actual shared library file which you create

libmyfuncs.so: when you compile, 
you use this name which doesn't have version information
But this is not an actual file 
but it's symbolic link to the actual shared library file like libmyfuncs.so.1.0


You can make libmyfuncs.so.1 file symbolic-link to actual shared library file 
which you want to use like libmyfuncs.so.1.0, libmyfuncs.so.1.1, libmyfuncs.so.1.2, etc
And this file libmyfuncs.so.1 is used by the executable file at runtime

# ======================================================================
How to create shared library files

1. Create object files 
with using -fPIC (position-independent code) option of GCC
gcc -fPIC -c func1.c
gcc -fPIC -c func2.c

2. Create shared library file by gathering object files
For this step, you can use gcc and ld

# -shared: you're going to create shared library file 
# (default so omitable, but recommended to use this for explicit expression)
# -Wl, <options>: <options> are passed to the ld
# compile and asembly steps are performed in GCC
# Linking is performed by Linker (ld)
# -soname=libmyfuncs.so.1: specify the name of representitive so file (shared library file)
# *.o: you will include all object files 
# which are located in the current directory into so file
# -o libmyfuncs.so.1.0: specify the name of actual shared library file 
# which you're going to create
# -lc: link libc
gcc -fPIC -shared -Wl, -soname=libmyfuncs.so.1 *.o -o libmyfuncs.so.1.0 -lc

ld -shared -soname=libmyfuncs.so.1 *.o -o libmyfuncs.so.1.0 -lc

# ======================================================================
After you create shared library file like libmyfuncs.so.1.0,
you need to perform symbolic link

# libmyfuncs.so.1.0: actual shared library file
# libmyfuncs.so: representitive name of libmyfuncs shared library file
# which is used when you link files at compile time in gcc
ln -s libmyfuncs.so.1.0 libmyfuncs.so

# libmyfuncs.so.1: is used at runtime when dynamic linking is performed
ln -s libmyfuncs.so.1.0 libmyfuncs.so.1


# ======================================================================
To link an application (foo) with shared library file

# When you want to use shared library libmyfuncs on foo.c file
# you need to add path (-L/mypath/lib) 
# which contains shared library file libmyfuncs
gcc -o foo foo.c -L/mypath/lib -lmyfuncs

# ======================================================================
Command-line options

-L: is used to tell the linker the places 
where the linker should search to find your libxxx.so file

-l: is used to tell the linker 
about which shared object files to be linked with first

- Wl: is used to tell gcc/g++ compilers 
to pass specified options onto the linker

# ======================================================================
How to find shared library files at runtime
How to link shared library files to executable and other files at runtime

Excutable files have pointers
at runtime, library files 
which are pointed by pointers are linked with executable files

But you can't search all directories to find specific shared library files.
So, system library paths (like /lib, /usr/lib, etc) 
which you should search to find shared library files are written 
in /etc/ld.so.conf

# ======================================================================
You also can have your own custom libraries than system library

Paths for your own custom libraries should be written 
in LD_LIBRARY_PATH environment variable
like export LD_LIBRARY_PATH=$HOME/foo/lib

Then, Linux loader which executes programs searches all libraries 
which are located in the written paths at runtime
