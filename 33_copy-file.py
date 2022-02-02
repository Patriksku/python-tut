# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file's creation and modification times)

import shutil

path = "C:\\Users\\fourseven\\Desktop\\test.txt"
toPath = "C:\\Users\\fourseven\\Desktop\\"

shutil.copyfile(path, toPath + "copy.txt")









