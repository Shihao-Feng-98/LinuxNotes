# Raspberry pi 4B with RT-patch

## Install Debian system
Burn the mirror system in windows, see [burn_system](https://shumeipai.nxez.com/2013/09/07/raspberry-pi-under-windows-system-installation-to-sd-card.html).

You can burn the newest version (Debain 11 bullseye) of mirror system by using the official tool directly. If you want to burn the previous version (Debian 10 buster / Debian 9 strecth) of mirror system, please download the from [old_images](https://mirrors.tuna.tsinghua.edu.cn/raspberry-pi-os-images/raspios_armhf/images/)

## RT-patch
### Environment setup
Hardware: raspberry pi 4B 4GB
Operating system: [2021-01-11-raspios-buster-armhf-full](https://mirrors.tuna.tsinghua.edu.cn/raspberry-pi-os-images/raspios_armhf/images/raspios_armhf-2021-01-12/)

### Compile tools
```
sudo apt-get install bc
sudo apt-get install libncurses-dev libssl-dev
sudo apt-get install build-essential kmod cpio flex cpio bison
```

### Download source code
```
mkdir ~/kernel
cd ~/kernel
git clone https://github.com/kdoren/linux/tree/rpi-5.4.81-rt
```

### Setup kernel file
```
unzip linux-rpi-5.4.81-rt.zip 
KERNEL=kernel7l
cd linux-rpi-5.4.81-rt/
make bcm2711_defconfig
```

### RT setting
```
make menuconfig
```
choose `General setup` -> `Preemption Model (Fully Preemtible Kernel(RT))` -> `Fully Preemptible Kernel(RT)`

### Compile kernal and install
```
make -j4 zImage modules dtbs
sudo make modules_install
```

### Change kernel
```
sudo cp arch/arm/boot/dts/*.dtb /boot/
sudo cp arch/arm/boot/dts/overlays/*.dtb* /boot/overlays/
sudo cp arch/arm/boot/dts/overlays/README /boot/overlays/
sudo cp arch/arm/boot/zImage /boot/$KERNEL.img
```

## Check
```
sudo reboot
uname -a
```
### RT kernel test
```
sudo apt install rt-tests
sudo cyclictest -t 5 -p 80 -n # 5 thread，priority 80
```

