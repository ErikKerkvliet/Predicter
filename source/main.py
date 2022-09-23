from globalvar import Globalvar
from predict import Predict


class Main:

    def __init__(self):
        self.glv = Globalvar()
        self.predict = Predict(self.glv)

    @staticmethod
    def start():
        print('start')
        pass


if __name__ == '__main__':
    main = Main
    main.start()

    exit(0)
