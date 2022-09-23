import numpy as np

from keras.models import load_model
from PIL import Image, ImageOps

from globalvar import KERAS_MODAL_PATH


class Predict:

    def __init__(self, glv):
        self.glv = glv
        self.image = None
        self.model = self.load_model()

    @staticmethod
    def load_model():
        return load_model(f'{KERAS_MODAL_PATH}/keras_modal.h5')

    @staticmethod
    def load_image(image_path):
        image = Image.open(image_path)

        size = (224, 224)
        return ImageOps.fit(image, size, Image.ANTIALIAS)

    def load_image_data(self, image_path):
        image = self.load_image(image_path)

        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        data[0] = normalized_image_array

        return data

    def predict(self, image_path):
        data = self.load_image_data(image_path)

        prediction = self.model.predict(data)

        if prediction == 2:
            self.glv.move_image(image_path)
