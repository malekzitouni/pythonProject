import cv2
#access and retrieve video streams from a camera or a video source.
cap=cv2.VideoCapture(0)
output_file='output.mp4'
fourcc=cv2.VideoWriter_fourcc(*'XVID')
fp=20
frame_size=(50,20)
video_writer=cv2.VideoWriter(output_file,fourcc,fp,frame_size)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret:
     print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
     print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
     video_writer.write(frame)
     cv2.imshow('video',frame)

     if cv2.waitKey(1) == ord('q'):
        break
    else:
       break   

cap.release()
cv2.destroyAllWindows()
