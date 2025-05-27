# 🗂️ Photo Mover

A **Python-based file management tool** with a **Tkinter-powered GUI** for organizing your media files efficiently. Executable file located in `dist` folder.

## 📦 Overview

**Photo Mover** scans a user-specified directory for photo and video files (e.g., `.jpg`, `.png`, `.mp4`) and automatically sorts them into newly created folders by **year and month**, using metadata extracted from the files.
The application also features a **duplicate detection mechanism** based on file **creation date** and **size**, ensuring that no redundant files are copied during the move.

## 🧰 Features

* Built with **Python** and **Tkinter** for a lightweight GUI
* Scans and organizes files into structured folders (e.g., `/2025/05 May`)
* Supports common photo/video formats: `.jpg`, `.jpeg`, `.png`, `.mp4` and `.mov`.
* Detects and skips duplicate files using metadata (creation date) and file size

## 🚀 How to Use

1. **Select Source Folder**
   Choose the directory that contains your photos and videos.

2. **Select Destination Folder**
   Pick the folder where you want the sorted media to be stored.

3. **Click "Move"**
   The tool will scan, sort, and move files into new folders organized by creation date.

## 📁 Folder Structure

```plaintext
destination/
  └── 2023/
        └── 05 May/
              ├── photo1.jpg
              ├── video1.mp4
  └── 2024/
        └── 01 January/
              └── photo2.png
```

## 💻 Tech Stack

* **Language**: Python
* **GUI Library**: Tkinter
* **Metadata Handling**: `os`, `datetime`, `shutil`, `platform`, `re`

