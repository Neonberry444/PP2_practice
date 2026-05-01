import shutil
import os

# Move file
if os.path.exists("test/a.txt"):
    shutil.move("test/a.txt", "test/sub")

# Copy file
if os.path.exists("test/sub/a.txt"):
    shutil.copy("test/sub/a.txt", "test/a_copy.txt")

print("Done")