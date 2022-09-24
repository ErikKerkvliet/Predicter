from os import rename
from predictor import Predictor

KERAS_MODEL_PATH = './../keras_model'
ACTION_IMAGES_PATH = './../../MoneyTree/action_images'
TRAINING_DATA_PATH = './../../TrainingData/data'
LABEL_FOLDERS = ['yes_plus']

PREDICTIONS = {
    0: 'BUY',
    1: 'SELL',
    2: 'NONE',
}


class Globalvar:

    def __init__(self):
        self.predictor = Predictor(self)

    def get_predictor(self) -> Predictor:
        return self.predictor

    @staticmethod
    def move_file(file_path) -> None:
        rename(file_path, f'{ACTION_IMAGES_PATH}/{file_path}')
