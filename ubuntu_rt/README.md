# Ubuntu with Preempt_RT_patch
## Ubuntu 20.04
[Official source code](http://git.kernel.org/cgit/linux/kernel/git/rt/linux-stable-rt.git)

[rt-5.15.65-rt49](https://git.kernel.org/pub/scm/linux/kernel/git/rt/linux-stable-rt.git/snapshot/linux-stable-rt-5.15.65-rt49.tar.gz) is choosed;

### Install some libs and tools
```
sudo apt install libncurses-dev libssl-dev libelf-dev bison flex
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

4. `Processor type and features` -> `Timer frequency` -> set `1000hz`

```
gedit .config
```

change `CONFIG_SYSTEM_TRUSTED_KEYS="xxxx"` as `CONFIG_SYSTEM_TRUSTED_KEYS=""`

change `CONFIG_SYSTEM_REVOCATION_KEYS="xxxx"` as `CONFIG_SYSTEM_REVOCATION_KEYS=""`

set `CONFIG_DEBUG_INFO=n`

set `CONFIG_X86_X32=n (for bug "CONFIG_X86_X32 enabled but no binutils support")`

### Build and install
```
make -j16
sudo make modules_install -j16
sudo make install -j16
sudo update-grub
sudo reboot
```
### Debug
problem: 
```
*** Missing file: arch/x86/boot/bzImage
*** you need to run "make before "make install".
```

solution: 

before `make modules_install`, run
```
make bzImage
```
if zstd mssing, run
```
make install zstd
```


## Ubuntu 18.04
Download [kernel](https://mirrors.tuna.tsinghua.edu.cn/kernel/v5.x/) and [rt-patch](https://mirrors.tuna.tsinghua.edu.cn/kernel/projects/rt/5.4/older/)

### Install some libs and tools
```
sudo apt install build-essential git libssl-dev libelf-dev flex bison
```

### Setup
```
xz -cd linux-5.4.19.tar.xz | tar xvf -cd linux-5.4.19
xzcat ../patch-5.4.19-rt11.patch.xz | patch -p1
```

```
cp /boot/config-5.3.0-40-generic .config
```

```
make menuconfig
```
then

 `General Setup` -> `Preemption Model` -> `Fully Preemptible Kernel(RT)`

```
gedit .config
```
change `CONFIG_SYSTEM_TRUSTED_KEYS="debain/canoical-certs.pem` as `CONFIG_SYSTEM_TRUSTED_KEYS=""`


### Build and install
```
make -j8
sudo make modules_install -j8
sudo make install -j8
sudo update-grub
sudo reboot
```
### Check
```
uname -a
sudo apt install rt-tests
sudo cyclictest -t 5 -p 80 -n
```

