# Linux Configuration

## Basic settings
#### 1. Change software repository
Backup the official sources
```shell
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
```
Change software repository image as [Tsinghua sources](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/).

#### 2. Disable system updates
Open `Software & Updates` -> `Updates`
- Subscribed to: `All updates`
- Autonatically check for updates: `Never`
- When there are security updates: `Display immediately`
- When there are other updates: `Display every two weeks`
- Notify me of a new Ubuntu version: `Never`

#### 3. Install nvidia drviers
Find the recommended driver version
```shell
ubuntu-drivers devices
```
Open `Software & Updates` -> `Additional Drivers`, choose the driver closest to the recommended version, click `Apply Changes`.

Reboot and check 
```shell
nvidia-smi
```

#### 4. Uninstall 
Uninstall the useless software that installs with ubuntu installation, including
- games 
- microsoft office


#### 5. Update
```shell
sudo apt update
sudo apt upgrade
```

---

## Software
Download the deb package, run
```shell
sudo apt install ./xxx.deb
```
or install using apt
```shell
sudo apt install software_name
```

Some recommended software:
- Keyboard input method
  - [Sogoupinyin](https://shurufa.sogou.com/linux)
- Web browser
  - [Google Chrome](http://www.google.cn/chrome/index.html)
  - [Microsoft Egde Dev](https://www.microsoft.com/zh-cn/edge/download/insider?form=MA13FJ)
- Code editor
  - [Vscode](https://code.visualstudio.com/)
  - Vim: `sudo apt install vim`
- Media player
  - VLC: `sudo apt install vlc`
- Screen shot and recorder
  - Flameshot: `sudo apt install flameshot`
  - SimpleScreenRecorder: `sudo apt install simplescreenrecorder`
- Office software
  - [WPS](https://linux.wps.cn/)
  - [Flatpak](https://itsfoss.com/flatpak-guide/) + [Planner](https://flathub.org/apps/com.github.alainm23.planner?ref=itsfoss.com)
  - [Xmind](https://xmind.cn/)
- Remote tools
  - [ToDesk](https://www.todesk.com/linux.html)
  - ssh: `sudo apt install openssh-server`
- VPN
  - [MonoCloud](https://mymonocloud.com/)
