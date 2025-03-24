import tkinter as tk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL

def download_video():
    url = url_entry.get()
    if not url.strip():
        messagebox.showwarning("Warning", "Please enter a YouTube URL!")
        return

    path = filedialog.askdirectory()
    if not path:
        messagebox.showwarning("Warning", "No directory selected!")
        return

    try:
        # yt-dlp options
        ydl_opts = {
            'format': 'best',  # Download the best quality
            'outtmpl': f'{path}/%(title)s.%(ext)s',  # Save with the video title
        }

        # Download the video
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main GUI window
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x200")
root.resizable(False, False)

# URL Label and Entry
url_label = tk.Label(root, text="Enter YouTube URL:", font=("Arial", 12))
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50, font=("Arial", 10))
url_entry.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download Video", font=("Arial", 12), bg="blue", fg="white", command=download_video)
download_button.pack(pady=20)

# Run the application
root.mainloop()
