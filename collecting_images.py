
import cv2
import sys
import os


try:
    label_name = sys.argv[1]
    samples = sys.argv[2]
except:
    print("Arguments missing")



j= 501

data_path = os.path.join(os.getcwd(),'Train')
image_class_path = os.path.join(data_path , label_name)

try:
    os.mkdir(data_path)
except :
    print("{} directory already exist".format(data_path))



try:
    os.mkdir(image_class_path)
except:
    print("{} directory already exist".format(image_class_path))

cap = cv2.VideoCapture(0)

def make_720():
    cap.set(3,1366)
    cap.set(4, 720)

make_720()
count = 1



while True:

    ret ,frame = cap.read()

    if not ret:
        continue

    font = cv2.FONT_HERSHEY_SIMPLEX


    cv2.putText(frame , "Enter the data for {}".format(label_name) , (150 ,50) , font , 1, (0,0,255) ,2 , cv2.LINE_AA )
    cv2.rectangle(frame , (100,100) , (500,500) , (255,255,255) ,2)



    # roi
    i=0
    if count<= int(samples):
        roi = frame[100:500 ,100:500]
        save_path = os.path.join(image_class_path ,"{} {}.jpg".format(label_name , count))
        
        if i%29 ==0:
            cv2.imwrite(save_path , roi)
            count +=1
            

    else:
        break

    cv2.putText(frame , "Collected {}".format(count) , (150 , 600)  , font , 1, (255,150,0) ,2 , cv2.LINE_AA )



    cv2.imshow("rock-ppr-scissors" , frame)

    pressed_key = cv2.waitKey(1) & 0xFF
    if pressed_key == ord('s'):
        break


print("{} samples saved to {}".format(samples, image_class_path))
cap.release()
cv2.destroyAllWindows()






