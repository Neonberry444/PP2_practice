import os

# Create directories
os.makedirs("test/sub", exist_ok=True)

# Create files
open("test/a.txt", "w").close()
open("test/b.py", "w").close()
open("test/sub/c.txt", "w").close()

# Show current directory
print("Current dir:", os.getcwd())

# List main folder
print("\nItems in test:")
for item in os.listdir("test"):
    print(item)
    print("\n.txt files:")