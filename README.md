# Find My Face

A Simple Face and Eye recognition model using [OpenCV](https://opencv.org/) Harcaascade models. The model draws red color boundry around the face and green color boundries across both eyes. It is really interesting to see the potential OpenCV has.

[![](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/images/0)](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/links/0)[![](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/images/1)](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/links/1)[![](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/images/2)](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/links/2)[![](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/images/3)](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/links/3)[![](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/images/4)](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/links/4)[![](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/images/5)](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/links/5)[![](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/images/6)](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/links/6)[![](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/images/7)](https://sourcerer.io/fame/engrravijain/engrravijain/FindMyFace/links/7)

## Basics

Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

Here we will work with face detection. Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. Then we need to extract features from it. For this, haar features shown in below image are used. They are just like our convolutional kernel. Each feature is a single value obtained by subtracting sum of pixels under white rectangle from sum of pixels under black rectangle.

![Cascades](https://docs.opencv.org/master/haar_features.jpg)

## Haar-cascade Detection in OpenCV

OpenCV comes with a trainer as well as detector. If you want to train your own classifier for any object like car, planes etc. you can use OpenCV to create one. Its full details are given here: Cascade Classifier Training.

Here we will deal with detection. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc. Those XML files are stored in the opencv/data/haarcascades/ folder.

Let's create a face and eye detector with OpenCV.

## Run it Locally

### Anaconda environment

```
$ conda create --name find-my-face python=3.7
$ conda activate find-my-face
```

creating the yml file be like

```
$ conda env export > sms-spam-find-my-face.yml
$ conda env create -f sms-spam-find-my-face.yml
```

Follow the below mentioned steps to run the model on your system.

```console
$ git clone https://github.com/engrravijain/FindMyFace.git
$ cd FindMyFace
$ conda env create -f sms-spam-find-my-face.yml
$ conda activate find-my-face
$ python face_eye_harcaascade.py
```

## Refrence

* [OpenCV Tutorial](https://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html)