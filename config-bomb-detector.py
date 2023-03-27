#################################################
#   A script to take a file and update the      #
#   server config.                              #
#   by loretdemolas feel free to use and edit   #
#################################################

import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from status import status

cwd = os.getcwd()

# Define the folder to monitor and the file extension to watch for
folder_to_watch = os.path.join(cwd) 
file_extension = '.txt' 

# Define the path to the configuration file
config_file_path = os.path.join(cwd, 'Server', 'servertest.ini') 
status('Current working directory ' + cwd,
       'Watching ' + folder_to_watch + ' for bomb',
       'location of config ' + config_file_path,
       'Monitoring folder'
       )

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the created file has the desired extension
        if event.is_directory or not event.src_path.endswith(file_extension):
            return
        
        with open(config_file_path) as f:
            lines = f.readlines()

        # read the input file line by line
        with open(event.src_path) as f:
                status('Bomb detected', 'Reading contents')
                for line in f:
                     # split the line into key-value pairs
                    split_line = line.strip().split('=')
                    if len(split_line) == 2:
                        key, value = split_line
                    elif len(split_line) == 1:
                        key = split_line[0]
                        value = ''
                    else:
                        continue
                    
                    # update the corresponding key in the ConfigParser object
                    for i, l in enumerate(lines):
                        if l.startswith(key + '='):
                            status(f"Updating {key} from {l.split('=')[1].strip()} --> {value}")
                            lines[i] = key + '=' + value + '\n'
                            break
                      

        with open(config_file_path, 'w') as f:
            f.writelines(lines)
            status("Configuration updated successfully")
        
        # Delete the created file
        os.remove(event.src_path)
        status('removing bomb')

if __name__ == '__main__':
    # Start monitoring the folder
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()