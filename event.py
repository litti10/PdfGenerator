import tkinter as tk
from tkinter import filedialog
from PIL import Image
import json

from utils import pillow_to_tk_image

def start_event(root, label, json_dict, image_size):
    # TODO: implement
    img = Image.new(mode='RGB', size=image_size)
    imgtk = pillow_to_tk_image(img)

    label.config(image=imgtk)
    label.image = imgtk

def load_event(root, label, json_dict, image_size):
    root.file = filedialog.askopenfile(
        initialdir='path',
        title='Select a custom json file',
        filetypes=(('json files', '*.json'), ('all files', '*.*'))
    )

    # TODO: make json file
    json_dict['image'] = True

    print(json_dict)
    print(root.file.name)

    popup=tk.Toplevel()
    popup.geometry("200x100")
    label=tk.Label(
        popup,
        text = 'File selected'
    )
    label.pack()
    close_button = tk.Button(
        popup,
        text="load compeleted",
        command=popup.destroy
    )
    close_button.pack()


def save_event(root, label, json_dict):
    with open(root.file.name, 'w') as f:
        json.dump(json_dict, f, indent = '\t')

    if root.file.name:
        popup=tk.Toplevel()
        popup.geometry("200x100")
        label=tk.Label(
            popup,
            text = 'File saved'
        )

        file_name = root.file.name.split('/')[-1]
        close_button = tk.Button(
            popup,
            text=file_name+" updated properly",
            command=popup.destroy
        )
        close_button.pack()
    else:
        popup=tk.Toplevel()
        popup.geometry("200x100")
        label=tk.Label(
            popup,
            text = 'Error'
        )

        file_name = root.file.name.split('/')[-1]
        close_button = tk.Button(
            popup,
            text=file_name+"json file not selected",
            command=popup.destroy
        )
        close_button.pack()