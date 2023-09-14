#install pytube package - pip3 install PYTUBE
from pytube import YouTube
from sys import argv

print("Let's Download youtube videos!")
link = argv[1]
ytube = YouTube(link)
print("Title: ",ytube.title)
print("Views: ",ytube.views)
ytubeD = ytube.streams.get_highest_resolution()
ytubeD.download('/ytubedownload');