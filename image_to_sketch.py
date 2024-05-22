import os
from tkinter.filedialog import askopenfilename
import numpy as np
import cv2
from tkinter import *
# ---------Functions-----------
def imageSelect():
    global img
    img = askopenfilename()

    sbar.update()
    statusvar.set(f"{img}")
    
def imageTransform():
    statusvar.set("Uploading.....")

    image = cv2.imread(f"{img}")
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255 - grey_image

    blur = cv2.GaussianBlur(inverted,(21,21), 0)
    invertedblur = 255 - blur

    sketch = cv2.divide(grey_image, invertedblur, scale=256.0)
    cv2.imwrite(f"C:\\Users\\Adrash\\Documents\\Python\\python_modules\\imageSketch\\Sketchs\\{name_value.get()}.png", sketch)

    sbar.update()  #tkiter optimize the resources to save time so we have to give an update call to update a variable
    import time
    time.sleep(2)
    statusvar.set("Image is Saved")
    os.system(f"C:\\Users\\Adrash\\Documents\\Python\\python_modules\\imageSketch\\Sketchs\\{name_value.get()}.png")
# ----x------x------x-----x-----x


root = Tk()
root.title("Welcome to image to sketch")
root.geometry("500x400")
# -------------------------------
photo = PhotoImage(file="search.png")
root.iconphoto(False, photo)
# -------------------------

text = Label(text="Transform your Image to Sketch",font="Lucida 15 bold",pady=12).pack(anchor="center", side=TOP)


button_select = Button(text="Select Image", borderwidth=2, relief=RIDGE, pady=10,padx=15,command=imageSelect).pack(pady=25)

# ---------Ask for file name--------
name_value = StringVar()
name_value.set("Give the file name (No exensions)")
pathSave = Entry(textvariable=name_value, font="comicsansns 10 bold",width=35).pack(pady=10)
# --------------------------------------

button_main = Button(text="Transform", borderwidth=2, relief=RIDGE, pady=10,padx=15, command=imageTransform).pack(pady=25)
# -----------Menubar down----------------
statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
# -------------------------------
root.mainloop()
