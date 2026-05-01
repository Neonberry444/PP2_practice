# with open("text.txt", "a") as f:
#   f.write("\nNow the file has more content!")
# with open("text.txt") as f:
#   print(f.read())


with open("text.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

with open("text.txt") as f:
  print(f.read())