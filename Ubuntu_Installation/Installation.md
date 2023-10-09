# Ubuntu/Win Dual System

**Note**: Disable secure boot before installation. Enter BIOS and set `Secure Boot Mode` -> `Disable`, then save and exit.

## 1. Single disk
### 1.1 Create a memory partition in win
Divide a partition of > 60G in the position of the last disk

### 1.2 Installation
- USB boot, choose `Install Ubuntu`
- Select minimum installation
- Select `other options` for manual partition
- Manually partition:
  - 500M, `logical partition`, `space starting position`, `for EFI system partition`
  - The size is generally 2 times the physical memory of the computer (50G), `primary partition`, `space starting position` `for SWAP`
  - 75G, `logical partition`, `space starting position`, `for ext4 journaling filesystem`, `the mount point is "/"`
  - The rest of the partition, `logical partition`, `space starting position`, `for ext4 journaling filesystem`, `the mount point is "/home"`
  - Device for boot loader installation, select 500M EFI partition
---

## 2. Dual disk
### 2.1 Create a memory partition in win
Divide a partition of > 200M in the position of the first disk for ubuntu boot, then divide a partition of > 60G in the position of the last disk.

### 2.2 Installation
- USB boot, choose `Install Ubuntu`
- Select minimum installation
- Installation type: select `other options` for  manual partition
- Manually partition:
  - Select 200M partition, 200M, `logical partition`, `space starting position`, `for EFI system partition`
  - Select 200G partition, the size is generally 2 times the physical memory of the computer (50G), `primary partition`, `space starting position` `for SWAP`
  - Select 200G partition, 50G, `logical partition`, `space starting position`, `for ext4 journaling filesystem`, `the mount point is "/"`
  - Select 200G partition, the rest of the partition, `logical partition`, `space starting position`, `for ext4 journaling filesystem`, `the mount point is "/home"`
  - Device for boot loader installation: select 200M EFI partition
