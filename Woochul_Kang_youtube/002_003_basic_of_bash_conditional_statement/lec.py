What you can compare?
- numbers, strings
- return value from the command 
(if return value is 0, it means command was success)
- whether some file exist? what is the access permission of that file?

# ======================================================================
You can use if statement in one line
if TEST_COMMANDS; then COMMANDS; fi

You can use if statement in multiple lines
if condition
then
  statements
elif condition
then
  statements
else
  statements
fi

# ======================================================================
Test on files

if [-f /etc/passwd]; then
  ACTION
fi

-e file: check whether the file exists

-d file: check whether the file is a directory

-f file: check whether the file is a regular file 
(like not a symbolic link, directory, device node, etc)

-s file: check whether the file is non-zero size

-g file: check whether the file has sgid set

-u file: check whether the file has suid set

-r file: check whether the file is readable

-w file: check whether the file is writable

-x file: check whether the file is executable

# ======================================================================
if [ string1 == string2 ]; then
  ACTION
fi

if [ string1 != string2 ]; then
  ACTION
fi

#!/bin/bash

# section that reads the input
echo "Enter any color code for red or yellow or green, For exampele, type R or Y or G: "

# read input from the user 
# and assign value into COLOR variable
read COLOR

echo $COLOR

# section that compares the entry and disply a message
# if you use $COLOR, it can lead to the situation where [  == "R" ]
# which is syntax error
# So, you use "" to make if [ "" == "R" ]
if [ "$COLOR" == "R" ]
then
echo "STOP. LEAVE WAY FOR OTHERS"
elif [ "$COLOR" == "Y" ]
then
echo "GET READY YOUR WAY WILL BE OPEN SHORTLY"
elif [ "$COLOR" == "Y" ]
then
echo "MOVE.. IT IS YOUR TURN TO GO"
else
echo "INCORRECT COLOR CODE"
fi

# ======================================================================
You can do numerical test
by using following operators inside of [ ]

-eq: equal to
-ne: not equal to
-gt: greather than
-lt: less than
-ge: greather than or equal to
-le: less than or equal to


# ======================================================================
You can perform arithmetic expression in shell script
by using 3 ways

1. Use expr utility
# expr 8 + 8: Perform opertion
# $(expr 8 + 8): Get value itself by referencing
echo $(expr 8 + 8)

2. Use $((...)) (much used)
echo $((x+1))

3. Use let

letx=(1 + 2); echo $x

# ======================================================================
vim agetest.sh

#!/bin/bash

echo "put your age: "

read AGE

# ||: or
if [ $AGE -lt 20 ] || [ $AGE -gt 50 ] ; then
  echo "Sorry, your are out of the age range"
elif [ $AGE -gt 20 ] || [ $AGE -lt 30 ] ; then
  echo "You are in 20s"
elif [ $AGE -gt 30 ] || [ $AGE -lt 40 ] ; then
  echo "You are in 30s"
elif [ $AGE -gt 40 ] || [ $AGE -lt 50 ] ; then
  echo "You are in 40s"
fi

sudo chmod +x agetest.sh

./agetest.sh

