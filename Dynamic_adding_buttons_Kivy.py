from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridScreen(GridLayout):

    def __init__(self, **kwargs):
        super(GridScreen, self).__init__(**kwargs)

        self.rows = 2
        
        #dictionary which holds all Buttons.
        self.buttons = {}

        for i in range(0,10):
            self.buttons[str(i)] = Button()

        print(self.buttons)
        
        for i in self.buttons:
            self.add_widget(self.buttons[i])

class MyApp(App):

    def build(self):
        self.screen = GridScreen()
        return self.screen
    
if __name__ == '__main__':
    application = MyApp()
    application.run()
