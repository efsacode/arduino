import sys
import serial
import time
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Arduino Veri Grafiği")
        self.setGeometry(100, 100, 800, 600)

        # Grafiği oluştur
        self.graphWidget = PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # Seri port ayarları
        self.serial_port = serial.Serial('COM3', 9600)  # COM portunu ayarlayın
        time.sleep(2)  # Portun açılması için bekle

        self.data = []
        self.x = []

        # Güncelleme döngüsü
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)  # Her saniyede bir güncelle
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        if self.serial_port.in_waiting > 0:
            line = self.serial_port.readline().decode('utf-8').strip()
            values = list(map(int, line.split(' ')))

            # Verileri güncelle
            self.x = list(range(len(values)))
            self.data = values

            # Grafiği güncelle
            self.graphWidget.clear()
            self.graphWidget.plot(self.x, self.data, pen='b', symbol='o')  # Mavi çizgi ve noktalar

    def closeEvent(self, event):
        if self.serial_port.isOpen():
            self.serial_port.close()  # Uygulama kapanırken seri portu kapat

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
