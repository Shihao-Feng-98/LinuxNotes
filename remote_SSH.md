## Client
```
sudo apt install openssh-client
```

## Server
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

## Log in server via ssh
```
ssh feng_shihao@192.168.5.155 # user_name@ip_address
exit # log out ssh
```

## Transfer files
```
scp local_file remote_user_name@remote_ip:remote_folder   # copy file
scp -r local_folder remote_user_name@remote_ip:remote_folder # copy folder
```
