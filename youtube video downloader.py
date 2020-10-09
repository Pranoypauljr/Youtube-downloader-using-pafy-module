from tkinter import *
import pafy as pf
app=Tk()
app.title("youtube downloader")
app.geometry("300x200")
app.iconbitmap("yt.ico")
Label(app,text="Paste the youtube link",font="Arial").pack()
def api():
    f=e.get()
    url=f
    video=pf.new(url)
    streams=video.streams
    for i in streams:
        print(i)
    best=video.getbest()
    print(best.resolution,best.extension)
    best.download()
    print("success")       
e=Entry(app,width=50)
e.pack()
photo=PhotoImage("yt.jpg")
Button(app,text="Download",command=lambda:api()).pack()
app.mainloop()
