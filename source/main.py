from globalvar import Globalvar, TRAINING_DATA_PATH
from watcher import Watcher


class Main:

    def __init__(self):
        self.glv = Globalvar()
        self.watcher = Watcher(self.glv)

    def start(self):
        self.watcher.watch(TRAINING_DATA_PATH)


if __name__ == '__main__':
    main = Main()
    main.start()

    exit(0)
