from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('spin.kv')

class MiSpinner(Widget):
    def spinner_click(self, value):
        self.ids.click_label.text = f'Ha seleccionado: {value}'
    
class MiApp(App):
    def build(self):
        return MiSpinner()

if __name__ == '__main__':
    MiApp().run()
