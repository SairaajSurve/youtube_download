from moviepy.editor import *
import os

mp4s = os.listdir('videos/')

for mp4 in mp4s:
    print('Converting: ' + mp4)
    video = VideoFileClip('videos/'+mp4)
    video.audio.write_audiofile('audios/'+mp4[:-1]+'3')

