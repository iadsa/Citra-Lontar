import os
import PySimpleGUI as sg

# GUI layout definition
def get_layout():
    background_color = "#F5EEE6"
    sg.theme("DefaultNoMoreNagging")

    file_list_column = [
        [sg.Text("Image Folder")],
        [
            sg.In(size=(15, 1), enable_events=True, key="ImgFolder"),
            sg.FolderBrowse(),
        ],
        [sg.Listbox(values=[], enable_events=True, size=(15, 15), key="ImgList")],
    ]

    image_viewer_column = [
        [sg.Text("Input Image")],
        [sg.Text(size=(40, 1), key="FilepathImgInput")],
        [sg.Image(key="ImgInputViewer")],
    ]

    image_viewer_column2 = [
        [sg.Text("Output Image")],
        [sg.Image(key="ImgOutputViewer")],
        [sg.Text(size=(25, 1), key="ImgSize")],
        [sg.Text(size=(25, 1), key="ImgColorDepth")],
        [sg.Button("Lontar", key="Lontar")],
    ]

    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(
            [
                
                [
                    sg.Column(
                        image_viewer_column, scrollable=True, size=(1100, 300)
                    )
                ],
                [sg.Column(image_viewer_column2,  scrollable=True, size=(1100, 400))],
            ]
        ),    
        
        ]
    ]

    return layout


def create_window():
    layout = get_layout()
    window = sg.Window(
        "Lontar Bali", layout, resizable=True, finalize=True
    )
    return window
