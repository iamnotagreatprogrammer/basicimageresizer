try:
    from tkinter.filedialog import asksaveasfile
    from tkinter.filedialog import askopenfile
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import *
    from tkinter import filedialog
    from PIL import ImageTk, Image
    import os
except ImportError:
    raise ImportError('function is not here')

def gui_input(prompt):
    root = tk.Toplevel()
    # this will contain the entered string, and will
    # still exist after the window is destroyed
    var = tk.StringVar()

    # create the dialog
    label = tk.Label(root, text=prompt)
    entry = tk.Entry(root, textvariable=var)
    label.pack(side="left", padx=(20, 0), pady=20)
    entry.pack(side="right", fill="x", padx=(0, 20), pady=20, expand=True)

    # Let the user press the return key to destroy the gui
    entry.bind("<Return>", lambda event: root.destroy())

    # this will wait until the window is destroyed
    root.wait_window()

    # after the window has been destroyed, we can't access
    # the entry widget, but we _can_ access the associated
    # variable
    value = var.get()
    return value

def directoryimageresize(): # function used for resizing image
    directory = filedialog.askdirectory(title="Select Directory containing image files") # open directory dialog to select location file to be resized are located in.
    while True:
        try:
            height = int(gui_input("Please enter height you would like image to be")) # enter new image height
            str(height)
        except ValueError:
            print("Not a valid number")
            continue
        else:
            break
    while True:
        try:
            width = int(gui_input("Please enter width you would like image to be")) # enter new image width
            str(width)
        except ValueError:
            print("Not a valid number")
            continue
        else:
            break

    savedirectory = filedialog.askdirectory(title="Select Directory to save files to") # opendirectory to set directory to save resized files to.

    for file_name in os.listdir(directory):
        print("Processing %s" % file_name)
        image = Image.open(os.path.join(directory, file_name)) # open directory path of directory set as directory containing files at beginning

        x,y = image.size
        new_dimensions = (int(width), int(height)) # set new dimensions (taken from variable created when entering values previously into text boxes).
        output = image.resize(new_dimensions, Image.ANTIALIAS) # create output file
        convertimage = output.convert('RGB') # convert image

        output_file_name = os.path.join(savedirectory, "resized_" + file_name) # save resized images to location selected (files created in the new location will have the same file names as originals but will be prefixed with _resized

        convertimage.save(output_file_name, "JPEG", quality = 95)

def singleimageresize():
     # function used for resizing image
    imagefile =  filedialog.askopenfilename(initialdir="/home", title = "Select image file to split",filetypes = (("png files","*.png"),("jpg files","*.jpg*"))) # - select image file to resize from dialog box
    while True:
        try:
            height = int(gui_input("Please enter height you would like image to be")) # enter new image height
            str(height)
        except ValueError:
            print("Not a valid number")
            continue
        else:
            break
    while True:
        try:
            width = int(gui_input("Please enter width you would like image to be")) # enter new image width
            str(width)
        except ValueError:
            print("Not a valid number")
            continue
        else:
            break

    savelocation = filedialog.asksaveasfilename(title="Select filename and directory to save to", defaultextension=".png",
    filetypes=(
                    ("PNG files", "*.png"),
                    ("JPG files", "*.jpg"),
                )
            )
 # set location to save file to and set filename to save new resized file as.

    print(savelocation)

    image = Image.open(os.path.join(imagefile)) # open file to resize

    x,y = image.size
    new_dimensions = (int(width), int(height)) # set new dimensions (taken from variable created when entering values previously into text boxes).
    output = image.resize(new_dimensions, Image.ANTIALIAS) # create output file
    convertimage = output.convert('RGB') # convert image

    output_file_name = os.path.join(savelocation) # save resized images
    if savelocation.endswith(".png"): # if file extension of saved file is set to .png
        convertimage.save(output_file_name, "PNG", quality = 95)
    elif savelocation.endswith(".jpg"):# if file extension of saved file is set to .jpg
        convertimage.save(output_file_name, "JPEG", quality = 95)



# main GUI code


root = tk.Tk()
root.resizable(False, False)
root.geometry("100x60")
root.wm_title("Basic Image Resizer")
resizeimage = tk.Button(text="Bulk Resize", command=directoryimageresize)
resizeimage.pack(anchor=CENTER)
singleresize = tk.Button(text="Single Resize", command=singleimageresize)
singleresize.pack(anchor=CENTER)
root.mainloop()



