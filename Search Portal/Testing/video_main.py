# ---- coding: utf-8 ----
# ===================================================
# Author: Karthikeyan M
# ===================================================
"""Description: Class with methods to do facial recognition
on video or webcam feed.

Usage: python -m face_recog.video_main"""
# ===================================================
from datetime import datetime
from email.mime import image
from fileinput import filename
from pydoc import locate
import sys
import time
import traceback
from typing import Dict, List

import os

import csv
import glob

import cv2
import numpy as np
from pyparsing import delimited_list
####import matplotlib.pyplot as plt

from face_recog.exceptions import NoNameProvided, PathNotFound
from face_recog.face_detection_dlib import FaceDetectorDlib
from face_recog.face_detection_mtcnn import FaceDetectorMTCNN
from face_recog.face_detection_opencv import FaceDetectorOpenCV
from face_recog.face_recognition import FaceRecognition
from face_recog.logger import LoggerFactory
from face_recog.media_utils import (
    convert_to_rgb,
    draw_annotation,
    draw_bounding_box,
    get_video_writer,
)
from face_recog.validators import path_exists

# Load the custom logger
logger = None
try:
    logger_ob = LoggerFactory(logger_name=__name__)
    logger = logger_ob.get_logger()
    logger.info("{} loaded...".format(__name__))
    # set exception hook for uncaught exceptions
    sys.excepthook = logger_ob.uncaught_exception_hook
except Exception as exc:
    raise exc


class FaceRecognitionVideo:
    """Class with methods to do facial recognition on video or webcam feed."""

    def __init__(
        self,
        face_detector: str = "dlib",
        model_loc: str = "models",
        persistent_db_path: str = "E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/data/facial_data.json",
        face_detection_threshold: float = 0.8,
    ) -> None:

        self.face_recognizer = FaceRecognition(
            model_loc=model_loc,
            persistent_data_loc=persistent_db_path,
            face_detection_threshold=face_detection_threshold,
            face_detector=face_detector,
        )
        if face_detector == "opencv":
            self.face_detector = FaceDetectorOpenCV(
                model_loc=model_loc, crop_forehead=True, shrink_ratio=0.2
            )
        elif face_detector == "mtcnn":
            self.face_detector = FaceDetectorMTCNN(crop_forehead=True, shrink_ratio=0.2)
        elif face_detector == "dlib":
            self.face_detector = FaceDetectorDlib()

    def recognize_face_video(
        self,
        video_path: str = None,
        detection_interval: int = 15, #milli second
        save_output: bool = False,
        preview: bool = False,
        output_path: str = "E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/data/output.mp4",
        resize_scale: float = 0.5,
        verbose: bool = True,
    ) -> None:

        if video_path is None:
            # If no video source is given, try
            # switching to webcam
            video_path = 0
        elif not path_exists(video_path):
            raise FileNotFoundError

        cap, video_writer = None, None

        try:
            cap = cv2.VideoCapture(video_path)

            # Check if the webcam is opened correctly
            if not cap.isOpened():
                raise IOError("Cannot open Webcam")
            
            # To save the video file, get the opencv video writer
            video_writer = get_video_writer(cap, output_path)
            frame_num = 1
            matches, name, match_dist = [], None, None

            t1 = time.time()
            #logger.info("Enter s to save...")
            logger.info("Enter q to exit...")

            while True:
                status, frame = cap.read()
                if not status:
                    break
                try:
                    # Flip webcam feed so that it looks mirrored
                    if video_path == 0:
                        frame = cv2.flip(frame, 2)

                    if frame_num % detection_interval == 0:
                        # Scale down the image to increase model
                        # inference time.
                        smaller_frame = convert_to_rgb(
                            cv2.resize(frame, (0, 0), fx=resize_scale, fy=resize_scale)
                        )
                        # Detect faces
                        matches = self.face_recognizer.recognize_faces(
                            image=smaller_frame, threshold=0.6, bboxes=None
                        )

                    #output_file(name)

                    if verbose:
                        self.annotate_facial_data(matches, frame, resize_scale)
                    if save_output:
                        video_writer.write(frame)
                        cv2.imwrite("Tested_images/Detected/Criminal/kk.jpg", frame)
                        #cv2.imwrite("Tested_images/Detected/Missing/image%04i.png", frame)
                        print("Detected Image Saving!...")
                    if preview:
                        cv2.imshow("Preview", cv2.resize(frame, (680, 480)))

                    key = cv2.waitKey(1) & 0xFF
                    if key == ord("q"):
                        print("Detected Image Saved!....")
                        break
                
                    '''if key == ord('s'):                        
                        #cv2.imwrite("data/detected_images/image%04i.png", frame)
                        cv2.imwritemulti("data/detected_images/image%04i.png", frame)
                        print("Detected Image Saved!...")'''
            
                except Exception:
                    pass
                frame_num += 1

            t2 = time.time()
            logger.info("Time:{}".format((t2 - t1) / 60))
            logger.info("Total frames: {}".format(frame_num))
            logger.info("Time per frame: {}".format((t2 - t1) / frame_num))

        except Exception as exc:
            raise exc
        finally:
            cv2.destroyAllWindows()
            cap.release()
            video_writer.release()

    def register_face_webcam(
        self, name: str = None, detection_interval: int = 5
    ) -> bool:
        if name is None:
            raise NoNameProvided

        cap = None
        try:
            cap = cv2.VideoCapture(0)
            frame_num = 0

            while True:
                status, frame = cap.read()
                if not status:
                    break

                if frame_num % detection_interval == 0:
                    # detect faces
                    bboxes = self.face_detector.detect_faces(image=frame)
                    try:
                        if len(bboxes) == 1:
                            facial_data = self.face_recognizer.register_face(
                                image=frame, name=name, bbox=bboxes[0]
                            )
                        if facial_data:
                            draw_bounding_box(frame, bboxes[0])
                            cv2.imshow("Registered Face", frame)
                            cv2.waitKey(0)
                            logger.info("Press any key to continue......")
                            break
                    except Exception as exc:
                        traceback.print_exc(file=sys.stdout)
                frame_num += 1
        except Exception as exc:
            raise exc
        finally:
            cv2.destroyAllWindows()
            cap.release()
            
    def register_face_path(self, img_path: str, name: str) -> None:
        if not path_exists(img_path):
            raise PathNotFound
        try:
            img = cv2.imread(img_path)
            facial_data = self.face_recognizer.register_face(
                image=convert_to_rgb(img), name=name
            )
            if facial_data:
                logger.info("Face registered...")
                return True
            return False
        except Exception as exc:
            raise exc

    def annotate_facial_data(
        self, matches: List[Dict], image, resize_scale: float
    ) -> None:
        if(not os.path.exists("E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/data/detection_list.csv")):
            f=open("E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/data/detection_list.csv","w")
        for face_bbox, match, accuracy in matches:
            name = match["name"] if match is not None else "Unknown"
            #match_dist = '{:.2f}'.format(dist) if dist < 1000 else 'INF'
            #name = name + ', Dist: {}'.format(match_dist)
            # draw face labels
            #draw_annotation(image, name, int(1 / resize_scale) * np.array(face_bbox))

            #accuracy = cv2.blur(image,(5,5))
            acc_img = '{:.2f}%'.format(accuracy * 1.5)
            #name = name + ', Acc: {}'.format(acc_img)
            name = name
            #location = ['Salem']
            acc = ', Acc: {}'.format(acc_img)
            sol = name + acc 
            draw_annotation(image, sol, int(1 / resize_scale) * np.array(face_bbox))

            '''homography = cv2.getPerspectiveTransform
            translation = np.zeros((3,1)) 
            translation[:,0] = homography[:,2]

            rotation = np.zeros((3,3))
            rotation[:,0] = homography[:,0]
            rotation[:,1] = homography[:,1]
            rotation[:,2] = np.cross(homography[0:3,0],homography[0:3,1])

            cameraMatrix = np.zeros((3,4))
            cameraMatrix[:,0:3] = rotation
            cameraMatrix[:,3] = homography[:,2]

            cameraMatrix = cameraMatrix/cameraMatrix[2][3] #normalize the matrix'''

            '''with open("data/listcsv.csv", "w", newline = "") as f:
                thewriter = csv.writer(f, delimiter = ',')
                thewriter.writerow(['Name', 'Accuracy'])
                f.writelines(f'\n[name, acc_img]')
            f.close()
            print("File Created and Updated!...")'''

            with open('E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/data/detection_list.csv','r+') as f:
                myDataList = f.readlines()
                nameList =[]
                for line in  myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                if name not in nameList:
                    now= datetime.now()
                    dtString =now.strftime('%H:%M:%S')
                    f.writelines(f'\n{dtString}, {name}, {acc_img}')
            print("File Created and Updated!...")

    '''def calculate_XYZ(self,u,v):
                                      
        #Solve: From Image Pixels, find World Points

        uv_1=np.array([[u,v,1]], dtype=np.float32)
        uv_1=uv_1.T
        suv_1=self.scalingfactor*uv_1
        xyz_c=self.inverse_newcam_mtx.dot(suv_1)
        xyz_c=xyz_c-self.tvec1
        XYZ=self.inverse_R_mtx.dot(xyz_c)

        return XYZ'''

if __name__ == "__main__":

    ob = FaceRecognitionVideo(face_detector='dlib')
    ob.recognize_face_video(video_path=None,
            detection_interval=5, save_output=True, preview=True)
    #register a face using the webcam
    #ob.register_face_webcam(name="Unknown")

    ################ 1 ####################
    #Register faces for videos
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Missing/Abishek.jpg',name="Abishek")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Missing/APJ.jpg',name="APJ")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Missing/Dhoni.jpg',name="Dhoni")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Missing/Gowcickram_K.jpg',name="Gowcickram")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Missing/Harish_S.jpg',name="Harish")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Missing/Harshvardan_S_M.jpg',name="Harshvardan")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Missing/Jack_Sparrow.jpg',name="Jack Sparrow")

    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Criminal/Karthick.jpg',name="Karthick")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Criminal/Karthikeyan.jpg',name="Karthikeyan")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Criminal/Kholi.jpg',name="Kholi")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Criminal/Vijay.jpg',name="Vijay")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Criminal/M_K_Stalin.jpg',name="M K Stalin")
    ob.register_face_path(img_path=r'E:/Softwares/XAMPP/Xampp/htdocs/Search-Portal/Testing/Training_images/Criminal/Vijayakanth.jpg',name="Vijayakanth")

    


    #ob.recognize_face_video(video_path='D:/Testing/data/trimmed.mp4',
            #detection_interval=2, save_output=True, preview=True, resize_scale=0.25)

    #if path_exists('data/facial_data.json'):
        #os.remove('data/facial_data.json')
    #print('[INFO] Test DB file deleted...')

    ##########################################   