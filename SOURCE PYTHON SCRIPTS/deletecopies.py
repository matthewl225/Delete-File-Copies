import send2trash, os, re

#goes through the specified folder and deletes duplicates of files
#windows usually handles copies by adding '(number)' to the end of the filename
#sometimes appends ' - Copy' at the end

copyFileRegex = re.compile(r'(\(\d+\))|(\s\-\s(Copy)).\w+')
print('Input the address of the folder where you would like to delete copies in')
print('Close all files that might be sent to trash')
directory = input()

for folderName, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        test = copyFileRegex.search(filename)
        if test:
            send2trash.send2trash(directory + '\\' + filename)

print('Removed all copies')
            
                                  
