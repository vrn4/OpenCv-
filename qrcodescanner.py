import cv2
from pyzbar.pyzbar import decode
import webbrowser
from tkinter import Tk,Label,Button

def retake_func():
    root.destroy()
    video_func()

def browser_func():
    webbrowser.open(link_address)
    root.destroy()
    video_func()

def gui_func():
    global root
    root = Tk()
    root.geometry("400x300")
    root.title("QRCodeReader")
    root.configure(bg="White")
    Label(root,text=link_address,width=50,bg="White").pack(pady=20)
    Button(root,text="Open in Browser",width=50,fg="Red",command=browser_func).pack(pady=20)
    Button(root,text="Retake",width=50,fg="Red",command=retake_func).pack(pady=20)    
    root.mainloop()

def video_func():
    vid = cv2.VideoCapture(0)
    vid.set(3,600)
    vid.set(4,400)
    flag = 0
    while True:
        if flag == 1:
            break
        else:
            success,img = vid.read()
            for code in decode(img):
                if code.data.decode("utf-8") != None:
                    global link_address
                    link_address = code.data.decode("utf-8")
                    flag = 1
            cv2.imshow("QRCodeReader",img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    vid.release()
    gui_func()

video_func()