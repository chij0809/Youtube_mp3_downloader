import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
from pathlib import Path
import threading
import os

print(os.getcwd())  # 顯示當前工作目錄

YTDLP_PATH = r"C:\Users\Jacky\AppData\Local\Programs\Python\Python313\Scripts\yt-dlp.exe"
FFMPEG_PATH = r"D:\ffmpeg\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"

def start_download():
    threading.Thread(target=download_video_or_audio).start()

def download_video_or_audio():
    progress.start()
    url = url_entry.get()
    if not url:
        messagebox.showwarning("提示", "請輸入 YouTube 網址")
        progress.stop()
        return

    save_path = filedialog.askdirectory(title="選擇要下載的資料夾")
    if not save_path:
        progress.stop()
        return

    save_path = Path(save_path)
    output_template = str(save_path / "%(title)s.%(ext)s")

    try:
        if format_var.get() == "mp3":
            command = [
                YTDLP_PATH,
                "--ffmpeg-location", FFMPEG_PATH,
                "-f", "bestaudio",
                "--extract-audio",
                "--audio-format", "mp3",
                "-o", output_template,
                url
            ]
        elif format_var.get() == "mp4":
            resolution = resolution_var.get()
            video_format = f"bestvideo[height<={resolution}]+bestaudio"
            command = [
                YTDLP_PATH,
                "--ffmpeg-location", FFMPEG_PATH,
                "-f", video_format,
                "--merge-output-format", "mp4",
                "-o", output_template,
                url
            ]
        else:
            messagebox.showerror("錯誤", "請選擇下載格式")
            progress.stop()
            return

        subprocess.run(command, check=True)
        messagebox.showinfo("成功", f"{format_var.get().upper()} 下載完成！")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("錯誤", f"下載失敗：\n{e}")
    except Exception as e:
        messagebox.showerror("錯誤", f"發生錯誤：{e}")
    finally:
        progress.stop()

# GUI 介面
app = tk.Tk()
app.title("YouTube 影片/音樂下載器")
app.geometry("500x500")

# 加載背景圖片
background_image = Image.open("background.jpg")  # 確認 background.jpg 放在正確位置
background_image = background_image.resize((500, 500), Image.Resampling.LANCZOS)  # ← 新版 Pillow 正確寫法
bg_photo = ImageTk.PhotoImage(background_image)

# 使用 Canvas 顯示背景
canvas = tk.Canvas(app, width=500, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# 在 Canvas 上放其他元件
canvas.create_text(250, 30, text="YouTube 影片/音樂下載器", fill="white", font=("Arial", 16, "bold"))

url_label = tk.Label(app, text="請貼上 YouTube 網址：", bg="#000000", fg="white")
url_entry = tk.Entry(app, width=50)
canvas.create_window(250, 70, window=url_label)
canvas.create_window(250, 100, window=url_entry)

format_var = tk.StringVar(value="mp3")
format_label = tk.Label(app, text="選擇下載格式：", bg="#000000", fg="white")
canvas.create_window(250, 140, window=format_label)

mp3_button = tk.Radiobutton(app, text="MP3", variable=format_var, value="mp3", bg="#000000", fg="white")
mp4_button = tk.Radiobutton(app, text="MP4", variable=format_var, value="mp4", bg="#000000", fg="white")
canvas.create_window(200, 170, window=mp3_button)
canvas.create_window(300, 170, window=mp4_button)

resolution_var = tk.StringVar(value="720")
resolution_label = tk.Label(app, text="選擇解析度（僅 MP4 有效）：", bg="#000000", fg="white")
resolution_menu = ttk.Combobox(app, textvariable=resolution_var, values=["144", "240", "360", "480", "720", "1080"])
canvas.create_window(250, 210, window=resolution_label)
canvas.create_window(250, 240, window=resolution_menu)

progress = ttk.Progressbar(app, orient="horizontal", length=300, mode="indeterminate")
canvas.create_window(250, 280, window=progress)

download_button = tk.Button(app, text="下載", command=start_download, bg="#4CAF50", fg="white")
canvas.create_window(250, 320, window=download_button)

app.mainloop()

