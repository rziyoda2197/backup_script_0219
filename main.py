import shutil

src = input("Qaysi papka backup: ")
dst = src + "_backup"

shutil.copytree(src, dst)
print("Backup tayyor:", dst)
