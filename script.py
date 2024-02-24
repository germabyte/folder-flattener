import os
import shutil
from tkinter import Tk, filedialog, simpledialog, messagebox

def select_folder(prompt):
    root = Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title=prompt)
    root.destroy()
    return folder_path

def copy_files_flat(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(target_folder, file)
            
            # In case of duplicate filenames, append a number to the filename
            counter = 1
            base, extension = os.path.splitext(target_file_path)
            while os.path.exists(target_file_path):
                target_file_path = f"{base}_{counter}{extension}"
                counter += 1
            
            shutil.copy2(source_file_path, target_file_path)

if __name__ == "__main__":
    source = select_folder("Select source folder")
    if source:
        target = select_folder("Select target folder")
        if target:
            copy_files_flat(source, target)
            messagebox.showinfo("Complete", "Files copied successfully.")
        else:
            messagebox.showwarning("Cancelled", "Target folder selection was cancelled.")
    else:
        messagebox.showwarning("Cancelled", "Source folder selection was cancelled.")
