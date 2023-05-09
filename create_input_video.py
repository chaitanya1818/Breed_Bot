import cv2
from glob import glob


video_name = "video2.avi"


dog_names = [item[0:-9] for item in sorted(glob("input_images/*"))]

files = [item for item in sorted(glob("input_images/*"))]

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc('M','J','P','G'), 0.5, (224,224))
for file in files:
    image = cv2.imread(file)
    image = cv2.resize(image, (224,224))
    #cv2.putText(image, file[12:-10], (5, 200),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255, 0, 0),2)
    cv2.waitKey(2)
    video.write(image)
    

cv2.destroyAllWindows()
video.release()