"""
File: main.py
Author: lnus 
Github: https://github.com/lnus
Description: A script that converts files to mp3 files
"""
import os
import time
import glob

class Converter(object):
    """Converts all the files in the current location to mp3"""
    def __init__(self):
        self.path = os.getcwd()
        if not os.path.exists("Finished"):
            os.system("mkdir Finished")
        self.formats = ["ogg", "mp4", "wav"]
        self.files = []

    def find_files(self):
        """finds all the files in self.path"""
        for f in self.formats:
            for item in glob.glob("*.{}".format(f)):
                self.files.append(item)
    
    def convert_files(self):
        """converts all files in self.files"""
        for f in self.files:
            filename = f[:-4] 
            os.system("ffmpeg -i {} Finished\{}".format(f, filename+".mp3"))
        
def main():
    """Main function"""
    c = Converter() 
    c.find_files()
    c.convert_files()

if __name__ == '__main__':
    main()
