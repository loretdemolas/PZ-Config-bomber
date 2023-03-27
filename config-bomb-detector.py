#################################################
#   A script to take a file and update the      #
#   server config.                              #
#################################################

# todo:
# Check to see if cofig bomb exists on startup




import os
import configparser
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the folder to monitor and the file extension to watch for
folder_to_watch = '/' # does python use relative or absolute dir
file_extension = '.txt' #look into alternative less used file extensions. 

# Define the path to the configuration file
config_file_path = '/servertest.ini' # does python use relative or absolute dir

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the created file has the desired extension
        if event.is_directory or not event.src_path.endswith(file_extension):
            return
        
        # Read the content of the created file
        with open(event.src_path, 'r') as f:
            content = f.read()
        
        # Update the configuration file
        config = configparser.ConfigParser()
        config.read(config_file_path)
        config['section_name']['key_name'] = content
        with open(config_file_path, 'w') as f:
            config.write(f)
        
        # Delete the created file
        os.remove(event.src_path)

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