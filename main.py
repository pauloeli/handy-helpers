import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from PIL import Image
from tabula.io import convert_into

window = tk.Tk()

window.title("Handy Helpers")
window.resizable(0, 0)

window.geometry("300x150+{}+{}".format(
    int(window.winfo_screenwidth() / 2 - 150), int(window.winfo_screenheight() / 2 - 50)))


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")],
                                           title="Select document")

    if not file_path:
        return

    file_save = filedialog.asksaveasfile(title="Save File", defaultextension=".csv",
                                         filetypes=[("CSV files", "*.csv")],
                                         initialdir=os.path.dirname(file_path))

    convert_into(file_path, file_save.name, output_format="csv", pages='all')
    messagebox.showinfo("Success", "File converted to CSV with success")


def select_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("All files", "*.*")],
                                             title="Please select images")

    if not file_paths:
        return

    images = [
        Image.open(file_path)
        for file_path in file_paths
    ]

    file_save = filedialog.asksaveasfile(title="Save File",
                                         defaultextension=".pdf",
                                         filetypes=[("PDF files", "*.pdf")],
                                         initialdir=os.path.dirname(file_paths[0]))

    images[0].save(file_save.name, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    messagebox.showinfo("Success", "PDF generated with success")


select_button = tk.Button(window, text="PDF to Spreadsheet", command=select_file, width=40)
select_button.grid(row=1, column=0, pady=5, sticky='n')

images_button = tk.Button(window, text="Images to PDF", command=select_images, width=40)
images_button.grid(row=2, column=0, pady=5, sticky='n')

images_button = tk.Button(window, text="Images to PDF", command=select_images, width=40)
images_button.grid(row=2, column=0, pady=5, sticky='n')

window.mainloop()
