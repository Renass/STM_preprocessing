import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import preprocessing_folder
from PyQt5.QtGui import QPixmap

import winsound

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class Widget(QDialog):
    def __init__(self):
        super(Widget, self).__init__()
        #loadUi('widget5.ui', self)
        #qpixmap = QPixmap('cmaps.jpg')
        loadUi(sys._MEIPASS + '/widget5.ui', self)
        qpixmap = QPixmap(sys._MEIPASS + '/cmaps.jpg')
        self.options = {'dir':-1,
                        'cmap':-1,
                        'micro_on':-1,
                        'spectro_on':-1,
                        'micro_eq1':-1,
                        'micro_eq2':-1}
        

        self.obj_type_micro_button.setChecked(True)
        self.obj_type_spectro_button.setChecked(True)
        self.dir_button1.toggled.connect(lambda: self.set_option(('dir','current')))
        self.dir_button2.toggled.connect(lambda: self.set_option(('dir','inner')))
        self.dir_button1.toggle()
        self.equa_write1.setText('1')
        self.equa_write2.setText('99')
        self.cmap_img.setPixmap(qpixmap)
        self.cmap_button1.toggled.connect(lambda: self.set_option(('cmap',0)))
        self.cmap_button2.toggled.connect(lambda: self.set_option(('cmap',1)))
        self.cmap_button1.toggle()
        self.start_button.clicked.connect(self.start)

    def set_option(self, option):
        self.options[option[0]] = option[1]

    def start(self):
        self.beep_melody()
        self.options['micro_on'] = self.obj_type_micro_button.isChecked()
        self.options['spectro_on'] = self.obj_type_spectro_button.isChecked()
        self.options['micro_eq1'] = self.equa_write1.text()
        self.options['micro_eq2'] = self.equa_write2.text()
        if self.options['micro_on']==True:
            preprocessing_folder.sm4_microscopy_preprocess(self.options['dir'],self.options['cmap'], int(self.options['micro_eq1']), int(self.options['micro_eq2']))
        if self.options['spectro_on']==True:
            preprocessing_folder.sm4_spectroscopy_preprocess(self.options['dir'])
        sys.exit()

    def beep_melody(self):
        winsound.Beep(600, 500)

    def melody(self):
        self.c4 = 262
        self.d4 = 294
        self.e4 = 330
        self.f4 = 349
        self.g4 = 392
        self.a4 = 440
        self.b4 = 494
        self.c5 = 523

        winsound.Beep(self.c4, 1000)
        winsound.Beep(self.g4, 1000)
        winsound.Beep(self.f4, 167)
        winsound.Beep(self.e4, 167)
        winsound.Beep(self.d4, 167)
        winsound.Beep(self.c5, 1000)
        winsound.Beep(self.g4, 500)

        winsound.Beep(self.f4, 167)
        winsound.Beep(self.e4, 167)
        winsound.Beep(self.d4, 167)
        winsound.Beep(self.c5, 1000)
        winsound.Beep(self.g4, 500)

        winsound.Beep(self.f4, 167)
        winsound.Beep(self.e4, 167)
        winsound.Beep(self.f4, 167)
        winsound.Beep(self.d4, 2000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Widget()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedWidth(655)
    widget.setFixedHeight(425)
    widget.show()
    app.exec_()
    #sys.exit(app.exec_())