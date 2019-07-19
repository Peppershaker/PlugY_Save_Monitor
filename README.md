# PlugY Save Monitor
Prevent Diablo II mod PlugY from corrupting saved games through automated interval backup and restore.

## How It Works
PlugY is not a 100% stable mod and it crashes quite often. For me, the frequency is around once every few hours. When the crash hapens,  the game sometimes overwrites the character stash save file `char_name.d2s` with an empty file of under 1KB in size. This casues all of your items in your stash to dissappear.

The script monitors for the file size of the save files, and when the file size goes under ~1KB, it will restore the backed up saved game files.

Note that in order for the restore operation to complete, we will need to terminate `Game.exe` and reload the backup save files. *If you are running Diablo with admin priviliges, you will NOT be able to terminate the game without also running this script /w admin priviliges.* 

In other words, if you are botting with D2ETAL you will need to run the script /w admin privilige.

## Quick Start
Open `plugy_save_monitor.py` with text monitor and change the save file locations. You can run the script afterwards.

This script has no external dependencies. 
