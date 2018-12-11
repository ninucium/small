import os


part_replace = input('What replace = ')
with_what_replace = input('With what replace = ')
cwd = os.getcwd()
for file in os.listdir(cwd):
    if file.endswith(".txt"):
        os.rename(file,file.replace(part_replace, with_what_replace))
