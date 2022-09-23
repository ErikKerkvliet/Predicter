import os
from os import rename

KERAS_MODAL_PATH = './../keras_model'


class Globalvar:

    def __init__(self):
        pass

    @staticmethod
    def move_file(file_path):
        os.rename(f'./../', f'./../../MoneyTree/action_images')
