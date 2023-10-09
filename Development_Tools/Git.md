# Git

#### Install git
```shell
sudo apt install git
```

#### Global git settings
Add the following lines in `/home/xxx/.gitconfig`
```
[user]
	name = xxxx
	email = xxx@xxx.com
[credential]
	helper = cache --timeout 3600
[url "https://github.com/"]
    insteadOf = git://github.com/
```

#### Show the current branch in terminal
Add the following lines in `~/.bashrc`
```shell
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] \$ "
```

#### [Git tutorial](https://github.com/Shihao-Feng-98/GitTutorial)