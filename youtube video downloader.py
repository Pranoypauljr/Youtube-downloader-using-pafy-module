import pafy as pf
url="https://www.youtube.com/watch?v=uV0F8LcU120&t=2s"
video=pf.new(url)
streams=video.streams
for i in streams:
    print(i)
best=video.getbest()
print(best.resolution,best.extension)
best.download()
print("success")

