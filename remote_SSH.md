# Client
```
sudo apt install openssh-client
```

# Server
```
sudo apt install openssh-server
```

check whether ssh is started, and should show `sshd`
```
sudo ps -e | grep ssh
```

if not, run
```
sudo server ssh start
```

check ip address
```
ifconfig
```
