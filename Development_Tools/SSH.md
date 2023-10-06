# SSH
## Client
```shell
sudo apt install openssh-client
```

## Server
```shell
sudo apt install openssh-server
```
Check whether ssh is started, and should show `sshd`
```shell
sudo ps -e | grep ssh
```
If not, run
```shell
sudo server ssh start
```
Check ip address
```shell
ifconfig
```

## Log in server via ssh
```shell
ssh user_name@ip_address
exit
```

## Transfer files
```shell
scp local_file remote_user_name@remote_ip:remote_folder   
scp -r local_folder remote_user_name@remote_ip:remote_folder
```