from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, \
    QHBoxLayout, QLabel,  QSpacerItem, QSizePolicy, QSpinBox, QLineEdit
import sys

# Задание:
# 1. понять код в этом файле (НА СКОЛЬКО ВОЗМОЖНО ПОНЯЛ КОД)
# 2. Добавить в самый верх виджета Window виджет с названием тренировки (тип виджета: QLineEdit)
# 3. добавить в виджет SportExercise колонки 'Количество повторений', 'Рабочий вес' (СДЕЛАЛ!)

class TrainingName(QLineEdit):
    def __init__(self, name):
        name(QLineEdit)
        self.resize(350, 250)


# Класс виджета 'спортивное упражнение'
class SportExercise(QWidget):
    def __init__(self, name, parent=None):
        super(SportExercise, self).__init__(parent)

        # Это главная гозизонтальная компоновка
        self.row = QHBoxLayout()

        nameLbl = QLabel(name)
        self.row.addWidget(nameLbl) # добвляем виджет в компоновку

        self.row.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # добавляем растяжение в компоновку

        # Столбик количество подходов
        number_podhodov_layout = QVBoxLayout() # вертикальная компоновка
        number_podhodov_lbl = QLabel("Количество подходов")
        number_podhodov_layout.addWidget(number_podhodov_lbl)
        number_podhodov_spinbox = QSpinBox()
        number_podhodov_spinbox.setSingleStep(1)  # Значение спинбокса изменяется при нажатии на 1
        number_podhodov_layout.addWidget(number_podhodov_spinbox)

        number_povtoreniy_layout = QVBoxLayout()
        number_povtoreniy_lbl = QLabel("Количество повторений")
        number_povtoreniy_layout.addWidget(number_povtoreniy_lbl)
        number_povtoreniy_spinbox = QSpinBox()
        number_povtoreniy_layout.addWidget(number_povtoreniy_spinbox)

        number_weight_layout = QVBoxLayout()
        number_weight_lbl = QLabel("Рабочий вес")
        number_weight_layout.addWidget(number_weight_lbl)
        number_weight_spinbox = QSpinBox()
        number_weight_layout.addWidget(number_weight_spinbox)

        self.row.addLayout(number_podhodov_layout)
        self.row.addLayout(number_povtoreniy_layout)
        self.row.addLayout(number_weight_layout)

        self.setLayout(self.row)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # главная (вертикальная) компоновка для окна
        mainlayout = QVBoxLayout()

        # Create the list
        mylist = QListWidget()

        for exercise_name in ["Отжимания", "Шраги", "Поднятие штанги на бицепс"]:
            # QListWidgetItem - это как бы ячейка, в которую мы можем поместить свой виджет
            item = QListWidgetItem(mylist)
            mylist.addItem(item)

            se = SportExercise(name=exercise_name)
            item.setSizeHint(se.minimumSizeHint())  # item имеет такой же размер, что и se

            # Привязываем виджет 'спортивное упражнение' с QListWidgetItem
            mylist.setItemWidget(item, se)

        mainlayout.addWidget(mylist)
        self.setLayout(mainlayout)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()