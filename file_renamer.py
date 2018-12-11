import os

## Text to be replaced
part_replace = input('What replace = ')

## Text to replace with
with_what_replace = input('With what replace = ')

## Specific tupes of files:
type_of_file = input('What type of files, for example txt or jpg = ')

## Scans for current script location
cwd = os.getcwd()
for file in os.listdir(cwd):
    if file.endswith('.' + type_of_file):
        os.rename(file,file.replace(part_replace, with_what_replace))
        
print('Done')
