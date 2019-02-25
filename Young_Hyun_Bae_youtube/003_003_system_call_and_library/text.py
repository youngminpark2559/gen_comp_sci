Let's see how to use "service" of OS

Aside from the concept of service, 
generaly, OS doesn't allow user programs to directly access to system resouces
due to the security issue

# ======================================================================
So, various functionalities which use system resouces
is provided by OS

user program only should request it to OS
which is called "system call"

When you do "system call", you use "system functions"

# ======================================================================
Formerly, "system call" means a progamming interface for the services which OS provides.
Simply, "system call" means system functions which OS provides.

# ======================================================================
If you don't know detailed architecture of hardwares,
"system call" does abstract "mechanism of hardware"
so you can access to hardwares via OS

So, the thing you need to know is 
that "read system function", "file name you want to read", 
"memory space where you save file"
for bringing file from hardward, which is convenience 
because you don't need to know hardware 
as well as you don't need to write code to access to hardware

And you only can access to hardware via OS,
which is safety.

# ======================================================================
System functions are generally written in C/C++

# ======================================================================
Refer "section 2" from "man page"
to see "unistd.h", "fcntl.h", "semaphore.h", etc

# ======================================================================
https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Young_Hyun_Bae_youtube/pics/2019_02_25_10:11:39.png

Example of using system call

In source file, you read a file, 
and you copy and paste that file into another directory.

Internally, various steps are performed by OS services.

# ======================================================================
System call means a programming interface which OS directly provides.

The programming interface which OS directly provides can't provide various functionalities
but can ony provide very-basic-functionalities
because size of OS code should be small and fast as much as possible
so, OS code can't have complicated functionalities.

For example, imagine printf()
You can display a varialbe via printf()
In some case, you can print integer value, in other case, you can print string
This compilicated functionalities are not provided by system call of OS.

# ======================================================================
System call provides simple function 
of printing specific value, writing specific value, etc

# ======================================================================
So, programmers need 
high-level-collection-of-functions to use functions conveniently.

High-level-collection-of-functions is called 
"application program interface (API) or system library."

# ======================================================================
Application program interface (API) or system library are 
not a part of the kernel, are not a part of OS.

Application program interface (API) or system library is a library
which uses kernel service, so, it provides more convenient functions

# ======================================================================
You can create your own API.

APIs should follow a standard to run APIs on various platforms.

Example of API:
Win32 API (for Windows)
POSIX API (for UNIX, Linux, Mac OS)
Java API (for Java virtual machine)

# ======================================================================
Example of standard API

- fread() from POSIX API

size_t fread(
  void *buffer,
  size_t size,
  size_t count,
  FILE *stream);

size_t: return type

fread: function name

Parameters
void *buffer: buffer space in which you write data after reading data
size_t size: size of object which becomes the unit of reading (as bytes)
size_t count: number of objects which will be read into the buffer
FILE *stream: a file which you will read

# ======================================================================
https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Young_Hyun_Bae_youtube/pics/2019_02_25_10:28:46.png

User application: your own program

open(): system function which is written in your program
to use system service

when open() is called via "system call interface", 
"system call interrupt" occurs and processes your call from open()

# ======================================================================
When you call open(), it doesn't mean you directory call system function open()

The mode should be changed first from user mode to kernel mode.

The mode is changed by "system call interrupt" against OS.

# ======================================================================
OS has "interrupt vector"

Contents of "interrupt vector" is like
open: 10, read: 11, write: 12, etc

open() of system function is executed via "interrupt vector"

While processing system function open(),
your code running is being stopped.

# ======================================================================
How "library" is executed?

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Young_Hyun_Bae_youtube/pics/2019_02_25_11:07:08.png

The illustration looks similar to the illustration of "system call"

It's because when you use "library",
"system call" happens in the end.

# ======================================================================
printf() in your code is not system function (not system call)

printf() is a function which is provided from the section 3 of man page

printf() is a system library functon.

# ======================================================================
printf() is not executed in the kernel.

printf() is executed in the standard C library.

standard C library calls system function write().

And after that, steps are same with the case of "direct system call."

# ======================================================================
https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Young_Hyun_Bae_youtube/pics/2019_02_25_11:12:00.png

# ======================================================================
System call, library call are all based on function

Let's see how parameters are passed to the kernel.

# ======================================================================
Way of passing parameters:

1. Stores parameters into a register which is directly attached to CPU 
rather than a memory and pass parameters to the kernel.
This way is generally used when the program is executed on ARM CPU.
It's because ARM CPU has more registers.
so using registers makes faster passing parameters.
Pros: fast
Cons: you have limited number of registers.
so, you can't pass many paramters,
but you can pass a couple of integer values.

2. You store parameters into blocks or tables of memory,
which is used when you pass large number of parameters.

Importantly note that you store parameters into memory,
and you pass addresses of memory 
in which parameters are stored to register then to CPU

illustration:
https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Young_Hyun_Bae_youtube/pics/2019_02_25_11:20:47.png

code for system call 13: you have to proceed your task by using system call 13
When you do that, 
you have to use memory for paramter (gray square marked by "parameters")

Since memory is too large,
instead of passing memory (marked by "parameters") to "operating system"
you pass address (X above register) 
and "operating system" accesses to memory (marked by "parameters")

3. You use "stack" memory. 
Your program puts (PUSH) parameters into "stack" memory,
and OS takes (POP) that parameters

This is most general way to pass parameters in computer system.


Note that "2. block way" and "3. stack way"
don't have limitations in number of parameters and size (length) of parameters.

# ======================================================================
Types of "system calls"

- Process control

- File management

- Device management

- Information maintenance

- Communications

- Protection

# ======================================================================
Examples of system calls in Windows and Unix

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Young_Hyun_Bae_youtube/pics/2019_02_25_11:27:49.png
