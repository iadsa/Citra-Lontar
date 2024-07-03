import os
import PySimpleGUI as sg
import time

# Definisi layout GUI
def get_layout():
    background_color = "#FFFFFF"
    sg.theme("Reddit")

    file_list_column = [
        [sg.Text("Folder Gambar")],
        [
            sg.In(size=(25, 1), enable_events=True, key="ImgFolder"),
            sg.FolderBrowse(button_text="Pilih Folder"),
        ],
        [sg.Listbox(values=[], enable_events=True, size=(25, 15), key="ImgList")],
    ]

    image_viewer_column = [
        [sg.Text("Gambar Masukan")],
        [sg.Text(size=(40, 1), key="FilepathImgInput")],
        [sg.Image(key="ImgInputViewer")],
    ]

    image_info_column = [
        [sg.Text(size=(25, 1), key="ImgSize")],
        [sg.Text(size=(25, 1), key="ImgColorDepth")],
        [sg.Button("Lontar", key="Lontar", size=(20, 1))],
        [sg.Button("Reset", key="Reset", size=(20, 1))],  # Tombol reset
    ]

    layout = [
        [
            sg.Column(file_list_column, pad=(5, 0)),
            sg.VSeparator(pad=(20, 0)),  
            sg.Column(image_viewer_column, pad=(70, 0))
        ],
        [sg.HorizontalSeparator(pad=(0, 0))],
        [
            sg.Column(image_info_column, element_justification="left", pad=(0, 0)),
            sg.VSeparator(pad=(88, 0)),  
            sg.Column([[sg.Image(key="ImgOutputViewer")]], element_justification="center", pad=(0, 0), size=(1100, 300))
        ]
    ]

    return layout

def create_window():
    layout = get_layout()
    window = sg.Window("Lontar Bali", layout, resizable=True, finalize=True)
    return window

def animate_reset(window):
    for i in range(10):
        window.refresh()
        time.sleep(0.1)
    window["ImgOutputViewer"].update(data=None)
    window["ImgSize"].update("")
    window["ImgColorDepth"].update("")
