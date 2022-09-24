# ✨ Shell commands

## Contents

1. [shell command](#1-shell-commands)
2. [manipulation](#2-manipulation)
3. [help command](#3-help-command)


## 1. Shell commands

|Command|Results|
|:--:|:--|
|[pwd](#pwd)|shows the current path in a hierarchical directory|
|[cd](#cd)|change directory|
|[ls](#ls)|list files and directories|
|[clear](#clear)|clear to now view|

### pwd
- show the current path in a hierarchical directory

ex)

```
$ pwd
/home/[user]
```

### cd
- change directory

ex)
```
$ pwd
/home/[user]
$ cd /Desktop
$ pwd
/home/[user]/Desktop
```

### ls
- list files and directories

|Options|Results|
|:--:|:--|
|-l|show detaild intormation (long format)|
|-lh|same as above, size in units|

ex)
```
$ ls
Documents Desktop Viedos etc...
$ ls -l
$ ls -lh
```

### clear
- clear to now view

ex)
```
$ clear
```

## 2. Manipulation

|manipulation|Results|
|:--:|:--|
|[cp](#cp)|copy files and directories|
|[mv](#mv)|move files and directories and rename them|
|[rm](#rm)|delete files and directories|
|[mkdir](#mkdir)|make a new directories|
|[wildcards](#wildcards)|Special characters that allow you to quickly specify file name groups|
### cp
- copy files and directories

ex)
```
$ cp [file name1] [file name1]
```

Examples of ***cp***

|Command|Results|
|:--|:--|
|cp file1 file2|Copies the contents of file1 into file2|
|cp -i file1 file2|if file2 exists, the user is prompted before it is overwritten with the content of file1|
|cp file1 dir1|Copy the content of file1 iniside of directory dir1|
|cp -R dir1 dir2|Copy the content of the dirctory dir1. If dirctory dir2 does not exist, it is created|


### mv
- move files and diresctories and rename them

ex)
```
$ mv [file naem1] [file name2]
```
```
$ mv file... directory
```

Examples of ***mv***

|Command|Results|
|:--|:--|
|mv file1 file2|If file2 does not exist, then file1 is renamed file2. If file2 exists, its contents are silently replaced with the contents of file1.|
|mv -i file1 file2|Like above however, since the "-i" (interactive) option is specified, if file2 exists, the user is prompted before it is overwritten with the contents of file1.|
|mv file1 file2 dir1|The files file1 and file2 are moved to directory dir1. If dir1 does not exist, mv will exit with an error.|
|mv dir1 dir2|If dir2 does not exist, then dir1 is renamed dir2. If dir2 exists, the directory dir1 is moved within directory dir2.|


### rm
- delete files and directories

ex)
```
$ rm file...
```
```
$ rm -r directory...
```

Examples of ***rm***

|Command|Results|
|:--|:--|
|rm file1 file2|Delte file1 and file2|
|rm -i file1 file2|Like above however, since the "-i" (interactive) option is specified, the user is prompted before each file is deleted.|
|rm -r dir1 dir2|Directories dir1 and dir2 are deleted along with all of their contents.|


### mkdir
- make a new directories

ex)
```
$ mkdir directory...
```

### wildcards
- Special characters that allow you to quickly specify file name groups

|Pattern|Matches|
|:--|:--|
|*|All file names|
|g*|All file names that begin with the character "g"|
|b*.txt|All file names that begin with the character "b" and end with the characters ".txt"|
|data???|Any file name that begins with the characters "Data" followed by exactly 3 more characters|

Using examples of ***wildcard***

|Command|Results|
|:--|:--|
|cp *.txt text_files|Copy all files in the current working directory with names ending with the characters ".txt" to an existing directory named text_files.|
|mv dir1 ../*.bak dir2|Move the subdirectory dir1 and all the files ending in ".bak" in the current working directory's parent directory to an existing directory named dir2.|
|rm *~|Delete all files in the current working directory that end with the character "~". Some applications create backup files using this naming scheme. Using this command will clean them out of a directory.|

## 3. Help command

|command|Using example|
|:--:|:--|
|help|$ help cd|
|man|$ man cp|
|exit|$ exit|