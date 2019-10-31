import cv2
import datetime
import time
from tkinter import *
from PIL import Image, ImageDraw, ImageTk


width, height = 800, 600
cap = cv2.VideoCapture(0)
time.sleep(1) # delay for camera initialisation
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

#Set up GUI
window = Tk()
window.wm_title("Video Motion Detector")
window.bind('<Escape>', lambda e: window.quit())


lbl = Label(window, text="WELCOME TO SECURITY SYSTEM (esc to quit)", font=("Arial Bold", 16))
lbl.grid(column=0, row=0)

lmain = Label(window)
lmain.grid(row=1, column=0, padx=24, pady=24)

v2 = Label(window)
v2.grid(row=1, column=1, padx=24, pady=24, sticky='n')

first_frame=None

def show_frame():
    check, frame = cap.read() # capture video frame

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # make frame gray
    gray = cv2.GaussianBlur(gray,(21,21),0) # make frame blur

    global first_frame
    if first_frame is None: #taking initial frame
        first_frame=gray

    delta_frame = cv2.absdiff(first_frame,gray) # calculating diff of each pixel (if no difference it shold be =0)

    thresh_delta = cv2.threshold(delta_frame,32,255, cv2.THRESH_BINARY)[1] # convert in Black and White by theshold (more then 32 made white pixel else black)

    thresh_frame = cv2.dilate(thresh_delta, None, iterations=2) # smooth contours of BW areas

    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # find all countours

    for contour in cnts[::5]:  # use every 5th set from cnts countours (to reduce number of taken pictures)
        if cv2.contourArea(contour) < 10000: # if area less then 10000 px (100x100 px) do nothing else start save frames
            continue

        (x, y, w, h) = cv2.boundingRect(contour)  # take rectangle coordinates
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2) # draw green rectangle, this two lines can bee deleted

        img123 = Image.fromarray(frame) #convert array representation of image for Pillow

        img123.thumbnail((560, 560)) # resize for side not bigger then 560 saving proportions
        now = datetime.datetime.today()
        timetext = str(now.strftime("%Y-%m-%d-%H.%M.%S.%f")) # take date
        img = ImageDraw.Draw(img123)
        img.text((12, 12), timetext) # two lines to add date to image - 12px from corner
        img123.save(timetext + "pil-basic-example.jpg") #save pic to current dir
        img123 = ImageTk.PhotoImage(image=img123)
        v2.img123 = img123
        v2.configure(image=img123)


    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img_vid = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img_vid)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(50, show_frame) # repeat every 50 milli seconds 

b1 = Button(window, text="start!", width=16, command=lambda:[show_frame()])
b1.grid(row=3,column=1, padx=6, pady=6)
window.mainloop()  #needed to run GUI