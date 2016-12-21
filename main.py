from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5.QtWidgets import QApplication, QWidget

from sqlalchemy.orm import sessionmaker
from models import engine, User

Session = sessionmaker(bind=engine)
session = Session()


class DbThread(QThread):
    sig = pyqtSignal(object)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        user = session.query(User).filter_by(id=1).first()
        self.sig.emit(user)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('main.ui', self)

    def on_data_ready(self, data):
        self.ui.label.setText(data.name)

    @pyqtSlot()
    def slot_firstButton(self):
        dbthread = DbThread()
        dbthread.sig.connect(self.on_data_ready)
        dbthread.start()

    @pyqtSlot()
    def slot_secondButton(self):
        self.ui.label.setText("두번째 버튼")

    @pyqtSlot()
    def slot_thirdButton(self):
        self.ui.label.setText("세번째 버튼")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())