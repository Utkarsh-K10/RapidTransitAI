import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
from tkinter import *
import os

names = []
def capture():
    cascPath = "/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    # log.basicConfig(filename='webcam.log',level=log.INFO)
    
    video_capture = cv2.VideoCapture(0)
    anterior = 0

    ws = Tk()
    ws.title("User Name")
    ws.geometry('400x300')
    ws['bg'] = '#ffbf00'

    def printValue():
        pname = player_name.get()
        names.append(pname)
        Label(ws, text=f'{pname}, Finding please Wait!', pady=20, bg='#ffbf00').pack() 


    player_name = Entry(ws)
    player_name.pack(pady=30)

    Button(ws,text="Enter Id", padx=10, pady=5,command=printValue).pack()

    ws.mainloop()
    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Capturing and Verifying..',(x,y),cv2.FONT_HERSHEY_SIMPLEX, 2, (2, 210,0), 1)
        if anterior != len(faces):
            anterior = len(faces)
            # log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

        for file in os.listdir('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/'):
            if file == '{}.jpg'.format(names[0]) or file =='.DS_Store':
                os.remove(file)

        # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('k'):
            check, frame = video_capture.read()
            cv2.putText(frame, 'RECOGNISING.. please wait',(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255,225), 1)
            cv2.imshow("Capturing", frame)
            fname = names[0]

            cv2.imwrite(filename='{}.jpg'.format(fname), img=frame)
            video_capture.release()
            img_new = cv2.imread('{}.jpg'.format(fname), cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            print("Image Saved")
            print("Program End")
            cv2.destroyAllWindows()
            break
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print("Turning off camera.")
            video_capture.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


# cam = cv2.VideoCapture(0)

# cv2.namedWindow("test")

# img_counter = 0


# def verif(img1path, img2path):
#     img1 = cv2.imread(img1path)
#     img2 = cv2.imread(img2path)
#     person = img2path.split('/')[-1]
#     result = DeepFace.verify(img1path, img2path)
#     verification = result[0]
#     if verification:
#         print('found')
#         cv2.PutText(img2, 'Found {}'.format(person))
#     else:
#         cv2.PutText(img2,'Unknown Person')
# while True:
#     ret, frame = cam.read()
#     if not ret:
#         print("failed to grab frame")
#         break
#     cv2.imshow("test", frame)

#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         # ESC pressed
#         print("Escape hit, closing...")
#         break
#     elif k%256 == 32:
#         # SPACE pressed
#         img_name = "opencv_frame_{}.png".format(img_counter)
#         cv2.imwrite(img_name, frame)
#         print("{} written!".format(img_name))
#         img_counter += 1
        # if saved_img in os.listdir('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/'):
        #     img1_path = os.path.join('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/',img_name)
        #     plt.imshow(cv2.imread(img1_path))
        #     plt.show()
        #     print('IMG1 PATH',img1_path)
        #     for file in os.listdir('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/database/'):
        #         img2_path = '/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/database/{}'.format(file)
        #         img2 = cv2.imread(img2_path)
        #         result = DeepFace.verify(img1_path, img2_path)
        #         print(result)
        #         verification = list(result.values())[0]
        #         if verification:
        #             print('found')
        #             plt.imshow(img2)
        #             plt.show()
        #             # cv2.putText(img2, 'Found {}'.format(img_name),(20,5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (67,67,67), 1)
        #         else:
        #             print("Please capture proper image")
        #             # cv2.putText(img2,'Unknown Person',(20,5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,67,227), 1)
        # else:
        #     print("Please capture proper image")
                

# cam.release()

# cv2.destroyAllWindows()

import cv2
from deepface import DeepFace
import os, json
import matplotlib.pyplot as plt
capture()
# n = input("Enter Your Name..")
# imgid = '{}.jpg'.format(n)
f = open('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/mappeddata.json')
imdata = json.load(f)
imgid = names[0]
print(imgid)
for i in imdata:
    if imgid in i['ID']:
        img2p = i['Image']
print(img2p)
fname = img2p.split('.')[0]
if imgid+'.jpg' in os.listdir('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/'):
    img1path = os.path.join('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/', '{}.jpg'.format(imgid))
    img2path = os.path.join('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/DataSet/{}'.format(img2p))

    print('Found')                
    fig = plt.figure()
    rows =1
    columns = 2
    img1 = cv2.imread(img1path)
    img2 = cv2.imread(img2path)
    name = img2path.split('/')[-1]
    fig.add_subplot(rows, columns, 1)
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Recognised Person :{}".format(fname))
    fig.add_subplot(rows, columns,2)
    plt.imshow(img1)
    plt.axis('off')
    plt.title('Original Person')
    plt.show()
else:
    fig = plt.figure()
    rows =1
    columns = 2
    uimgpath = '/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/unknown.jpg'
    img1path = os.path.join('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/', '{}.jpg'.format(imgid))
    img1 = cv2.imread(img1path)
    img2 = cv2.imread(uimgpath)
    name = 'Unknown'
    fig.add_subplot(rows, columns, 1)
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Recognised Person :{}".format(name))
    fig.add_subplot(rows, columns,2)
    plt.imshow(img1)
    plt.axis('off')
    plt.title('Original Person')
    plt.show()

    # db_path = '/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/database'
    # for file in os.listdir(db_path):
    #     if file.split('.')[-1] != 'jpg' or file=='.DS_Store':
    #         pass
    #     else:
    #         img2path = os.path.join(db_path,file)
    #         fname = file.split('_')[0]
    #         fname = fname.lower()
    #         print(fname)
    #         result = DeepFace.verify(img1path,img2path)
    #         verification = list(result.values())[0]

    # #         if verification == True and fname == imgid:
    #             print('Found', result)                
    #             fig = plt.figure()
    #             rows =1
    #             columns = 2
    #             img1 = cv2.imread(img1path)
    #             img2 = cv2.imread(img2path)
    #             name = img2path.split('/')[-1]
    #             fig.add_subplot(rows, columns, 1)
    #             plt.imshow(img2)
    #             plt.axis('off')
    #             plt.title("Recognised Person :{}".format(fname))
    #             fig.add_subplot(rows, columns,2)
    #             plt.imshow(img1)
    #             plt.axis('off')
    #             plt.title('Original Person')
    #             plt.show()
    #         elif verification == False and fname != imgid:
    #             print("Unknown")
                # fig = plt.figure()
                # rows =1
                # columns = 2
                # uimgpath = '/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/unknown.jpg'
                # img1 = cv2.imread(img1path)
                # img2 = cv2.imread(uimgpath)
                # name = 'Unknown'
                # fig.add_subplot(rows, columns, 1)
                # plt.imshow(img2)
                # plt.axis('off')
                # plt.title("Recognised Person :{}".format(name))
                # fig.add_subplot(rows, columns,2)
                # plt.imshow(img1)
                # plt.axis('off')
                # plt.title('Original Person')
                # plt.show()
                # img3 = cv2.imread('/Users/utkarshkushwaha/Downloads/ITDEPT/testproject/unknown.jpg')
                # plt.imshow(img3)
                # plt.show