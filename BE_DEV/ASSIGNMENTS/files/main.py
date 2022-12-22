__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# ASSIGNMENT: FILES - THIJS BREUKEL

import os
import shutil


def main():
    clean_cache() # Check Part #1
    cache_zip(data_path, cache) # Check Part #2
    print(cached_files()) # Check Part #3
    print(find_password(cached_files())) # Check Part #4
   

wd = os.getcwd()
cache = os.path.join(wd, 'files', 'cache')
data_path = os.path.join(wd, 'files', 'data.zip')

# 1: 
# clean_cache: takes no arguments and creates an empty folder named cache in the current directory. 
# If it already exists, it deletes everything in the cache folder.

def clean_cache():
    if os.path.exists(cache):
        shutil.rmtree(cache)
    os.mkdir(cache)

#2:
# cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, in that order. 
# The function then unpacks the indicated zip file into a clean cache folder.

def cache_zip(zip_file_path, cache_dir_path):
    shutil.unpack_archive(zip_file_path, cache_dir_path)

#3: 
# cached_files: takes no arguments and returns a list of all the files in the cache. 
# The file paths should be specified in absolute terms.

def cached_files():
    os.chdir(cache)
    cached_files_list = [os.path.abspath(x) for x in os.listdir(cache)]
    return cached_files_list

#4:
# find_password: takes the list of file paths from cached_files as an argument. 
# This function should read the text in each one to see if the password is in there.
# Once found, find_password should return this password string.

def find_password(cached_files):
    for file in cached_files:
        with open(file) as f:
            content = f.read()
            for line in content.split('\n'):
                if 'password' in line:
                    return line.replace('password: ', '')

if __name__ == '__main__':
    main()