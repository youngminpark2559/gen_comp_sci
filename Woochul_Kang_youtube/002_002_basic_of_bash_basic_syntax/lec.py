Bash shell script file isn't compiled
It works in the interpretation way.

# ======================================================================
Special characters in shell script

#: for comment except for #!
When #! is used at the first line like #!/bin/bash
it means this file is a shell script file.

\: concatenate break-lines

;: is used when you run multiple commands in sequence

$<variable_name>

# ======================================================================
make;make install;make clean
make&&make install&&make clean: stops when command runs into errors
cat file1||cat file2||cat file3: continues tasks until you don't meet an error.

# ======================================================================
Declare functions in the shell script file

# Args are not defined explicitly unlike other programming languages
function_name(){
  commands...
}

# ======================================================================
display(){
  echo "This is the message from the function"
  # $1 means first argument which is passed into the function
  echo "the parameter which is passed from calling process is" $1
}

# Pass argument with calling the function
display "Bob"
display "James"

# ======================================================================
/home/young/Pictures/2019_02_24_13:48:16.png

You can use any commands (which are defined in the Linux) in a shell script file

But there are categories on the commands

"Compiled applications" are excutable program file 
which are generally located in /usr/bin or /bin

"Built-in bash commands" don't have executable file
but they exist as a bash command which is defined in the bash program.

"Other script" means that you can use other shell scripts
by calling them from a shell script file.

# ======================================================================
Command substitution

You can use a result from the command as a part of the command on other command

To do this, there are 2 ways

1. you use backtick
`...`

2. you use $()

# ======================================================================
uname -r
4.14.41

# When bash interpreter executes this sentence pushd /lib/modules/`uname -r`
# first bash interpreter gets a result from uname -r
# second bash interpreter replaces `uname -r` with the resut from uname -r 
pushd /lib/modules/`uname -r`
/lib/modules/4.14.41 ~

# Other way but same effect
pushd /lib/modules/$(uname -r)

# ======================================================================
You can use variables in the shell script file

When you reference a variable (when you extract value of variable),
you use $
echo $MYCOLOR

When you assign and change value in variable,
you don't use $
MYCOLOR=blue
echo $MYCOLOR

# ======================================================================
Environment variables like HOME, PATH, HOST, etc are used in the same way with ordinary variables.
echo $PATH

# ======================================================================
You can get environment variables by using commands like env, set, printenv

# ======================================================================
The variables which are defined in the specific shell script file,
those variables are valid in only that shell script file.

# ======================================================================
If you want child process to access that variable,
you should decorate the variable with "export"

# variable VAR is exported,
# so child process can access variable VAR
export VAR=value

# Or you can use this sentence for same goal
VAR=value;export VAR

# ======================================================================
You can hand parameters in a script file.

# Pass /tmp
./script.sh /tmp

# Pass 100 2000
./script.sh 100 2000

# ======================================================================
Then, how to get paramters in a script file?

$0 returns the name of the script file (script.sh)

$1 means the first parameter (/tmp or 100)

$2, $3: second, third parameters (like 2000)

$*: reference all parameters

$#: number of parameters

# ======================================================================
vim ioscript.sh

# This script file is interpreted by /bin/bash 
#! /bin/bash

echo -n "Enter your name:"

# Read your input and assign it into sname variable
read sname

echo "Hello $name. You are wonderful."

chmod +x ioscript.sh

./ioscript.sh

# ======================================================================
