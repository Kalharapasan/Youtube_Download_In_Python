import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from yt_dlp import YoutubeDL
import threading

def update_progress(percent):
    progress_bar["value"] = percent
    progress_label.config(text=f"Progress: {percent:.2f}%")
    root.update_idletasks()

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please enter a YouTube URL or playlist!")
        return
    
    path = filedialog.askdirectory()
    if not path:
        messagebox.showwarning("Warning", "No directory selected!")
        return
    
    download_button.config(state=tk.DISABLED)
    
    def download_task():
        try:
            # Setup options for downloading
            ydl_opts = {
                'format': 'best[height<=1080]/best',  # Best quality up to 1080p, fallback to best available
                'outtmpl': f'{path}/%(playlist_title)s/%(title)s.%(ext)s',  # Save in playlist folder
                'progress_hooks': [progress_hook],  # Attach progress hook
                'noplaylist': False,  # Enable playlist downloads
                'geo_bypass': True,  # Bypass geo-restrictions
                'writethumbnail': True,  # Download thumbnail image
                'writeinfojson': False,  # Don't write info json
                'ignoreerrors': True,  # Continue on download errors
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                # Download the video with the specified format
                ydl.download([url])
            
            messagebox.showinfo("Success", "Download completed successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            download_button.config(state=tk.NORMAL)
            update_progress(0)
    
    threading.Thread(target=download_task, daemon=True).start()

def progress_hook(d):
    if d['status'] == 'downloading':
        # Handle cases where total_bytes might be None
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        downloaded_bytes = d.get('downloaded_bytes', 0)
        
        if total_bytes > 0:
            percent = (downloaded_bytes / total_bytes) * 100
            update_progress(percent)
        else:
            # If we don't have total bytes, show indeterminate progress
            progress_label.config(text="Downloading...")
            
    elif d['status'] == 'finished':
        update_progress(100)

# GUI Setup
root = tk.Tk()
root.title("YouTube Downloader with Progress Bar")
root.geometry("500x300")
root.resizable(False, False)

# URL Label and Entry
url_label = tk.Label(root, text="Enter YouTube URL or Playlist URL:", font=("Arial", 12))
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=60, font=("Arial", 10))
url_entry.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download", font=("Arial", 12), bg="blue", fg="white", command=download_video)
download_button.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

progress_label = tk.Label(root, text="Progress: 0%", font=("Arial", 10))
progress_label.pack()

# Run the Application
root.mainloop()
