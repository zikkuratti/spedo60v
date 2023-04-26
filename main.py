import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class Converter(App):

    def build(self):
        Window.clearcolor = (62 / 255, 17 / 255, 92 / 255, 1)
        Window.title = "Конвертер"

        # maximize first, to get the screen size, minus any OS toolbars
        Window.maximize()
        # set the actual window size, to be slightly smaller than full screen
        maxSize = Window.system_size
        desiredSize = (maxSize[0]*0.9, maxSize[1]*0.9)
        Window.size = desiredSize
        # center the window
        Window.left = (maxSize[0] - desiredSize[0])*0.5
        Window.top = (maxSize[1] - desiredSize[1])*0.5

        self.charge = Label(text='Заряда осталось:')
        self.oncharge = Label(text='Время на подзарядку:')
        self.trip = Label(text='Остаточное время пути:')
        self.distance = Label(text='Остаточное расстояние:')
        self.input_data = TextInput(hint_text='How much volts?', multiline=False)
        self.input_data.bind(text=self.on_text)

        box = BoxLayout(orientation='vertical')
        box.add_widget(self.input_data)
        box.add_widget(self.charge)
        box.add_widget(self.oncharge)
        box.add_widget(self.trip)
        box.add_widget(self.distance)

        return box

    def on_text(self, *args):
        data = self.input_data.text

        if data:
            data = float(data.replace(',', '.'))
            percentcharged = ((data - 48) * 100) / 19.2
            self.charge.text = f'Заряда осталось: {percentcharged:.2f} % батареи'

            # амперчасы батареи делим на амперы зарядки и умножаем на коэффицент от 1.2 до 1.6
            charging_time = round(10.75 - (10.75 * (percentcharged/100)), 2)
            self.oncharge.text = f'Время на подзарядку: {datetime.timedelta(hours=charging_time)}'

            # время на ходу 4.5 часа умножаем на процент заряда
            trip_time = round(4.5 * (percentcharged/100), 2)
            self.trip.text = f'Остаточное время пути: {datetime.timedelta(hours=trip_time)}'

            # самокат проходит 64 км, домножаем на процент заряда
            remaining_distance = round(64 * (percentcharged/100), 2)
            self.distance.text = f'Остаточное расстояние: {remaining_distance} км'


if __name__ == "__main__":
    Converter().run()
