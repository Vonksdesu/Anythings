# ZZZ-Mod-Fixer (Community Update)

This is a Python-based tool designed to update and fix character skin mod hash IDs for the game **Zenless Zone Zero (ZZZ)** to ensure compatibility with the latest versions of the game.

---

## About The Project

This project is a community-driven continuation of the original **ZZZ-Mod-Fixer** tool. 

Since the original creator has not released any new updates, I have taken the initiative to update the program independently to support Zenless Zone Zero versions **2.6 to 2.8**. 

### Key Improvements in This Version:
* **Updated Hash Database**: Added support for newer character hashes (v2.6 – v2.8).
* **Backup File Conflict Fix**: In the original version, updated `.ini` mod files often conflicted with the backup (original) `.ini` files when left in the same folder. I have modified the code to automatically move the old/backup `.ini` files to a separate folder, preventing any conflicts and keeping your mod directory clean.

*Note: This tool is exclusively designed to fix and update character skin mods. It is not intended for other types of mods.*

---

## Project Origins & Credits

This project is built upon the amazing work of the original creators in the modding community.

* **Original Tool on GameBanana**: [ZZZ-Mod-Fixer (GameBanana)](https://gamebanana.com/tools/21671)
* **Original Owner**: [petrascyll](https://gamebanana.com/members/2644630)
* **Contributors**:
  * [HammyCate](https://gamebanana.com/members/3539653)
  * [EnteleJiang](https://gamebanana.com/members/4064027)

---

## Disclaimer

This project is not my own original creation from scratch; I am simply maintaining and updating it of my own volition to keep the tool working for the community. 

As this is my first time maintaining a project like this and I am working on it solo, there may still be bugs or edge cases where some mods cannot be fully repaired. I apologize for any inconvenience, and I highly appreciate your understanding and support!

---

## How to Use

1. **Download**: Download the latest `zzz-mod-fixer-2.8.exe` from the [Releases](../../releases) page.
2. **Placement**: Place the `.exe` file **directly** inside the `Mods` folder within your **XXMI Launcher** installation directory. 
   > ⚠️ **Important:** Do *not* create a new folder for the `.exe` inside the `Mods` folder, as the program may not work properly.
3. **Run**: Run the program and wait for the process to complete.
4. **Launch**: Once the process is finished, open your **XXMI Launcher** and launch *Zenless Zone Zero*.
