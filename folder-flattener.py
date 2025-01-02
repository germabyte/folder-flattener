import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class FileCopierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Copier")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.configure(padx=10, pady=10)

        # Apply a modern theme
        style = ttk.Style(self.root)
        style.theme_use('clam')

        # Initialize variables
        self.source_folder = tk.StringVar()
        self.target_folder = tk.StringVar()
        self.status_message = tk.StringVar()
        self.progress = tk.DoubleVar()
        self.selected_file_types = {}
        self.copying = False
        self.cancel_event = threading.Event()

        # Define standard file types
        self.file_types = {
            "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
            "eBooks": [".epub", ".mobi", ".azw3"],
            "Media": [".mp3", ".mp4", ".mkv", ".avi", ".flac", ".wav"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
            "Scripts": [".py", ".js", ".html", ".css", ".sh", ".bat"],
            "Others": [".csv", ".json", ".xml"]
        }

        # Create UI Components
        self.create_widgets()

    def create_widgets(self):
        # Source Folder Selection
        source_label = ttk.Label(self.root, text="Source Folder:")
        source_label.grid(row=0, column=0, sticky='w')

        source_frame = ttk.Frame(self.root)
        source_frame.grid(row=1, column=0, columnspan=3, sticky='ew', pady=(0,10))

        self.source_entry = ttk.Entry(source_frame, textvariable=self.source_folder, width=60, state='readonly')
        self.source_entry.pack(side='left', fill='x', expand=True)

        browse_source_btn = ttk.Button(source_frame, text="Browse", command=self.browse_source)
        browse_source_btn.pack(side='left', padx=5)

        # Target Folder Selection
        target_label = ttk.Label(self.root, text="Target Folder:")
        target_label.grid(row=2, column=0, sticky='w')

        target_frame = ttk.Frame(self.root)
        target_frame.grid(row=3, column=0, columnspan=3, sticky='ew', pady=(0,10))

        self.target_entry = ttk.Entry(target_frame, textvariable=self.target_folder, width=60, state='readonly')
        self.target_entry.pack(side='left', fill='x', expand=True)

        browse_target_btn = ttk.Button(target_frame, text="Browse", command=self.browse_target)
        browse_target_btn.pack(side='left', padx=5)

        # File Type Selection with Scrollbar
        file_type_label = ttk.Label(self.root, text="Select File Types to Preserve:")
        file_type_label.grid(row=4, column=0, sticky='w')

        file_type_frame = ttk.Frame(self.root)
        file_type_frame.grid(row=5, column=0, columnspan=3, sticky='nsew')

        # Add a canvas and scrollbar for file type checkboxes
        canvas = tk.Canvas(file_type_frame)
        scrollbar = ttk.Scrollbar(file_type_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Create checkboxes for each file type category
        for category, extensions in self.file_types.items():
            cat_frame = ttk.LabelFrame(scrollable_frame, text=category)
            cat_frame.pack(fill='x', padx=5, pady=5)

            for ext in extensions:
                var = tk.BooleanVar(value=True)  # Default to selected
                chk = ttk.Checkbutton(cat_frame, text=ext, variable=var)
                chk.pack(side='left', padx=5, pady=2)
                self.selected_file_types[ext] = var

        # Progress Bar and Percentage
        progress_label = ttk.Label(self.root, text="Progress:")
        progress_label.grid(row=6, column=0, sticky='w', pady=(10,0))

        progress_frame = ttk.Frame(self.root)
        progress_frame.grid(row=7, column=0, columnspan=3, sticky='ew')

        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress, maximum=100)
        self.progress_bar.pack(side='left', fill='x', expand=True)

        self.progress_percent = ttk.Label(progress_frame, text="0%")
        self.progress_percent.pack(side='left', padx=10)

        # Status Message
        status_frame = ttk.Frame(self.root)
        status_frame.grid(row=8, column=0, columnspan=3, sticky='ew', pady=(10,0))

        self.status_label = ttk.Label(status_frame, textvariable=self.status_message, foreground="blue")
        self.status_label.pack()

        # Control Buttons
        control_frame = ttk.Frame(self.root)
        control_frame.grid(row=9, column=0, columnspan=3, sticky='ew', pady=(20,0))

        self.copy_button = ttk.Button(control_frame, text="Copy Files", command=self.start_copy)
        self.copy_button.pack(side='left', expand=True, fill='x', padx=5)

        self.cancel_button = ttk.Button(control_frame, text="Cancel", command=self.cancel_copy, state='disabled')
        self.cancel_button.pack(side='left', expand=True, fill='x', padx=5)

        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)
        self.root.columnconfigure(2, weight=0)
        self.root.rowconfigure(5, weight=1)

    def browse_source(self):
        folder = filedialog.askdirectory(title="Select Source Folder")
        if folder:
            self.source_folder.set(folder)
            self.status_message.set("Source folder selected.")

    def browse_target(self):
        folder = filedialog.askdirectory(title="Select Target Folder")
        if folder:
            self.target_folder.set(folder)
            self.status_message.set("Target folder selected.")

    def start_copy(self):
        source = self.source_folder.get()
        target = self.target_folder.get()

        if not source:
            messagebox.showwarning("Input Required", "Please select a source folder.")
            return
        if not target:
            messagebox.showwarning("Input Required", "Please select a target folder.")
            return
        if source == target:
            messagebox.showwarning("Invalid Selection", "Source and target folders cannot be the same.")
            return

        # Get selected file extensions
        selected_extensions = [ext for ext, var in self.selected_file_types.items() if var.get()]
        if not selected_extensions:
            messagebox.showwarning("No File Types Selected", "Please select at least one file type to preserve.")
            return

        # Disable buttons during copy
        self.copy_button.config(state='disabled')
        self.cancel_button.config(state='normal')
        self.status_message.set("Starting copy...")
        self.progress.set(0)
        self.progress_percent.config(text="0%")
        self.cancel_event.clear()
        self.copying = True

        # Start copy in a separate thread to keep UI responsive
        self.copy_thread = threading.Thread(target=self.copy_files_flat, args=(source, target, selected_extensions))
        self.copy_thread.start()

    def cancel_copy(self):
        if self.copying:
            if messagebox.askyesno("Cancel Copy", "Are you sure you want to cancel the copy process?"):
                self.cancel_event.set()
                self.status_message.set("Cancelling...")
        else:
            messagebox.showinfo("Cancel", "No copy operation to cancel.")

    def copy_files_flat(self, source_folder, target_folder, selected_extensions):
        try:
            # Gather all files that match the selected extensions
            all_matching_files = []
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    if os.path.splitext(file)[1].lower() in selected_extensions:
                        all_matching_files.append(os.path.join(root, file))

            total_files = len(all_matching_files)
            if total_files == 0:
                self.update_status("No matching files found to copy.")
                messagebox.showinfo("No Files", "No files matching the selected types were found.")
                self.reset_ui()
                return

            copied_files = 0

            for file_path in all_matching_files:
                if self.cancel_event.is_set():
                    self.update_status("Copy operation cancelled.")
                    messagebox.showinfo("Cancelled", "File copy operation was cancelled.")
                    self.reset_ui()
                    return

                file = os.path.basename(file_path)
                target_file_path = os.path.join(target_folder, file)

                # Handle duplicate filenames
                counter = 1
                base, extension = os.path.splitext(target_file_path)
                while os.path.exists(target_file_path):
                    target_file_path = f"{base}_{counter}{extension}"
                    counter += 1

                shutil.copy2(file_path, target_file_path)
                copied_files += 1
                progress_percent = (copied_files / total_files) * 100
                self.update_progress(progress_percent, f"Copied {copied_files} of {total_files} files.")

            self.update_status("Files copied successfully.")
            messagebox.showinfo("Complete", "Files copied successfully.")
        except Exception as e:
            self.update_status("Error during copy.")
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.reset_ui()

    def update_progress(self, percent, message):
        def callback():
            self.progress.set(percent)
            self.progress_percent.config(text=f"{percent:.2f}%")
            self.status_message.set(message)
        self.root.after(0, callback)

    def update_status(self, message):
        def callback():
            self.status_message.set(message)
        self.root.after(0, callback)

    def reset_ui(self):
        def callback():
            self.copy_button.config(state='normal')
            self.cancel_button.config(state='disabled')
            self.copying = False
        self.root.after(0, callback)

def main():
    root = tk.Tk()
    app = FileCopierApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
