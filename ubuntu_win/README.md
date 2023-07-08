# Ubuntu and win dual system

## Disable secure boot before installation
Enter BIOS and set `Secure Boot Mode` -> `Disable`, then `F10`, save and exit.

## Single disk
### Create a memory partition in win
Divide a partition of > 60G in the position of the last disk

### Installation
1. USB boot, choose `Install Ubuntu`
2. Select minimum installation
3. Installation type: select `other options` for  manual partition
4. Manually partition:
  - 500M, `logical partition`, `space starting position`, `for EFI system partition`
  - the size is generally 2 times the physical memory of the computer (50G), `primary partition`, `space starting position` `for SWAP`
  - 75G, `logical partition`, `space starting position`, `for ext4 journaling filesystem`, `the mount point is "/"`
  - the rest of the partition, `logical partition`, `space starting position`, `for ext4 journaling filesystem`, `the mount point is "/home"`
  - Device for boot loader installation: select 500M EFI partition




## Dual disk
### Create a memory partition in win
Divide a partition of > 200M in the position of the first disk for ubuntu boot, then divide a partition of > 60G in the position of the last disk.

### Installation
1. USB boot, choose `Install Ubuntu`
2. Select minimum installation
3. Installation type: select `other options` for  manual partition
4. Manually partition:
  - Select 200M partition, 200M, `logical partition`, `space starting position`, `for EFI system partition`
  - Select 200G partition, the size is generally 2 times the physical memory of the computer (50G), `primary partition`, `space starting position` `for SWAP`
  - Select 200G partition, 50G, `logical partition`, `space starting position`, `for ext4 journaling filesystem`, `the mount point is "/"`
  - Select 200G partition, the rest of the partition, `logical partition`, `space starting position`, `for ext4 journaling filesystem`, `the mount point is "/home"`
  - Device for boot loader installation: select 200M EFI partition
