for
while
until

# ======================================================================
# when list runs out, iteration exists
for variable_name in list
do
  commands
done

# --------------------------------------------------
#!/bin/sh

sum=0

for i in 1 2 3 4
do
  # $sum->0
  # $i->1
  # 0+1=1
  # $((1))->1
  sum=$(($sum+$i))
done

echo "The sum of $i numbers is: $sum"

# ======================================================================
# when condition is false, iteration exists
while condition is true
do
  commands
done

# --------------------------------------------------
#!/bin/sh

echo "Enter the number"
read no
fact=1
i=1

while [ $i -le $no ]
do
  fact=$(($fact * $i))
  i=$(($i + 1))
done

echo "The factorial of $no is: $fact"

# ======================================================================
# when condition is true, iteration exists
until condition is false
do
  commands
done

# --------------------------------------------------
#!/bin/sh

echo "NUMBER"

mn=1
mx=10

until [ $mn -gt $mx ]
do
  echo "$mn"
  mn=$(($mn + 2))
done
