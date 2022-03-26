import subprocess

MESSAGE_COLOR = "\xb1[34m"
RESET_ALL = "\ xb1[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository... {RESET_ALL}")

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit","-m","initial commit"])

print(f"{MESSAGE_COLOR}The beginning of your destiny is define now! Create and have fun! {RESET_ALL}")