# promt the user 
filename = input("File name: ").strip().lower()

# list a filetype in each type
if filename.endswith(".gif"):  # endswith use look like below png in filemname
    print("image/gif")
elif '.png' in filename:  # it is the same above with endswith
    print("image/png")
else: 
    print("Not Found")