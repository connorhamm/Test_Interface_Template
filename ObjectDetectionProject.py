"""
Find a purpose for image recognition.

Ideas:
- Search through pictures based on item

1. Get an image database such as a folder of instagram pictures

App Logic:
1. Type in name, e.g "Tennis Racquet"
- seperate PyQT5 program
2. List picture file names
- AI program
3. Click picture file name to open picture
- Basic opening of a picture


"""

from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image2.jpg"), output_image_path=os.path.join(execution_path , "image2new.jpg"), minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")

