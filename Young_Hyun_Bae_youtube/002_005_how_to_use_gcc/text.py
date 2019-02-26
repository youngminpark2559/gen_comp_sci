GCC stands for GNU C Compiler

======================================================================
GCC is an open source compiler which is create by GNU

Since GCC is created as the open source,
it suppiles most number of CPUs

======================================================================
Since GCC is separated into "driver program" and "compier core program" 
if you replace "compier core program" part,
GCC can compile C++, Java, Objective-C, Fortran, etc as well as C

======================================================================
GCC is composed of 
1. Preprocessor: cpp0 or cc1-E
2. Compiler: cc1 (you can replace this with other compilers)
3. Assembler: as
4. Linker: collect2 or ld

======================================================================
# -v: verbose, print intermediate steps
# -save-temps: save intermediate steps in the temp file?
gcc -v -save-temps -o hello hello.c

======================================================================
Most basic command for compile
gcc file.c

======================================================================
You can use various options to specify how to compile, how to print results, etc

======================================================================
gcc -g -W -Wall -O2 -o ouput file1.c file2.c

You compile file1.c and file2.c and you link compiled files and you create output executable

One of source files should have main()

-g: you create output file with including debugging information
which is needed when you sync source files and CPU actions

-W: Errors in source files are instantly detected by compiler 
but there can be vague parts in source files and in steps of compiling
This option prints "Warning" which is not an error but vague part
Recommended to turn on this option

-Wall: Print "Warning" message all vague parts
Recommended to turn on this option

-O2: optimization level2 (you also can use -O0,-O1,-O3)
When you compile, how much of optimization will be used?

Intensive optimization level results in more machine code ratio? (faster)
But higher intensive optimization level can result in higher probability of bad actions

-o: stands for output
Name of output executable file from compile

If you omit this option, a.out is autumatically used

======================================================================
Options for controling "print"
-E: you print result from preprocessing
-S: you perform only compile, you create *.s file
-c: you perform compile and assemble, you create *.o file
-v: you print each step of compile, print each command, print gcc version
-save-temps: you create intermediate file (*.i file, *.s file) from compile steps

======================================================================
Options for preprocessing
-D<Macro>[=value]: you define constant (#define)
this is used for selective compile or for defining external constant value
-I<dir>: this is used for adding paths of header files which compile looks at

======================================================================
Options for optimization on compile
-O<number>: higher numbers, higher optimization.
optimization is related to time for running program, related to the size of program
Higher values can result in more compile time, lower stability
-Os: optimization to reduce size of a program
-march=<CPU>: this creates a optimized code to a specific CPU

======================================================================
Options for linking
-l<library>: you specify "linking library"]
-L<dir>: you add path of library which the compiler will search
-static: you perform linking using a statc library
Otherwise, will you perform linking dynamically?

======================================================================
Other options:
-m32: you compile source codes to fit 32bit architect (simply 32bit CPU, you can use 32bit program on 64bit computer) of i386
-m64: you compile source codes to fit 64 architect of i386
-M,-MM: you print dependency information of source files
dependency information of source files is used for makefile