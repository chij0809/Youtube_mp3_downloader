# YouTube MP3/MP4 Downloader 🎵

一個使用 Python、Tkinter 與 yt-dlp 製作的 YouTube 音訊/影片下載器。  
支援 MP3 音訊與 MP4 影片下載，可選擇解析度與儲存路徑，簡單直覺，適合自用與教學示範。

---
## ⚙️ 前置需求

本程式需要使用 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 與 [ffmpeg](https://ffmpeg.org/) 來下載與轉檔影音。

### 📦 如何安裝 ffmpeg（Windows 使用者）

請前往下列官方網站下載 Windows 可執行版：

👉 [FFmpeg Windows 版本（Essentials Build）](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)

下載後請：

1. 解壓縮 zip 檔案
2. 將 `bin` 資料夾的完整路徑（裡面包含 `ffmpeg.exe`）加入系統環境變數 Path
3. 或者，將該路徑填入程式內的 `FFMPEG_PATH` 欄位（不改環境變數也能執行）

> 若未正確安裝 ffmpeg，將無法將 MP4 的音訊與影像合併

---

## 🔍 執行時會自動檢查 ffmpeg 是否存在

若使用者選擇 MP4 格式下載，系統會自動檢查 ffmpeg 是否存在：

- 若未找到 ffmpeg，將顯示錯誤提示並中止下載
- 使用者可透過環境變數或程式內硬編路徑處理


## 📦 使用技術

- Python 3.x
- Tkinter GUI
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- subprocess 模組呼叫 yt-dlp
- pathlib 處理儲存路徑與輸出檔名

---

## 🌟 功能特色

- ✅ 支援 MP3 音訊下載
- ✅ 支援 MP4 影片下載（解析度可選）
- ✅ 自訂儲存資料夾與檔名格式
- ✅ 簡易 GUI 操作介面（不需終端機）

---

## 🚀 如何使用

1. 安裝 Python 套件（建議使用 virtualenv）：
   ```bash
   pip install yt-dlp
2. 執行主程式：
   ```bash
   python yt_mp3_downloader.py
3. 操作流程：
   - 貼上 YouTube 網址
   - 選擇下載格式（MP3 或 MP4）
   - 若為 MP4 可選解析度（如 720p）
   - 點擊「下載」開始執行

## 🖼️ 畫面預覽

> 主程式介面（YouTube 下載器 GUI）：

![screenshot](screenshot.png)


📄 License
本專案採用 MIT 授權條款。
可自由使用、修改與分享，僅供學習與個人用途，請勿用於商業盜版用途。
