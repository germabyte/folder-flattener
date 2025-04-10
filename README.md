# 📁 Folder Flattener

## 1. Introduction and Purpose

### Introduction  
**Folder Flattener** is a desktop application that helps users collect and copy files of specific types from any folder (including subfolders) into a single destination folder. It includes a graphical user interface (GUI) to easily select source and target folders, choose file types, and track progress—all without writing a single line of code.

### Purpose & Problem Statement  
When working with deeply nested directories (e.g., downloads, media libraries, document archives), it’s often time-consuming to manually locate and extract files of certain formats. This program solves that by recursively scanning a folder structure and copying selected file types into one flat, organized destination.

### Value Proposition  
- Saves time by automating the collection of desired files.
- Ensures easy access to all files of interest in one place.
- Provides a clean, simple, and intuitive interface for users of all technical skill levels.

---

## 2. Dependencies (Required Software/Libraries)

The script is built using **Python's standard library only** and requires no third-party packages.

### Requirements:
- **Python 3.x**  
  Used to run the program and power the GUI with built-in `tkinter`.

> **Installation Instructions:**  
1. Download and install Python from the official website:  
   👉 [https://www.python.org/downloads](https://www.python.org/downloads)  
2. During installation, ensure the box labeled **"Add Python to PATH"** is checked.

---

## 3. Getting Started (Installation & Execution)

### Step-by-Step Guide

#### 1. **Download the Repository**
- Click the green `<> Code` button on the GitHub page.
- Choose `Download ZIP`.
- Extract the ZIP file to any folder of your choice.

#### 2. **Run the Program**
- Open the **Command Prompt (Windows)** or **Terminal (macOS/Linux)**:
  - Windows: Press `Win + R`, type `cmd`, press Enter.
  - macOS: Open Spotlight (`Cmd + Space`), type `Terminal`, press Enter.
- Navigate to the folder containing the script:
  ```bash
  cd path_to_extracted_folder
  ```
  Replace `path_to_extracted_folder` with the actual path (e.g., `Downloads/folder-flattener-main`).

- Run the program using:
  ```bash
  python folder-flattener.py
  ```

✅ The graphical interface will launch automatically.

---

## 4. User Guide (How to Effectively Use the Program)

### 📂 Step-by-Step Usage

1. **Select Source Folder**  
   Click the **"Browse"** button next to **Source Folder**, then choose the folder where your files are located.

2. **Select Target Folder**  
   Click the **"Browse"** button next to **Target Folder**, then choose where you want the collected files to be copied.

3. **Choose File Types**  
   - Check or uncheck specific file extensions by category (e.g., `.mp4`, `.pdf`, `.jpg`).
   - All types are selected by default for convenience.

4. **Start Copying**  
   Click **"Copy Files"** to begin. A progress bar and status message will keep you informed.

5. **Cancel Operation** *(Optional)*  
   You can cancel at any point by clicking **"Cancel"**.

### 🧾 Output Behavior
- The program **copies (not moves)** matching files into the selected target folder.
- All files are **flattened** into one directory (no subfolder structure).
- If files with the same name already exist, the program will automatically rename the new ones (e.g., `file_1.pdf`).

---

## 5. Use Cases and Real-World Examples

### ✅ Use Case 1: Collecting All PDFs from a Research Folder  
**Problem:** A student has hundreds of academic PDFs scattered across multiple subfolders.  
**Action:**  
- Set the main folder as source.  
- Select `.pdf` under "Documents".  
- Set Desktop as target folder.  
**Result:** All PDFs copied to one easy-access location.

---

### ✅ Use Case 2: Extracting Media from Downloads  
**Problem:** A user wants to gather all music and video files from their messy Downloads folder.  
**Action:**  
- Select "Downloads" as source.  
- Select `.mp3`, `.mp4`, `.mkv`, `.avi` under "Media".  
- Choose "Music and Videos" folder as target.  
**Result:** Only selected media files are copied, no clutter.

---

### ✅ Use Case 3: Backing Up Scripts  
**Problem:** A developer wants to back up all script files across projects.  
**Action:**  
- Set "Projects" as source.  
- Select `.py`, `.js`, `.html`, `.css`, `.sh` under "Scripts".  
- Set an external drive folder as the target.  
**Result:** All scripts from various folders are now backed up in one place.

---

## 6. Disclaimer & Important Notices

- This repository and its contents may be updated at any time without notice.  
- Such updates may render parts of this README file obsolete.  
- No commitment is made to maintain or update the README to reflect future changes.  
- The provided code is delivered **"as-is"**, and no guarantees—explicit or implied—are made regarding functionality, reliability, compatibility, or correctness.
