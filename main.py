# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
 
# Глобальные настройки
Window.size = (250, 200)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
Window.title = "Конвертер"


class MyApp(App):

    # Создание всех виджетов (объектов)
    def __init__(self):
        super().__init__()
        self.charge = Label(text='Charge')
        self.oncharge = Label(text='Time to charge')
        self.trip = Label(text='Time to trip')
        self.distance = Label(text='Got Distance')
        self.input_data = TextInput(hint_text='How much volts?', multiline=False)
        self.input_data.bind(text=self.on_text)  # Добавляем обработчик события

    # Получаем данные и производит их конвертацию
    def on_text(self, *args):
        data = self.input_data.text

        if data:
            #19.2 разброс верх низ для 60v  
            self.charge.text = 'Заряда осталось: ' + str(round((((float(data.replace(',','.'))-48) * 100)/19.2), 2)) + ' % батареи'
            percentcharged = str((((float(data.replace(',','.'))-48) * 100)/19.2))
            self.oncharge.text = 'Время на подзарядку: ' + str(round(11.5 - (11.5 * (float(percentcharged)/100)), 2))+ ' часа'
            self.trip.text = 'Остаточное время пути: ' + str(round(3 - (3 * (float(percentcharged)/100)), 2)) + ' часа'
            self.distance.text = 'Остаточное расстояние: ' + str(round( (50 * (float(percentcharged)/100)), 2)) + ' км'

    # Основной метод для построения программы
    def build(self):
        # Все объекты будем помещать в один общий слой
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.input_data)
        box.add_widget(self.charge)
        box.add_widget(self.oncharge)
        box.add_widget(self.trip)
        box.add_widget(self.distance)
        return box


# Запуск проекта
if __name__ == "__main__":
    MyApp().run()
