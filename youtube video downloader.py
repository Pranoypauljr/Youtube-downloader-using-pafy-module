import pafy as pf
url="<url of youtube video is to be added here>"
video=pf.new(url)
streams=video.streams
for i in streams:
    print(i)
best=video.getbest()
print(best.resolution,best.extension)
best.download()
print("success")

