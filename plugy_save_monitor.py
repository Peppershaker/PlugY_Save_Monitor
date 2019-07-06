from datetime import datetime
from time import sleep
import os
from shutil import copy2

class FileCorruptError(Exception):
    pass


def any_file_is_corrupt(save_directory, save_files):
    """Check for file corruption
    
    Args:
        save_directory: str
            save file directory
        
        save_file: tup
            a tuple containing a list of file names
    
    Returns:
        is_corrupt: bool
            if any of the files is corrupt. This is because if any
            of the save files are corrupt, all files needs to be
            backed up or restored together.
    """

    for save_file in save_files:
        # If files are less than 2KB, it is corrupt
        if os.path.getsize(os.path.join(save_directory, save_file)) < 2000:
            return True
        
        return False


def make_backup(char_backup_path, save_files):
    """Makes character backup
    
    Args:
        char_backup_path: str
            path of character backup directory

        save_files: tup
            a tuple containing a list of character save file names
    """
  
    # Check if directory exists
    if not os.path.exists(char_backup_path):
        os.makedirs(char_backup_path)

    # Check if files are corrupt
    if any_file_is_corrupt(plugy_save_dir, save_files):
        raise FileCorruptError("Files are corrupt, not saving")

    # Saving
    for save_file in save_files: 
        file_full_path = os.path.join(save_dir, save_file)
        copy2(file_full_path, char_backup_path)


def load_backup(char_backup_path, save_files):
    """Load character backup

    Args:
        char_backup_path: str
            path of character backup directory

        save_files: tup
            a tuple containing a list of character save file names 
    """

    # Paste backup files
    for save_file in save_files: 
        copy2(os.path.join(char_backup_path, save_file), plugy_save_dir)

    # Restart Diablo 2 to prevent current currupt game state to be saved again
    # Also loads recovered game save states
    os.system("taskkill /f /im  Game.exe")


def log_msg(msg, log_file_folder):
    if not os.path.exists(log_file_folder):
        os.makedirs(log_file_folder)
	
    with open(os.path.join(log_file_folder,'monitor_log.txt'), 'a') as f:
        f.write(msg + '\n')

if __name__ == '__main__':
    char_name = "Peppershaker"

    save_dir = 'E:/'
    
    char_backup_path = os.path.join(save_dir, char_name + '_bk')
    
    plugy_save_dir = os.path.join(char_backup_path, os.pardir)
    
    save_files = (char_name + '.d2s', char_name + '.d2x')
	
    log_file_folder = 'E:/PlugY_Monitor_Logs'

    while True:
        if any_file_is_corrupt(save_dir, save_files):
            # File is corrupt
            load_backup(char_backup_path, save_files)

            msg = "Successfully recovered at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_msg(msg, log_file_folder)
            print(msg)
        
        else:
            # File not corrupt
            make_backup(char_backup_path, save_files)

            msg = "Successfully backedup at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_msg(msg, log_file_folder)
            print(msg)

        # Check again in 5 minutes
        sleep(300)            