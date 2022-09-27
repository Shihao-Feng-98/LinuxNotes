# Linux python and pip version management

ubuntu 18.04 system pre-installed `python2.7` and `python3.6`

ubuntu 20.04 system pre-installed `python3.8`

## Install other version python
```
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.x python3.x-dev python3.x-distutils
```

if `add-apt-repository` hangs, run
```
sudo gedit /etc/gai.conf
```

then comment the following line

```
precedence:ffff:0.0/96 100
```
 
## Install corresponding pip version
```
wget -O /tmp/get-pip.py https://bootstrap.pypa.io/pip/3.x/get-pip.py
python3.x /tmp/get-pip.py
```

## Install modules in corresponding python version
```
pip3.x install xx
```

