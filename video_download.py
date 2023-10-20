import pytube


link = input('Video Link: ')
video = pytube.YouTube(link)


cur_dir = 'videos'

print('downloading : {} with url : {}'.format(video.title, video.watch_url))
video.streams.\
  filter(type='video', progressive=True, file_extension='mp4').\
  order_by('resolution').\
  desc().\
  first().\
  download(cur_dir)
