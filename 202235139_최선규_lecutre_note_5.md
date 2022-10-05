# 💻 CLI(Command Line Interface) 

## Contents

1. [I/O Redrection](#1-io-redection)
2. [Premissions](#2-premissions)
3. [Superuser](#3-superuser)
4. [Text Editors and Shell Script](#4-text-editor-and-shell-script)

## 1. I/O Redection

|Part|comment|
|:--|:--|
|[Standard Output](#standard-output)|By default, standard output is screen.|
|[Standard Input](#standard-input)|By default, standard input is from.|
|[Pipelines "\|"](#pipelines)|Pipeline feeds output of previous command to input of next command.|
|[Tip: Backslach](#tip-backslach)|Backslah can be used to ignore line change in command (“enter”), to enter a long command in multiple lines.|

### Standard Output
- By default, standard output is screen.
- You can redirect output using “>” after a command (e.g., ls) to create and save the output in a file
- Command “cat” displays the content of a text file.
- Using “>>” appends output to an extising file (if it already exitsts), or create and write to a new file if it doesn’t exist.

ex)
```sh
$ ls -lh > file_list.txt
$ cat file_list.txt
```
```sh
$ ls -lh >> file_list.txt
$ cat file_list.txt
```


### Standard Input
- By default, standard input is from keyboard.
- You can redirecct input from a file using “<”.
- You can mix “<“ and “>” together in a single line.

```sh
$ cat word.txt
school
class
home
new
lecture
$ sort < words.txt > sorted_words.txt
$ cat sorted_words.txt
class
home
lecture
new
school
```


### Pipelines "|"
- Pipeline feeds output of previous command to input of next command.
- command1 | command2 | command3 | … 

ex )
```sh
$ ls -lh | less
```


### Tip: Backslach
- Backslah can be used to ignore line change in command (“enter”), to enter a long command in multiple lines.

ex )
```sh
$ ls -l \
> --reverse \
> --human-readable \
```

## 2. Premissions
|Part|Comment|
|:--|:--|
|[Permissions](#premissions)|Files and directories have a permission assigned differently to owner / group / other in linux system.|
|[Changing Permissions](#changing-permissions)|“chmod” changes permissions.|

### Premissions
- Linux is a multi-user system.
- Files and directories have a permission assigned differently to owner / group / others.

ex )
```sh
$ ls -l /bin/bash
-rwxr-xr-x l root root 1113504 Jun 6 2019 /bin/bash
```

### Changing Permissions
- “chmod” changes permissions. 
- Change the permission of a file “word.txt” that only the owner (you) can read and write, but all the others (including others in the group) can only read it. No execution is needed for all users.


## 3. Superuser
- A superuser has all system administation authority.
- Some commands need superuser’s privilleges.
- Put “sudo” before the command if you are a superuser.

ex )
```sh
$ sudo some_command
```


## 4. Text Editor and Shell Script
|Part|Comment|
|:--|:--|
|[Text Editors](#text-editor)|A text editor is a program, like a word processor, that reads and writes ASCII text files.|
|[Shell Script](#shell-script)|A shell script is a file that contains ASCII text.|
|[Tip: History](#tip-history)|Type “history” to see previous command history. Or, save it to a text file.|

### Text Editor
- In Linux, you can choose CLI-based or GUL-based text editors

ex )
|Name|Description|Interface|
|:--|:--|:--|
|vi, vim|The granddaddy of Unix text editors, vi, is infamous for its obtuse user interface. On the bright side, vi is powerful, lightweight, and fast. Learning vi is a Unix rite of passage, since it is universally available on Unix-like systems. On most Linux distributions, an enhanced version of vi called vim is provided in place of vi. vim is a remarkable editor and well worth taking the time to learn it.|command line|
|Emacs|The true giant in the world of text editors is Emacs originally written by Richard Stallman. Emacs contains (or can be made to contain) every feature ever conceived of for a text editor. It should be noted that vi and Emacs fans fight bitter religious wars over which is better.|command line|
|nano|nano is a free clone of the text editor supplied with the pine email program. nano is very easy to use but is very short on features compared to vim and emacs. nano is recommended for first-time users who need a command line editor.|command line|
|gedit|	gedit is the editor supplied with the GNOME desktop environment. gedit is easy to use and contains enough features to be a good beginners-level editor.|graphical|
|kwrite|kwrite is the "advanced editor" supplied with KDE. It has syntax highlighting, a helpful feature for programmers and script writers.|graphical|

### Shell Script
- Write and run a shell script

### Tip: History
- Type “history” to see previous command history.  Or, save it to a text file.

ex )
```sh
$ history > history_command.txt
$ cat history
```