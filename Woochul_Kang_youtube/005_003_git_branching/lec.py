There is a main line in software

And you sometimes want to develop software in different direction.

Having different flow of code is called branching.

# ======================================================================
And you can add "differently create code" into main line of code
which is called "merging"

# ======================================================================
The reason you do merging and branching is to do "non-linear programming"

# ======================================================================
Suppose you have coped code A from repository

And main line of A is called master

# https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:21:01.png

# ======================================================================
You edit A and get B

You edit B and get C

And master pointer points to latest code (C)

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:21:56.png

# ======================================================================
You create branch bug123
# -b: for creating branch
git checkout -b bug123

# To see your branches
git branch

# https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:23:04.png

star means code stream which you're working now

# ======================================================================
You edit C and get D

You edit D and get E

bug123 branch points to E

# https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:24:26.png

# ======================================================================
# When you merge code state of bug123 branch into master branch,
# first, you checkout to master branch

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:25:04.png

# ======================================================================
Then, you merge bug123 into master branch
git merge bug123

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:26:31.png

And master branch and bug123 branch point E (latest code)

# ======================================================================
Now, bug123 branch is no useful anymore
so, you can remove it
git branch -d bug123

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:28:28.png

# ======================================================================
Another possible scenario

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:29:04.png

# ======================================================================
you edit in master branch

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:29:35.png

# ======================================================================
To merge 2 branches,
first you checkout to master branch

git checkout master

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:30:21.png

# ======================================================================
git merge bug456

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:31:02.png

Contents (F and G) of bug456 branch are merged into master branch
and H becomes latest code

# ======================================================================
There is case where merging 2 branches work smoothly
when edit (D and E) in master branch has no common parts with edit (F and G) in bug456 branch

# ======================================================================
What if "D and E changes" edited same parts which "F and G changes" edited?

In that case, merging can happen automatically.

In that case, people should manually resolve conflict and then merge 2 branches again

# ======================================================================
After merging, you can delete bug456 branch

https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_20:37:35.png

# ======================================================================
