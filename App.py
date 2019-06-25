#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
# Labelki
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
# buttonki
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout

# message + zamkniecie
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        self.resize(300, 100)
        self.setWindowTitle("Prosty kalkulator")
        self.show()
        # labelki
        etykieta1 = QLabel("Calculator", self)

        # przypisanie widgetów do układu tabelarycznego
        layoutT = QGridLayout()
        layoutT.addWidget(etykieta1, 0, 0)

        # 1-liniowe pola edycyjne
        self.windowEdt = QLineEdit()

        self.windowEdt.readonly = True
        self.windowEdt.setToolTip('write <b>numbers</b> and select ...')

        layoutT.addWidget(self.windowEdt, 1, 0)
        # ukladT.addWidget(self.liczba2Edt, 1, 1)
        # ukladT.addWidget(self.wynikEdt, 1, 2)

        # buttons - numbers
        numbersBtns = {
            'oneBtn': QPushButton('1', self),
            'twoBtn': QPushButton('2', self),
            'threeBtn': QPushButton('3', self),
            'fourBtn': QPushButton('4', self),
            'fiveBtn': QPushButton('5', self),
            'sixBtn': QPushButton('6', self),
            'sevenBtn': QPushButton('7', self),
            'eightBtn': QPushButton('8', self),
            'nineBtn': QPushButton('9', self),
            'zeroBtn': QPushButton('0', self),
            'comaBtn': QPushButton(',', self)
        }

        # buttons - dzialanie
        i = 0
        j = 0
        layoutNumbers = QGridLayout()
        for button in numbersBtns:
            layoutNumbers.addWidget(numbersBtns[button],j,i)
            i += 1
            if i > 2 :
                i = 0
                j += 1

        layoutT.addLayout(layoutNumbers, 2, 0, 1, 3)


        dodajBtn = QPushButton("+", self)
        odejmijBtn = QPushButton("-", self)
        dzielBtn = QPushButton("*", self)
        mnozBtn = QPushButton("/", self)
        koniecBtn = QPushButton("&Close", self)
        # koniecBtn.resize(koniecBtn.sizeHint())

        layoutH = QHBoxLayout()
        layoutH.addWidget(dodajBtn)
        layoutH.addWidget(odejmijBtn)
        layoutH.addWidget(dzielBtn)
        layoutH.addWidget(mnozBtn)

        layoutT.addLayout(layoutH, 2, 1, 1, 3)
        layoutT.addWidget(koniecBtn, 3, 0, 1, 3)

        # dodajBtn.clicked.connect(self.dzialanie)
        # odejmijBtn.clicked.connect(self.dzialanie)
        # mnozBtn.clicked.connect(self.dzialanie)
        # dzielBtn.clicked.connect(self.dzialanie)

        # koniecBtn.clicked.connect(self.koniec)

        # przypisanie utworzonego układu do okna
        self.setLayout(layoutT)

        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Prosty kalkulator")
        self.show()

    def dzialanie(self):

        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = float(self.liczba2Edt.text())
            wynik = ""

            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + liczba2
            elif nadawca.text() == "&Odejmij":
                wynik = liczba1 - liczba2
            elif nadawca.text() == "&Mnóż":
                wynik = liczba1 * liczba2
            else:  # dzielenie
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return

            self.wynikEdt.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

    def koniec(self):
        self.close()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())
