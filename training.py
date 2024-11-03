yolo task=detect mode=train model=yolov8s.pt data="D:\Code_Sources\YourEye\Training_YoloV8\dataset\data.yaml" epochs=5 imgsz=640 device=0

yolo task=detect mode=train model=yolov8s.pt data="D:\Code_Sources\YourEye\Training_YoloV8\dataset\data.yaml" epochs=5 imgsz=640 device=0 lr0=0.001

# SUCCESS
AMP (Automatic Mixed Precision) kullanımı sırasında bazı donanım veya veri seti uyumsuzlukları NaN hatalarına yol açabilir.
yolo task=detect mode=train model=yolov8s.pt data="D:\Code_Sources\YourEye\Training_YoloV8\dataset\data.yaml" epochs=2 imgsz=640 device=0 amp=False




yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=5 imgsz=800 plots=True