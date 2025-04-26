# YouTube MP3/MP4 Downloader 🎵

A simple and intuitive YouTube audio/video downloader built with Python, Tkinter, and yt-dlp.  
Supports MP3 audio and MP4 video downloads with resolution selection and custom save paths.  
Perfect for personal use or educational demonstration.

---

## ⚙️ Requirements

This program requires [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [ffmpeg](https://ffmpeg.org/) to handle media downloading and conversion.

### 📦 How to Install FFmpeg (Windows Users)

Download the Windows build from the official website:

👉 [FFmpeg Windows Essentials Build](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)

Then:

1. Extract the zip file.
2. Copy the full path of the `bin` folder (where `ffmpeg.exe` is located) and add it to your **system environment variable `Path`**.
3. Alternatively, set the full path in the script's `FFMPEG_PATH` variable (works even without editing system variables).

> ⚠️ Without ffmpeg, MP4 downloads will not merge audio and video correctly.

---

## 🔍 Auto-Detection of FFmpeg at Runtime

When the user selects MP4 format, the system will automatically check whether `ffmpeg` is available:

- If not found, a warning will be shown and the process will stop.
- You can solve this by either installing ffmpeg and setting environment variables, or hardcoding the path in the script.

---

## 📦 Built With

- Python 3.11
- Tkinter GUI
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- `subprocess` to call yt-dlp
- `pathlib` to manage file paths and filenames

---

## 🌟 Features

- ✅ MP3 audio download support
- ✅ MP4 video download with resolution options
- ✅ Custom output folder and filename
- ✅ Simple GUI interface (no terminal needed)
- ✅ **Playlist download support** (downloads all videos in a playlist)

---

## 🚀 How to Use

1. Install required Python packages:
   ```bash
   pip install yt-dlp
   ```
2. Run the main script:
   ```bash
   python yt_mp3_downloader.py
   ```
3. Follow the steps in the GUI:
   - Paste a YouTube URL  
   - Select download format (MP3 or MP4)
   - If MP4, choose desired resolution (e.g., 720p)
   - Click Download to begin

🖼️ Interface Preview  
Main GUI (YouTube Downloader):  
![screenshot](screenshot.png)

---

## 🎬 Demo Video

A full walkthrough demonstrating how to use the YouTube MP3/MP4 downloader, including Git version control and ffmpeg setup:

👉 [Watch on YouTube](https://youtu.be/Pww479_sxQk)

---

📄 License  
This project is licensed under the MIT License.  
You are free to use, modify, and share for personal or educational purposes. Commercial piracy is strictly prohibited.
