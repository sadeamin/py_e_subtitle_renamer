from os import rename
import time



# for i in range(20):
#     remfile()
#     time.sleep(10)

# remfile()


from tkinter import *

window = Tk()
window.config(padx=50, pady=50, bg="#333333")
window.title("Subtitle_renamer")

text = Label(text="write what to replace: ", bg="#333333", padx=10, pady=10, fg="white")
text.pack()

entry = Entry()
entry.pack(padx=10, pady=15)
entry.insert(0, "-subtitle-en")
string_rename = entry.get()



def remfile():
    global string_rename
    print(f"\n\n\n\n")


    import os
    from tkinter import messagebox
    from tkinter.filedialog import askdirectory
    import glob

    path = askdirectory()

    os.chdir(path=path)

    str_list = glob.glob('*.srt')


    if len(str_list) > 0:
	    messagebox.showinfo(title="message", message="successfully replaced")


	    for i in range(len(str_list)):
	        os.rename(str_list[i], str_list[i].replace(f"{string_rename}", ""))
	        

	    print(str_list, len(str_list))
     
    else:
        messagebox.showerror(title="ERROR", message="THERE IS NO FILE!")
	
    print(f"\n\n\n\n")

button = Button(text="Open", bg="#4A4A4A", command=remfile)
button.pack()

window.mainloop()