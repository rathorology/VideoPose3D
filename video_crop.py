import cv2

vid_path = "/home/rathorology/PycharmProjects/VideoPose3D/input_directory/1.mp4"
cap = cv2.VideoCapture(vid_path)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) / 2)
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(5))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

final_out = cv2.VideoWriter("/home/rathorology/PycharmProjects/VideoPose3D/input_directory/2.mp4", fourcc, fps,
                            (frame_width, frame_height))
while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = frame[:, int(frame.shape[1] / 2):]
    final_out.write(frame)
