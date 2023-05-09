from Detector import *
from model_inference.VGG19 import *
from model_inference.Resnet import *
from model_inference.Inception import *
from model_inference.Xception import *
import os


def main():
    print("Welcome to breed_bot")
    print("please select from the following options")
    print("Which selected_model do you like use for classifying \n1. Xception\n2. Inception\n3. ResNet-50\n4. VGG-19")
    option = input()
    match option:
        case "1":
            selected_model = Xception('TrainedModels/Model_Xception.h5')
        case "2":
            selected_model = Inception('TrainedModels/Model_Inception.h5')
        case "3":
            selected_model = Resnet('TrainedModels/Model_Resnet50.h5')
        case "4":
            selected_model = VGG19('TrainedModels/Model_VGG19.h5')



    print("Please select the input option?")
    print("\n1. SavedVideo\n2. Webcam")
    input_choice = input()
    match input_choice:
        case "1":
            Input_VideoPath = 'input_video.avi'
        case "2":
            Input_VideoPath = 0



    modelPath = os.path.join('inferenceData', 'frozen_inference_graph.pb')
    configPath = os.path.join('inferenceData', 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
    classesPath = os.path.join('inferenceData', 'coco.names')


    dog_detector = Detector(Input_VideoPath, configPath, modelPath, classesPath)

    dog_detector.onVideo(selected_model)




if __name__=="__main__":
    main()



