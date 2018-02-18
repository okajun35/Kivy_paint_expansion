# -*- coding: utf-8 -*-

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import ObjectProperty


class MyPaintWidget(Widget):
    #pass
    
    
    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return


        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def clear_canvas(self):
        print("MyPaintWidget clear")
        saved = self.children[:]
        self.clear_widgets()
#        self.canvas.clear()
#        for widget in saved:
#            self.add_widget(widget)
        #self.set_color(self.last_color)

class MyCanbasWidget(Widget):

    def clear_canvas(self):
        print(self.player1)
        #self.painter.canvas.clear()
        MyPaintWidget.clear_canvas(self)


class MyPaintApp(App):
    paint_id = ObjectProperty(None)


    def __init__(self, **kwargs):
        super(MyPaintApp, self).__init__(**kwargs)
        self.title = '画像表示'
        
    def build(self):
        parent = Widget()
        self.painter = MyCanbasWidget()
        #clearbtn = Button(text='Clear')
        #clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        #parent.add_widget(clearbtn)
        return parent


    #def clear_canvas(self, obj):
    def clear_canvas(self):
        print(self.paint_id)
        self.painter.ids['paint_area'].canvas.clear()
#        saved = self.children[:]
#        self.painter.canvas.clear()

#        self.clear_widgets()
#        self.canvas.clear()
#        for widget in saved:
#            self.add_widget(widget)

        #self.player1.clear_canvas()

if __name__ == '__main__':
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')  # 16:9
    MyPaintApp().run()