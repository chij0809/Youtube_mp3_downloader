import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from pathlib import Path

YTDLP_PATH = r"C:\Users\Jacky\AppData\Local\Programs\Python\Python313\Scripts\yt-dlp.exe"
FFMPEG_PATH = r"D:\ffmpeg\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"

def download_video_or_audio():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("提示", "請輸入 YouTube 網址")
        return

    save_path = filedialog.askdirectory(title="選擇要下載的資料夾")
    if not save_path:
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
            return

        subprocess.run(command, check=True)
        messagebox.showinfo("成功", f"{format_var.get().upper()} 下載完成！")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("錯誤", f"下載失敗：\n{e}")
    except Exception as e:
        messagebox.showerror("錯誤", f"發生錯誤：{e}")

# GUI
app = tk.Tk()
app.title("YouTube 下載器")
app.geometry("400x250")

tk.Label(app, text="請貼上 YouTube 網址：").pack(pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

format_var = tk.StringVar(value="mp3")
tk.Label(app, text="選擇下載格式：").pack(pady=5)
tk.Radiobutton(app, text="MP3", variable=format_var, value="mp3").pack()
tk.Radiobutton(app, text="MP4", variable=format_var, value="mp4").pack()

resolution_var = tk.StringVar(value="720")
tk.Label(app, text="選擇解析度（僅 MP4 有效）：").pack(pady=5)
resolution_menu = tk.OptionMenu(app, resolution_var, "144", "240", "360", "480", "720", "1080")
resolution_menu.pack()

tk.Button(app, text="下載", command=download_video_or_audio).pack(pady=20)

app.mainloop()

