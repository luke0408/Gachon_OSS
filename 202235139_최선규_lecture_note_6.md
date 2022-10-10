# Git - 1

## Content
1. [Installing Git]()
2. [Git Config]()
3. [Git Commands]()

## 1. Installing Git

### Linux (install on a Debian-based distribution)
```bash
$ sudo apt install git-all
```

### Mac
<https://git-scm.com/download/mac>

### Windows - Run "Git Bash"
<https://git-scm.com/download/win>

### check pre-installed version
```bash
$ git --version
```

## 2. Git config

+ Git configurations are stored in three levels :
  |Levels|Option|Description|
  |:--|:--|:--|
  |System level|--system option.|Affects all uses and repositories on the system|
  |Global (user) level|--global option.|Affects all repositories of a current user|
  |Local level|--local option.|Specific to the current repository|

+ Git config options :
  |Options|Results|
  |:--|:--|
  |[--list]()|List all variables set in config file, along with their values.|
  |[--global]()|For writing options: write to global ~/.gitconfig file rather than the repository .|

  ### --list
  ```bash
  $ git config --list
  $ git config --list --show-origin
  ```

  ### --global
  ```bash
  $ git config --global user.name "SunKyu Choi"
  $ git config --global user.email zjvl324@gmail.com
  ```

  ```bash
  $ git config --list
  user.name=SunKyu Choi
  user.email=zjvl324@gmail.com
  ```

## 3. Git Commands

+ Init :
  - Initalizing a Repository in an Existing Directory
  ```bash
  $ git init
  ```

+ Status :
  - Checking Repository Status
  ```bash
  $ git status
  ```

+ branch
  ```bash
  $ git branch
  master
  $ git branch -m master main
  $ git branch
  main
  ```

+ Add :
  - Adding a new file to be staged
  ```bash
  $ git add [file_name]
  ```
  ```bash
  $ git add .
  ```

+ Unstaging :
  ```bash
  $ git rm -cached [file_name]
  ```

+ commit :
  ```bash
  $ git commit -m "commit message"
  ```

+ gitignore :
  - Ignoring a file
  ```text
  # ignore all .a files
  *.a

  # but do track lib.a, even though you're ignoring .a files above
  !lib.a

  # only ignore the TODO file in the current directory, not subdir/TODO
  /TODO

  # ignore all files in any directory named build
  build/

  # ignore doc/notes.txt, but not doc/server/arch.txt
  doc/*.txt

  # ignore all .pdf files in the doc/ directory and any of its subdirectories
  doc/**/*.pdf
  ```

