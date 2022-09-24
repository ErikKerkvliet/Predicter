import os
import time

from globalvar import PREDICTIONS
from globalvar import LABEL_FOLDERS


class Watcher:

    def __init__(self, glv):
        self.glv = glv
        self.predictor = self.glv.get_predictor()

    def watch(self, watch_path):
        while True:
            image_folders = os.listdir(watch_path)
            for image_folder in image_folders:
                label_folders = os.listdir(f'{watch_path}/{image_folder}')

                for label_folder in label_folders:
                    if label_folder in LABEL_FOLDERS:
                        files = os.listdir(f'{watch_path}/{image_folder}/{label_folder}')
                        for file in files:
                            file_path = f'{watch_path}/{image_folder}/{label_folder}/{file}'
                            prediction = self.predictor.predict(file_path)

                            self.handle_prediction(prediction, file)

            time.sleep(1)

    def handle_prediction(self, prediction, file_path):
        # for key in PREDICTIONS.keys():
        if prediction == PREDICTIONS.keys()[0]:
            self.glv.move_file(file_path)
