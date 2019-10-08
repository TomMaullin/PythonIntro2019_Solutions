# Change directory back to original working directory
os.chdir(pwd)

# import shutil and remove the testdir folder
import shutil
shutil.rmtree('testdir')