import os
import shutil

path = "C:\\Users\\fourseven\\Desktop\\wow\\test2.txt"
dir = "C:\\Users\\fourseven\\Desktop\\direct"

try:
    # os.remove(path)
    # os.rmdir(dir)  # For removing directories. (will not delete directories that contain files)
    shutil.rmtree(dir)  # For removing directories that contain files. (unsafe)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You do not have permission to delete this file")
except OSError:
    print("Can not delete a non-empty directory")
else:
    print("Deleted file or directory.")














