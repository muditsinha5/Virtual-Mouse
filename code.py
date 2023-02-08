import cv2
import mediapipe as mp
import pyautogui
#opening the video camera and reading the image

cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width,screen_height=pyautogui.size()
index_y=0
index_x=0

while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1) #flipping the video and removing mirror image flipping it on y axis
    frame_height,frame_width,_=frame.shape
    rgbframe=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgbframe)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)


                #commands for index finger

                if id==8:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    index_x=screen_width/frame_width*x
                    index_y=screen_width/screen_height*y
                    pyautogui.moveTo(index_x,index_y)

                  #commands for thumb
                if id==4:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    thumb_x=screen_width/frame_width*x
                    thumb_y=screen_width/screen_height*y
                    if abs(index_x-thumb_x)<9:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print('click operation done')



    cv2.imshow("Virtual Mouse",frame)
    cv2.waitKey(1)

