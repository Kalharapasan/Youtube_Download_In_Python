# 🎬 YouTube Downloader with GUI (yt-dlp + tkinter)

This is a simple yet powerful desktop application built in Python that allows users to download YouTube videos or playlists using a graphical interface. It leverages the power of [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) for video downloading and `tkinter` for the GUI.

---

## 📌 Features

- ✅ Download individual videos or entire playlists
- 🎥 Supports up to 1080p quality (automatically selects best available)
- 📁 Organizes videos into folders by playlist title
- 🖼 Downloads thumbnails
- 📊 Real-time progress bar updates
- 🖱 User-friendly interface with folder selection

---

## 🧰 Requirements

Make sure you have the following installed:

- Python 3.7+
- Python modules:
  - `yt-dlp`
  - `tkinter` (included by default in most Python installations)

### 📦 Install dependencies

Open your terminal/command prompt and run:

```bash
pip install yt-dlp

📸 Screenshots

![image](https://github.com/user-attachments/assets/268b835f-b19f-4695-8876-ad310555d71b)


🚀 How to Use
Download or clone this repository.

Open the terminal in the project directory.

Run the script:
python App.py
A GUI window will appear.

Paste your YouTube video or playlist URL.

Click Download.

Choose a folder where you want to save the downloaded video(s).

The progress bar will show real-time download progress.

When finished, a success message will appear.

❓ Troubleshooting
Error: ModuleNotFoundError: No module named 'yt_dlp'
👉 Run pip install yt-dlp in your terminal.

No download starts / stuck
👉 Make sure the link is correct and the video is available.

Permission Error when choosing a folder
👉 Select a folder where you have write access.

💡 Future Improvements (Optional Ideas)
Add download format options (MP4, MP3)

Let user choose resolution (480p, 720p, 1080p)

Show estimated download time

Support download from other platforms (yt-dlp supports many)

📝 License
This project is open-source and free to use.
