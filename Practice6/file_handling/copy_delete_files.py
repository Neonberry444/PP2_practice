# import shutil
# import os

# t = "text.txt"
# backup = "backup_text.txt"

# if os.path.exists(t):
#     shutil.copy(t, backup)
#     print("File was copied")
# else:
#     print("Source file not found.")

# print("\nBackup content:")
# with open(backup, "r") as f:
#     print(f.read())

import os
if os.path.exists("backup_text.txt"):
  os.remove("backup_text.txt")
else:
  print("The file does not exist")