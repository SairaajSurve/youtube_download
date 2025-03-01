from pytubefix import Playlist
from pytubefix.cli import on_progress

url = ""
output_path = ""

pl = Playlist(url)
for video in pl.videos:
    ys = video.streams.get_audio_only()
    # ys = video.streams.get_highest_resolution()
    ys.download(output_path=output_path)
