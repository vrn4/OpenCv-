import cv2
from tkinter import Tk,Label,Button,filedialog
import os

def nothing(x):
    pass

def crop(imgpath):
    fname = "Cropped_"+os.path.basename(imgpath)
    dirfname = os.path.join(os.path.dirname(imgpath),fname)   
    img = cv2.imread(imgpath)
    cv2.namedWindow("Crop Settings")
    cv2.resizeWindow("Crop Settings",500,200)
    cv2.createTrackbar("Left","Crop Settings",0,600,nothing)
    cv2.createTrackbar("Right","Crop Settings",600,600,nothing)
    cv2.createTrackbar("Top","Crop Settings",0,500,nothing)
    cv2.createTrackbar("Bottom","Crop Settings",500,500,nothing)
    while True:
        img = cv2.resize(img,(600,500))
        left = cv2.getTrackbarPos("Left","Crop Settings")
        right = cv2.getTrackbarPos("Right","Crop Settings")
        top = cv2.getTrackbarPos("Top","Crop Settings")
        bottom = cv2.getTrackbarPos("Bottom","Crop Settings")
        tempimg = img[top:bottom,left:right]
        tempimg = cv2.resize(tempimg,(600,500))
        cv2.imshow("Image",tempimg)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        elif cv2.waitKey(1) & 0xFF == ord("s"):
            cv2.imwrite(dirfname,tempimg)
            break
    cv2.destroyAllWindows()
    first()

def fileopen():
    path = filedialog.askopenfile(title="Select an Image",filetypes=(("PNG Files(.png)","*.png"),("JPEG Files(.jpg)","*.jpg")))
    try:
        root.destroy()
        crop(path.name)
    except:
        first()

def first():    
    global root
    root = Tk()
    root.geometry("500x300")
    root.title("File Selection")
    root.configure(bg="white")
    Button(root,text="Browse",font="Corier 20",command=fileopen).pack(pady=20)
    Label(root,text="Press s to save a file",bg="white",font="Corier 20").pack(pady=20)
    Label(root,text="Press q to quit",bg="white",font="Corier 20").pack(pady=20)
    root.mainloop()

first()
