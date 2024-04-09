import cv2

# Video normal
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter('video_tarea.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20,
                         (width, height))

while True:
    ret, frame = cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    writer.write(frame)
    cv2.imshow('frame', frame)

cap.release()
writer.release()
cv2.destroyAllWindows()

# Video reversa
cap = cv2.VideoCapture("video_tarea.mp4")
check, vid = cap.read()
frame_list = []

while(check==True):
    check,vid = cap.read()
    frame_list.append(vid)
frame_list.pop()
frame_list.reverse()


writer_reverse = cv2.VideoWriter('video_tareareverse.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20,
                                 (width, height))

for frame in frame_list:
    cv2.imshow("Frame", frame)
    writer_reverse.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer_reverse.release()
cv2.destroyAllWindows()

cap_normal = cv2.VideoCapture("video_tarea.mp4")
cap_reverse = cv2.VideoCapture("video_tareareverse.mp4")

joined_writer = cv2.VideoWriter('video_combinado.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))

while True:
    ret_normal, frame_normal = cap_normal.read()
    if not ret_normal:
        break
    joined_writer.write(frame_normal)

while True:
    ret_reverse, frame_reverse = cap_reverse.read()
    if not ret_reverse:
        break
    joined_writer.write(frame_reverse)
    
cap_normal.release()
cap_reverse.release()
joined_writer.release()
cv2.destroyAllWindows()



