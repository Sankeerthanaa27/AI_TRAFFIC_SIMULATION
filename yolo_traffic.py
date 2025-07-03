import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

vehicle_classes = ['car', 'motorcycle', 'bus', 'truck']

def runYolo(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("[ERROR] Unable to open video.")
        return

    print("[INFO] Running YOLO Traffic Detection...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        labels = results.xyxyn[0][:, -1].numpy()
        classes = [model.names[int(i)] for i in labels]

        vehicle_count = sum([1 for cls in classes if cls in vehicle_classes])
        cv2.putText(frame, f'Vehicles: {vehicle_count}', (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("YOLO Traffic Detection", frame)
        if cv2.waitKey(1) == 27:  # ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()
