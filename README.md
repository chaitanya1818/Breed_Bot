# Breed-Bot


### Team Members :

    ● Jaswanth Karangula - 016522818
    ● Venkata Sai Sri Batchu - 016118557
    ● Suhas Byrapuneni - 016118596
    ● Venkata Chandu Konduru - 016726775
    
    
### Requirements and Dependencies :

    ● Tensorflow - 2.12.0
    ● Keras - 2.10.0
    ● Jupyter/Colab Notebook
    ● OpenCV - 4.7.0
    ● Matplotlib - 3.5.1
    ● Numpy - 1.21.5
    ● Scikit-learn - 1.0.2
    ● Python - 3.10.9


### Files :

    ● bottleneck_features - A folder containing the bottleneck features of the 4 models. Download links
    for all 4 models have been provided in the below section.
    ● training_model_data - A folder containing the Object detection model. Refer
    https://github.com/haroonshakeel/real_time_object_detection_cpu for more information.
    ● dogImages - A folder containing the images separated into training , validation and test folders.
    The link to download is https://drive.google.com/drive/folders/1_s3H1TElpj0qBjP5cIC81kTHJhdShB0x?usp=share_link
    ● Models - A folder that contains all the saved models and weights.
    ● Output_video - A folder which saves the out video
    ● input.avi - input video of testing images for dog.
    ● Model_training.ipynb - A colab notebook for training all the models and saving them.
    ● Resnet-50.py - loads Resnet-50 model and makes predictions.
    ● Inception.py - loads Inception model and makes predictions.
    ● VGG19.py -     loads VGG-19 layer model and makes predictions.
    ● Xception.py -  loads Xception model and makes predictions.
    ● Detector.py - askes the user options and predcits the model output.
    ● main.py - This is the main file which needs to be run. All other files are imported into this file.
   

### Dataset :

    ● You can download the dog dataset from the below link: https://drive.google.com/drive/folders/1_s3H1TElpj0qBjP5cIC81kTHJhdShB0x?usp=share_link

    ● This data collection contains 8,287 photos of 127 distinct breeds. The quantity of photos provided for the models to learn from is around 67 per breed, which may not be sufficient for CNN.



### Training phase :

We have modified code in colab for training the data which requires more space to train the model and saves the model.

    ● For the rest of the pretrained models we need to download the bottleneck features. Bottleneck
    features are the last activation maps before the fully-connected layers in a pretrained model. We
    remove the last fully connected layer from the model and plug in your layers there.
    ● Place the downloaded files in a folder bottleneck_features in your working directory.
    ● The "CNN model from scratch" may be trained by running all of the code blocks in the notebook under it.
    ● save the trained models into colab directory and you download to local/

### Steps to run the Code :

    ● we need to run the file main.py after creating and saving all the required data.
    ● model option will be displayed and user needs to select the model.
    ● next user will be asked with live webcam or 
    ● selcting video we need to provide 
    ● selectin live cam,you need toshow some dog images to get prediction
    
### Results :
    ● accuracy of each model can be found in traning notebooks
    ● The main file can be used to test the models' real-time performance. It takes the input 'video.mp4' and stores the result video in the output folder and result is displayed with bounding box.