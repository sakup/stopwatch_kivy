import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.clock import Clock


kivy.config.Config.set('graphics', 'width', '450')
kivy.config.Config.set('graphics', 'height', '600')

class Root(BoxLayout):

    time = NumericProperty()
    running = False

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)


    def increment_time(self, interval):
        self.time += 1
        # print (self.time)

    def start_time(self):
        print ('START')
        running = True
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)
        self.increment_time(0)

    def stop_time(self):
        print ('STOP')
        Clock.unschedule(self.increment_time)

    def reset_time(self):
        global time
        print ('RESET')
        Clock.unschedule(self.increment_time)
        self.time = 0


    def format(self, data):
        # a = int(self.time) / 600
        # b = ((int(t) / 10) % 60) /10
        # c = ((int(t) / 10) % 60) % 10
        d = (int(self.time) % 60) % 10
        # return str(a) + ":" + str(b) + str(c) + "." + str (d)
        return d

class StopwatchApp(App):

    def build(self):
        watch = Root()
        # Clock.schedule_interval(watch.update(), 1/99)
        return watch

StopwatchApp().run()
