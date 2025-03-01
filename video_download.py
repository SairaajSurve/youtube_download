from pytubefix import YouTube
from pytubefix.cli import on_progress

url = ""
output_path = ""

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
# ys = yt.streams.get_highest_resolution()
ys.download(output_path=output_path)