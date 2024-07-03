import os
from PIL import Image, ImageOps
from processing import *
from layout import *
import PySimpleGUI as sg

filename_out = "out.png"

mode_to_coldepth = {
    "1": 1,
    "L": 8,
    "P": 8,
    "RGB": 24,
    "RGBA": 32,
    "CMYK": 32,
    "YCbCr": 24,
    "LAB": 24,
    "HSV": 24,
    "I": 32,
    "F": 32,
}

def print_pixel_values(img, label):
    pixels = img.load()
    print(f"{label} pixel values:")
    for i in range(min(3, img.width)):  # Print first 3 rows for brevity
        for j in range(min(3, img.height)):
            print(pixels[i, j], end=' ')
        print()
    print()

# Create the window
window = create_window()

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # Folder name was filled in, make a list of files in the folder
    if event == "ImgFolder":
        folder = values["ImgFolder"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif", ".jpg", ".jpeg"))
        ]
        window["ImgList"].update(fnames)

    elif event == "ImgList":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["ImgFolder"], values["ImgList"][0])
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename)

            img_input = Image.open(filename)
            # Size
            img_width, img_height = img_input.size
            window["ImgSize"].update(f"Image Size : {img_width} x {img_height}")

            # Color depth
            coldepth = mode_to_coldepth.get(img_input.mode, "Unknown")
            window["ImgColorDepth"].update(f"Color Depth : {coldepth}")

        except Exception as e:
            print(f"Error: {e}")
            pass

    elif event == "Lontar":
        try:
            filename = os.path.join(values["ImgFolder"], values["ImgList"][0])
            img_input = Image.open(filename)

            # Ensure coldepth is obtained before processing
            coldepth = mode_to_coldepth.get(img_input.mode, "Unknown")
            if coldepth == "Unknown":
                raise ValueError("Unsupported image mode")

            # Process the image
            img_output = Lontar(img_input, coldepth)
            img_output.save(filename_out)

            window["ImgOutputViewer"].update(filename=filename_out)

        except Exception as e:
            print(f"Error: {e}")
            pass

window.close()