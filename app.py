from math import sqrt
from sys import argv

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase

import design

# pushButton - кнопка «Рассчитать»
# a_field - поле для ввода a
# b_field - поле для ввода b
# h_field - поле для ввода h
# answer_text - поле для вывода ответа 

class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        """Метод инициализации интерфейса."""
        super().__init__()
        QFontDatabase.addApplicationFont('fonts/circe.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-bold.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-extrabold.ttf')
        self.setupUi(self)
        self.pushButton.clicked.connect(self.count)

    def __text_to_html(self, text, font_family='Circe', font_size=14):
        """Возвращает HTML-разметку для поля вывода ответа с переданным текстом text."""
        return f'''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
    <meta name="qrichtext" content="1" />
    <style type="text/css">
        p, li {{ white-space: pre-wrap; }}
    </style>
</head>
<body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-family:'{font_family}'; font-size:{font_size}pt;">{text}</span></p>
</body>
</html>'''

    def set_answer(self, answer, font_family='Circe', font_size=14):
        """Устанавливает ответ answer в поле ответа."""
        return self.answer_text.setHtml(self.__text_to_html(answer))

    def count(self):
        """Выполняет расчёты на основании данных значений."""
        Rs = 350    # МПа  - растянутая арматура класса A400
        As = 2945   # мм²  - площадь сечения арматуры (6Ø25)
        Rb = 14.5   # МПа  - тяжёлый бетон класса B25
        M = 550     # кН·м - изгибающий момент с учетом кратковр. нагрузок
        ξR = 0.531  # Значение для арматуры А400 (с. 54, таблица 3.3)

        # Валидация введённых значений
        try:
            # Пробуем преобразовать полученные значения str в float для расчётов
            fields = (self.a_field.text(), self.b_field.text(), self.h_field.text())
            a, b, h = tuple(map(int, fields))
        except ValueError:
            # Так как в полях обнаружен текст, вызывается ошибка ValueError
            if fields == ('', '', ''):
                # Если ничего не было введено, то выставляем 
                # стандартные значения, указанные в задаче
                self.a_field.setText('70')
                self.b_field.setText('300')
                self.h_field.setText('800')
                a, b, h = 70, 300, 800
            else:
                # Если введен текст, пишем об этом в поле ответа.
                return self.set_answer('Введены не числа. Повторите попытку.')

        h0 = h - a # мм

        try:
            x = (Rs * As) / (Rb * b) # мм
            ξ = x / h0
            if ξ < ξR:
                # Условие 3.20
                case = round((Rs * As * (h0 - 0.5 * x)) / 10**6, 1)
                if M <= case:
                    return self.set_answer(f'M = {M} кН·м ⩽ {case} кН·м, прочность сечения обеспечена.')
                else:
                    return self.set_answer(f'M = {M} кН·м > {case} кН·м, прочность сечения НЕ обеспечена.')
            else:
                # Условие 3.21
                αr = ξR * (1 - 0.5 * ξR)
                case = round((αr * Rb * h0 * h0), 1)
                if M <= case:
                    return self.set_answer(f'M = {M} ⩽ {case}, прочность сечения обеспечена.')
                else:
                    return self.set_answer(f'M = {M} > {case}, прочность сечения НЕ обеспечена.')
        except ZeroDivisionError:
            # Обработчик ошибки деления на ноль
            self.set_answer(f'Обнаружено деление на ноль. Измените входные данные.')
            return


def main():
    app = QApplication(argv) 
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()