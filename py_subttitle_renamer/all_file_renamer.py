from os import rename, replace
import time
from tkinter import *
## creating the ui
window = Tk()
window.config(padx=50, pady=50, bg="#333333")
window.title("Subtitle_renamer")

text = Label(text="write what to replace: ", bg="#333333", padx=10, pady=10, fg="white")
text.pack()

entry = Entry()
entry.pack(padx=10, pady=15)
entry.insert(0, "-subtitle-en")

text = Label(text="write the type of file: ", bg="#333333", padx=10, pady=10, fg="white")
text.pack()

type_entry = Entry()
type_entry.pack(padx=10, pady=15)
type_entry.insert(0, "*.")


## creating the remfile function for renameing file
def remfile():
    string_rename = entry.get()
    type_file = type_entry.get()
    print(f"\n\n\n\n")


    import os
    from tkinter import messagebox
    from tkinter.filedialog import askdirectory
    import glob

    path = askdirectory()

    os.chdir(path=path)
    ## geting all type_file type files.using glob module
    str_list = glob.glob(type_file)


    if len(str_list) > 0:
        
        for i in range(len(str_list)):
            ### renameing the file using os module
            x = str_list[i].replace(string_rename, "")
            os.rename(str_list[i], x)
        
            print(x)
        
        messagebox.showinfo(title="message", message="successfully replaced")
     
    else:
        messagebox.showerror(title="ERROR", message="THERE IS NO FILE!")
	
    print(f"\n\n\n\n")


button = Button(text="Open", bg="#4A4A4A", command=remfile)
button.pack()
##
window.mainloop()

