from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window
from yt_dlp import YoutubeDL
import threading


class Downloader(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Set Window size for testing (ignored on mobile)
        Window.size = (360, 640)

        # Add a Label for the URL
        self.add_widget(Label(text="Enter YouTube URL or Playlist URL:", font_size="16sp", size_hint=(1, 0.1)))

        # TextInput for the URL
        self.url_input = TextInput(hint_text="Paste YouTube URL here", multiline=False, size_hint=(1, 0.1))
        self.add_widget(self.url_input)

        # Download Button
        self.download_button = Button(text="Download", size_hint=(1, 0.1), background_color=(0.2, 0.6, 1, 1))
        self.download_button.bind(on_press=self.start_download)
        self.add_widget(self.download_button)

        # ProgressBar for the download
        self.progress = ProgressBar(max=100, size_hint=(1, 0.1))
        self.add_widget(self.progress)

        # Status Label
        self.status_label = Label(text="Progress: 0%", font_size="14sp", size_hint=(1, 0.1))
        self.add_widget(self.status_label)

    def update_progress(self, percent):
        self.progress.value = percent
        self.status_label.text = f"Progress: {percent:.2f}%"

    def download_task(self, url):
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': '/sdcard/Download/%(playlist_title)s/%(title)s.%(ext)s',
                'progress_hooks': [self.progress_hook],
                'noplaylist': False,  # Enable playlist downloads
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.update_progress(100)
            self.status_label.text = "Download Completed!"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"
        finally:
            self.download_button.disabled = False

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = (d.get('downloaded_bytes', 0) / d.get('total_bytes', 1)) * 100
            Clock.schedule_once(lambda dt: self.update_progress(percent))
        elif d['status'] == 'finished':
            Clock.schedule_once(lambda dt: self.update_progress(100))

    def start_download(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.status_label.text = "Please enter a valid URL!"
            return

        self.download_button.disabled = True
        self.status_label.text = "Downloading..."
        threading.Thread(target=self.download_task, args=(url,), daemon=True).start()


class YouTubeDownloaderApp(App):
    def build(self):
        return Downloader()


if __name__ == "__main__":
    YouTubeDownloaderApp().run()
