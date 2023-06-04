import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import pokemonName

def select_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("MKS files", "*.mks")])

    if file_path:
        file_name = os.path.basename(file_path)
        file_name_without_extension = os.path.splitext(file_name)[0]
        new_file_extension = ".ssa"

        output_directory = os.path.dirname(file_path)
        new_file_name = file_name_without_extension + new_file_extension
        output_file_path = os.path.join(output_directory, new_file_name)

        cmd_command = f'ffmpeg -i {file_path} {output_file_path}'

        subprocess.call(['cmd', '/c', cmd_command])
        read_ssa_file(output_file_path)

def read_ssa_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

        source_tuple = pokemonName.japanese_names
        replacement_tuple = pokemonName.english_names

        for word in source_tuple:
            if word in content:
                index = source_tuple.index(word)
                content = content.replace(word, replacement_tuple[index])

    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(content)

    print("File modifications saved.")

select_file()