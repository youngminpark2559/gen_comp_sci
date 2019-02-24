


# ======================================================================
https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_18:48:06.png

In a previous VCS, only differences are saved at each moment.

C1 means code version 1
At C2, A1 which is edited file A is stored along with C1 (picture might be wrong)

So, if you want to have final code (most-right one at C5),
you get all of differences up to C5

It's not efficient.

# ======================================================================
The way of git

# https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_18:48:57.png

# ======================================================================
git directory (repository) has your actual code

# https://raw.githubusercontent.com/youngminpark2559/gen_comp_sci/master/Woochul_Kang_youtube/pics/2019_02_24_18:50:25.png

- You perform "checkout the project" 
then you get copied code into your local PC (working directory)

- You edit codes

Status after this: modified

- There is sort of buffer zone called "staging area"
You "stage" edited files onto "staging area"

Why should you use "staging area"?
To review edited codes before commit

Status after this: staged

- You can "commit" to push your edited code into git directory (repository)

Status after this: commited

# ======================================================================
Basic workflow

- Init a repository 

You can clone codes from repository into your local working directory

- You stage the files to your staging area

- You do a commit, 
which stores the edited files in repository permanently

# ======================================================================
sudo apt-get install git

Set your identity
git config --global user.name "Your name"
git config --global user.email "your_mail@mail.com"

Check your setting
git config --list

# ======================================================================
Init a repository

There are 2 ways

1. Create a repository from the scratch
git init

2. clone an existing repository
git clone https://github.com/wchkang/helloworld.git

# ======================================================================
Edit hello.txt and edited file stays in working directory

In current directory where hello.txt file is located,
execute
git status

And you will see message

Changes not staged for commit
modified: hello.txt

# ======================================================================
Let's send edited file hello.txt to stage area
git add hello.txt

git status
Changes to be comminted
modified: hello.txt

# ======================================================================
Commit to store edit history and edited file into repository

git commit -m 'initial commin'

# ======================================================================
To view edit history
git log

# ======================================================================
Other options
git log -p : to check specific diff
git log --stat : to check summarized changes
git log --since=1.days : to check changes since 1 days ago

# ======================================================================
