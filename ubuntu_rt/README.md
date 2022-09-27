# Ubuntu with Preempt_RT_patch
## Ubuntu 20.04
[Official source code](http://git.kernel.org/cgit/linux/kernel/git/rt/linux-stable-rt.git)

[rt-5.15.65-rt49](https://git.kernel.org/pub/scm/linux/kernel/git/rt/linux-stable-rt.git/snapshot/linux-stable-rt-5.15.65-rt49.tar.gz) is choosed;

### Install some libs and tools
```
sudo apt-get install libncurses-dev libssl-dev libelf-dev bison flex
```
### Setup
```
tar -zxvf linux-stable-rt-5.15.65-rt49.tar.gz
cd linux-stable-rt-5.15.65-rt49
make olddefconfig
make menuconfig 
```
then 

1. `General Setup` -> `Preemption Model` -> `Fully Preemptible Kernel(RT)`

2. `General Setup` -> `Timers subsystem` -> `old idle dynticks config` -> enable `High Resolution Timer Support`

3. `General Setup` -> `Kernel hacking` -> `Compile-time checks and compiler options` -> disable `Compile the kernel with debug info`

4. `Processor type and features` -> `Timer freqyency` -> set `1000hz`

```
gedit .config
```

change `CONFIG_SYSTEM_TRUSTED_KEYS="xxxx"` as `CONFIG_SYSTEM_TRUSTED_KEYS=""`

change `CONFIG_SYSTEM_REVOCATION_KEYS="xxxx"` as `CONFIG_SYSTEM_REVOCATION_KEYS=""`

set `CONFIG_DEBUG_INFO=n`

set `CONFIG_X86_X32=n (for bug "CONFIG_X86_X32 enabled but no binutils support")`

## Build and install
```
make -j16
sudo make modules_install -j16
sudo make install -j16
sudo update-grub
sudo reboot
```


## Ubuntu 18.04
