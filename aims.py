"""this code aim to present my first ever real time  eyeglass detection system to the entire AIMS network
  I don't know the out-come but i will do it

Author: Nken ALLASSAN
Project title: EYE GLASS DETECTION SYSTEM"""
"Date: 15/02/2021"

import cv2
# now i create a new cam object
cap=cv2.VideoCapture(0)
print("well imported......")
#we will start by trying the eyeglass HaarCascade classifier
"initializing the face classifier"
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    #read the image from the cam
    _,image=cap.read()
    #now i convert the image into grayscale
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #detect all faces in the image
    faces=face.detectMultiScale(image_gray,1.3,5)
    #for every face draw a rectangle
    for x,y, width,height in faces:
        cv2.rectangle(image,(x,y),(x+width,y+height),color=(255,0,0),thickness=1)
        #cv2.putText(image,'Face',(10,500),font,1,(0,0,255),2)
    cv2.imshow('Stark',image)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()






#url='http://10.123.50.24:8080/shot.jpg'
#while True:
    #grab the frame and resize it to have a frame width of 400
    #frame=vs.read()
#    imageRes=urllib.request.urlopen(url)
#    imageNp=np.array(bytearray(imageRes.read()),dtype=np.uint8)
#    img=cv2.imdecode(imageNp,-1)
#    frame=imutils.resize(img,width=400)
#    (h,w)=frame.shape[:2]
