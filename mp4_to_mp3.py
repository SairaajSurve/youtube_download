from moviepy.editor import *

mp4 = input('Enter file name: ') + '.mp4'

print('Converting: ' + mp4)
video = VideoFileClip('videos/'+mp4)
video.audio.write_audiofile('audios/'+mp4[:-1]+'3')
