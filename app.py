from tkinter import *
import speedtest
print("calculating! pls wait....")
root = Tk()
root.title("Speedtest_GUI")
root.geometry("300x100")
root.resizable(0, 0)
root.iconbitmap(r"speedtest.ico")
root.config(bg="Blue")
s = speedtest.Speedtest()
up = s.upload() * 0.000001
down = s.download() * 0.000001
txt1 = Label(root, text="download speed", bg="orange")
txt1.pack()
res1 = Label(root, text=f"{down} mbps", bg="White")
res1.pack()
txt2 = Label(root, text="upload speed", bg="green")
txt2.pack()
res2 = Label(root, text=f"{up} mbps", bg="White")
res2.pack()
root.mainloop()
