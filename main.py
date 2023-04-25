 
# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
 
# Глобальные настройки
#-- maximize first, to get the screen size, minus any OS toolbars
Window.maximize()
maxSize = Window.system_size

#-- set the actual window size, to be slightly smaller than full screen
desiredSize = (maxSize[0]*0.9, maxSize[1]*0.9)
Window.size = desiredSize

#-- center the window
Window.left = (maxSize[0] - desiredSize[0])*0.5
Window.top = (maxSize[1] - desiredSize[1])*0.5



##Window.size = (250, 200)
Window.clearcolor = (62 / 255, 17 / 255, 92 / 255, 1)
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
            #19.2 разброс верх67.2 низ48 для 60v   (в твоем случае 36 30 вроде как 6 но хз подогнать надо билд)
            self.charge.text = 'Заряда осталось: ' + str(round((((float(data.replace(',','.'))-48) * 100)/19.2), 2)) + ' % батареи'
            #переменная вычесленного процента заряда чтоб дальше юзать
            percentcharged = str((((float(data.replace(',','.'))-48) * 100)/19.2))
            #по фармуле амперчасы батареи делим на амперы зарядки и умножаем на коэффицент от 1.2 до 1.6 вычисляется экспериментально наблюдением за сколько половина батки зарядится в моем случае 1.45*(21.5\3)
            self.oncharge.text = 'Время на подзарядку: ' + str(round(11.5 - (11.5 * (float(percentcharged)/100)), 2))+ ' часа'
            # экспериментально самик на ходу 4.5 часа умножаем на процент заряда
            self.trip.text = 'Остаточное время пути: ' + str(round( (4.5 * (float(percentcharged)/100)), 2)) + ' часа'
            #экспериментально самик проходит 64км домножаем на процент заряда
            self.distance.text = 'Остаточное расстояние: ' + str(round( (64 * (float(percentcharged)/100)), 2)) + ' км'

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
