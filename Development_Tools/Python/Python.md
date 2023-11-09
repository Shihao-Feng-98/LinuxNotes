# Python
Generally, python is pre-install by linux system. And the version of pre-install python is shown in the following:

|    Linux    | python2 | python3 |
|     ---     |  :---:  |  :---:  |
| Ubuntu18.04 |   2.7   |   3.7   |
| Ubuntu20.04 |   ❌    |   3.8   |

## Builtin
Install pip3
```shell
sudo apt install python3-pip
```

## Conda
During python development, a different version of python is needed.   
Using conda to manage the virtual environment with different versions of python is recommended.  
**Anaconda** integrates many useful libraries and tools for python development and also integrates conda that easy to manage your pythton environment. 

#### Download [Anaconda](https://www.anaconda.com/download) and run the shell script
```shell
bash ./Anaconda3-2023.07-2-Linux-x86_64.sh
```

#### Create python environment
```shell
conda create --name env_name python=x.x.x
```

####  Activate specific python environment in terminal
```shell
conda activate env_name
```

#### Install modules in specific python environment 
Make sure the specific python environment is activate
```shell
conda install module_name # recommended
pip install module_name # optional
```

#### Auto enter another env
When opening a terminal, if you want to automatically enter a specific python environment instaed of `base` (the default python environment install by anaconda), add the following line in `~/bashrc`
```shell
conda activate env_name # auto enter conda env
```
  
#### Deactivate the current python environment
```shell
conda deactivate
``` 
**Note**: when you are in another environment and call this command, the terminal will activate `base`. Please call this command again, the terminal will enter the origin python environment that is pre-install by the linux system.

#### List all python environments that exist in your system 
```shell
conda env list
```

#### Use anaconda gui which provides many development tools and tutorials
```shell
conda activate base
anaconda-navigator # only work in base environment!
```
