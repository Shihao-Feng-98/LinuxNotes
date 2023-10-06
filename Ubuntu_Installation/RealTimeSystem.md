# Preempt RT Patch

## x86 System
Here is **Ubuntu 20.04** as an example. The kernel with preempt real-time patch can be found in the [official source code](http://git.kernel.org/cgit/linux/kernel/git/rt/linux-stable-rt.git), and [rt-5.15.65-rt49](https://git.kernel.org/pub/scm/linux/kernel/git/rt/linux-stable-rt.git/snapshot/linux-stable-rt-5.15.65-rt49.tar.gz) is chosen in this tutorial;

### 1. Development tools
```shell
sudo apt install libncurses-dev libssl-dev libelf-dev bison flex
```

### 2. Setup
```shell
tar -zxvf linux-stable-rt-5.15.65-rt49.tar.gz
cd linux-stable-rt-5.15.65-rt49
make olddefconfig
make menuconfig 
```
then 
- `General Setup` -> `Preemption Model` -> `Fully Preemptible Kernel(RT)`

- `General Setup` -> `Timers subsystem` -> `old idle dynticks config` -> enable `High Resolution Timer Support`

- `General Setup` -> `Kernel hacking` -> `Compile-time checks and compiler options` -> disable `Compile the kernel with debug info`

- `Processor type and features` -> `Timer frequency` -> set `1000hz`

then 
```shell
gedit .config
```
- Change `CONFIG_SYSTEM_TRUSTED_KEYS="xxxx"` as `CONFIG_SYSTEM_TRUSTED_KEYS=""`

- Change `CONFIG_SYSTEM_REVOCATION_KEYS="xxxx"` as `CONFIG_SYSTEM_REVOCATION_KEYS=""`

- Set `CONFIG_DEBUG_INFO=n`

- Set `CONFIG_X86_X32=n (for bug "CONFIG_X86_X32 enabled but no binutils support")`

### 3. Build and install
```shell
make -j16
sudo make modules_install -j16
sudo make install -j16
sudo update-grub
sudo reboot
```

### 4. Fix error
If the error **"Missing file: arch/x86/boot/bzImage"** occurs, run 
```shell
make bzImage
``` 
before `make modules_install`. If the error **"zstd mssing"** occurs, run
```shell
make install zstd
```
----

## Arm System
Here is the hardware **Raspberry Pi 4B** as an example, and the **Debian 11 bullseye** system is installed which is recommended by officials. Burn the mirror system in windows, see [Installation Tutorial](https://shumeipai.nxez.com/2013/09/07/raspberry-pi-under-windows-system-installation-to-sd-card.html).

Hardware: raspberry pi 4B 4GB  
Operating system: [2021-01-11-raspios-buster-armhf-full](https://mirrors.tuna.tsinghua.edu.cn/raspberry-pi-os-images/raspios_armhf/images/raspios_armhf-2021-01-12/)


### 1. Development tools
```shell
sudo apt-get install bc
sudo apt-get install libncurses-dev libssl-dev
sudo apt-get install build-essential kmod cpio flex cpio bison
```

### 2. Setup
Dowload the source code
```shell
mkdir ~/kernel
cd ~/kernel
git clone https://github.com/kdoren/linux/tree/rpi-5.4.81-rt
```
Setup the kernel file
```shell
unzip linux-rpi-5.4.81-rt.zip 
KERNEL=kernel7l
cd linux-rpi-5.4.81-rt/
make bcm2711_defconfig
make menuconfig
```
Select `General setup` -> `Preemption Model (Fully Preemtible Kernel(RT))` -> `Fully Preemptible Kernel(RT)`

### 3. Build and install
```shell
make -j4 zImage modules dtbs
sudo make modules_install
```

### 4. Change real-time kernel
```shell
sudo cp arch/arm/boot/dts/*.dtb /boot/
sudo cp arch/arm/boot/dts/overlays/*.dtb* /boot/overlays/
sudo cp arch/arm/boot/dts/overlays/README /boot/overlays/
sudo cp arch/arm/boot/zImage /boot/$KERNEL.img
sudo reboot
```
----

## Check real-time system
Check the kernel version
```shell
uname -a
```
Check the latency of real-time system
```shell
sudo apt install rt-tests
sudo cyclictest -t 5 -p 80 -n
```

