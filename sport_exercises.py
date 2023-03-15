from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, \
    QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QSpinBox, QLineEdit
import sys


# Задание:
# 1. понять код в этом файле (НА СКОЛЬКО ВОЗМОЖНО ПОНЯЛ КОД)
# 2. Добавить в самый верх виджета Window виджет с названием тренировки (тип виджета: QLineEdit)
# 3. добавить в виджет SportExercise колонки 'Количество повторений', 'Рабочий вес' (СДЕЛАЛ!)

# Задание 2
# 1. добавить в класс SportExercise для упражения элемент QLabel (справа от 'Рабочий вес'),
#    который будет в будущем отображать тоннаж этого упражнения
# 2. написать функцию, которая получает на вход 3 параметра:
#    a. количество подходов; b. количество повторений; c. рабочий вес
#    функция должна возвращать тоннаж, исходя из значений этих параметров
# 3. удалить из git папки .idea и __pycache__ (воспользоваться командой: git rm --cached <file>)

# Задание 3
# 1. Под списком заданий создать QHBoxLayout, который содержит 2 QLabel:
#    - первый QLabel отображает надпись: "Общий тоннаж"
#    - второй QLabel будет отображать суммарное значение тоннажа для всех упражнений
# 2. Создать для класса SportExercise метод с именем get_tonaj, который возвращает тоннаж для этого упражнения
# 3. Изучить статью по сигналам и слотам в pyqt: https://pythonworld.ru/gui/pyqt5-eventssignals.html
# 4. Создать сигнал для класса SportExercise с названием tonaj_changed
# 5. изучить статью про лямбда функции: https://habr.com/ru/company/piter/blog/674234/

# Дополнение к заданию 3
# 1. комментарий к коммиту лучше делать на английском языке: git commit -m 'You should use English here'
# 2. не добавлять папки (.idea), которые не относятся к разработанным нами файлам и не
#    будут полезны для тех, кто пользуется репозиторием
# 3. нужно добавить .idea в .gitignore
# 4. названия переменных (классов, функций) должны отражать их сущность:
#    a. то есть если мы создаем объект класса QLabel -> то название button этой переменной не подходит,
#    потому что это надпись, а не кнопка
#    b. избегать названий для переменных типа "a", "b", "size1", "size2" -> ведь если увидишь в коде
#       переменную с таким названием, то сразу не поймешь, для чего она нужна


def calculate_tonaj(count_podhodov, robociy_ves, count_povtoreniy):
    tonaj = (count_povtoreniy * robociy_ves) * count_podhodov
    return tonaj


# Класс виджета 'спортивное упражнение'
class SportExercise(QWidget):
    def __init__(self, name, parent=None):
        super(SportExercise, self).__init__(parent)

        # Это главная гозизонтальная компоновка
        self.row = QHBoxLayout()

        nameLbl = QLabel(name)
        self.row.addWidget(nameLbl)  # добвляем виджет в компоновку

        self.row.addItem(
            QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))  # добавляем растяжение в компоновку

        # Столбик количество подходов
        number_podhodov_layout = QVBoxLayout()  # вертикальная компоновка
        number_podhodov_lbl = QLabel("Количество подходов")
        number_podhodov_layout.addWidget(number_podhodov_lbl)
        self.number_podhodov_spinbox = QSpinBox()
        self.number_podhodov_spinbox.setSingleStep(1)  # Значение спинбокса изменяется при нажатии на 1
        number_podhodov_layout.addWidget(self.number_podhodov_spinbox)

        number_povtoreniy_layout = QVBoxLayout()
        number_povtoreniy_lbl = QLabel("Количество повторений")
        number_povtoreniy_layout.addWidget(number_povtoreniy_lbl)
        self.number_povtoreniy_spinbox = QSpinBox()
        number_povtoreniy_layout.addWidget(self.number_povtoreniy_spinbox)

        number_weight_layout = QVBoxLayout()
        number_weight_lbl = QLabel("Рабочий вес")
        number_weight_layout.addWidget(number_weight_lbl)
        self.number_weight_spinbox = QSpinBox()
        self.number_weight_spinbox.setMaximum(999)
        number_weight_layout.addWidget(self.number_weight_spinbox)

        tonaj_layout = QVBoxLayout()
        tonaj_lbl = QLabel("Тоннаж")
        tonaj_layout.addWidget(tonaj_lbl)
        self.tonaj_value_lbl = QLabel("0")
        tonaj_layout.addWidget(self.tonaj_value_lbl)

        self.row.addLayout(number_podhodov_layout)
        self.row.addLayout(number_povtoreniy_layout)
        self.row.addLayout(number_weight_layout)
        self.row.addLayout(tonaj_layout)

        self.number_podhodov_spinbox.valueChanged.connect(self.update_tonaj)
        self.number_povtoreniy_spinbox.valueChanged.connect(self.update_tonaj)
        self.number_weight_spinbox.valueChanged.connect(self.update_tonaj)

        self.setLayout(self.row)

    def update_tonaj(self):
        count_podhodov = self.number_podhodov_spinbox.value()
        robociy_ves = self.number_weight_spinbox.value()
        count_povtoreniy = self.number_povtoreniy_spinbox.value()
        tonaj = calculate_tonaj(count_podhodov, robociy_ves, count_povtoreniy)
        self.tonaj_value_lbl.setText(str(tonaj))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # главная (вертикальная) компоновка для окна
        mainlayout = QVBoxLayout()

        name_of_training_lbl = QLineEdit("Тренировка 1")
        mainlayout.addWidget(name_of_training_lbl)

        # Create the list of exercises
        exercises_list = QListWidget()

        for exercise_name in ["Отжимания", "Шраги", "Поднятие штанги на бицепс"]:
            # QListWidgetItem - это как бы ячейка, в которую мы можем поместить свой виджет
            item = QListWidgetItem(exercises_list)
            exercises_list.addItem(item)

            se = SportExercise(name=exercise_name)
            item.setSizeHint(se.minimumSizeHint())  # item имеет такой же размер, что и se

            # Привязываем виджет 'спортивное упражнение' с QListWidgetItem
            exercises_list.setItemWidget(item, se)

        # Добавляется таблица с упражнениями
        mainlayout.addWidget(exercises_list)

        # Обший тоннаж добавляется под таблицу
        obsiy_tonaj_layout = QHBoxLayout()
        tonaj_sum_description_lbl = QLabel("Общий тоннаж:")
        tonaj_sum_value_lbl = QLabel("0")
        obsiy_tonaj_layout.addWidget(tonaj_sum_description_lbl)
        obsiy_tonaj_layout.addWidget(tonaj_sum_value_lbl)
        obsiy_tonaj_layout.addItem(
            QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed))

        mainlayout.addLayout(obsiy_tonaj_layout)

        self.setLayout(mainlayout)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.resize(700, 400)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
