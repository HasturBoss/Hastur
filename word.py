from fpdf import FPDF
from PIL import Image
import os

pdf = FPDF()
imagelist = []                                                 # Contains the list of all images to be converted to PDF.


# --------------- USER INPUT -------------------- #

folder = "C:\\Users\\micor\\Desktop\\2019\\"                                                    # Folder containing all the images.
name = "2019.pdf"                                                      # Name of the output PDF file.


# ------------- ADD ALL THE IMAGES IN A LIST ------------- #

for dirpath, dirnames, filenames in os.walk(folder):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        full_path = os.path.join(dirpath, filename)
        imagelist.append(full_path)

imagelist.sort()                                               # Sort the images by name.
for i in range(0, len(imagelist)):
    print(imagelist[i])

# --------------- ROTATE ANY LANDSCAPE MODE IMAGE IF PRESENT ----------------- #

for i in range(0, len(imagelist)):
    im1 = Image.open(imagelist[i])                             # Open the image.
    width, height = im1.size                                   # Get the width and height of that image.
    if width > height:
        im2 = im1.transpose(Image.ROTATE_270)                  # If width > height, rotate the image.
        os.remove(imagelist[i])                                # Delete the previous image.
        im2.save(imagelist[i])                                 # Save the rotated image.
        # im.save

print("\nFound " + str(len(imagelist)) + " image files. Converting to PDF....\n")


# -------------- CONVERT TO PDF ------------ #

for image in imagelist:
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)                           # 210 and 297 are the dimensions of an A4 size sheet.

pdf.output(folder + name, "F")                                 # Save the PDF.

print("PDF generated successfully!")






import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
fig, ax = plt.subplots()
for i in range(10):    
    ax.plot(np.random.rand(10), '-o', ms=20, lw=2, mfc='blue')
    ax.grid()
    plt.title("Linear graph")
    plt.pause(1)
    plt.cla()
    if i==9:
        plt.pause(1)
        exit(0)

plt.show()






import win32com.client, sys, pathlib

ppt_path = "C://Users//micor//Desktop//YouTube//pptx//test.pptx"
mp4_path = "C://Users//micor//Desktop//YouTube//pptx//test.mp4"

def run(ppt_path, mp4_path):
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    ppt.Visible = 1
    ppt.DisplayAlerts = 1
    set = ppt.Presentations.Open(ppt_path)
    mp4_exit = pathlib.Path(mp4_path)
    try:
        set.CreateVideo(mp4_path, True)
    except:
        raise SystemExit
    else:
        print("Convert Successful!")
        while(1):
            if mp4_exit.is_file():
                print("MP4 exists!")
                set.Close()
                ppt.Quit()
                exit()

if __name__ == '__main__':
    run(ppt_path, mp4_path)







import pyttsx3

str = "C://Users//micor//Desktop//YouTube//pyttsx3//test.mp3"
txt = "C://Users//micor//Desktop//YouTube//pyttsx3//test.txt"

def tts(str):
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    
    volume = engine.getProperty('volume') 
    engine.setProperty('volume',1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    f = open(txt, "r")
    text = f.read()
    f.close()

    engine.save_to_file(text, str)
    engine.runAndWait()

if __name__=='__main__':
    tts(str)