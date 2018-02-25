# -*- coding: utf-8 -*-

from random import random
from kivy.app import App
from kivy.config import Config

# 起動時の解像度の設定
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')  # 16:9
Config.set('graphics', 'resizable', False)  # ウインドウリサイズ禁止



from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton

from kivy.utils import get_color_from_hex   # 色の16進数表示を可能にする
from kivy.core.window import Window
#:import color kivy.utils.get_color_from_hex


class MyPaintWidget(Widget):
    #pass
    last_color = '' # 画面クリアを押された場合の最後の色
    
    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return


        color = (random(), 1, 1)
        with self.canvas:
            #Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def set_color(self, new_color):
        self.last_color = new_color
        self.canvas.add(Color(*new_color))







class MyCanvasWidget(Widget):

    def clear_canvas(self):
  
        #self.painter.canvas.clear()
        MyPaintWidget.clear_canvas(self)


class MyPaintApp(App):
    paint_id = ObjectProperty(None)


    def __init__(self, **kwargs):
        super(MyPaintApp, self).__init__(**kwargs)
        self.title = '画像表示'
        
    def build(self):
        parent = Widget()
        self.painter = MyCanvasWidget()

        # 起動時の色の設定を行う
        self.painter.ids['paint_area'].set_color(
            get_color_from_hex('#000000'))  #黒色を設定

        #clearbtn = Button(text='Clear')
        #clearbtn.bind(on_release=self.clear_canvas)
        
        #parent.add_widget(self.painter)
        
        #parent.add_widget(clearbtn)
        
        #return parent
        return self.painter

    #def clear_canvas(self, obj):
    def clear_canvas(self):
        # 削除
        #print(self.paint_id)
        self.painter.ids['paint_area'].canvas.clear()
        self.painter.ids['paint_area'].set_color(self.painter.ids['paint_area'].last_color)

#        saved = self.children[:]
#        self.painter.canvas.clear()

#        self.clear_widgets()
#        self.canvas.clear()
#        for widget in saved:
#            self.add_widget(widget)

        #self.player1.clear_canvas()

class ColorButton(ToggleButton):
    def _do_press(self):
        '''
        何も押されていない状態で設定が解除されるのを防ぐためToggleButtonの関数を継承して変更する 
        Source code for kivy.uix.behaviors.button
        https://kivy.org/docs/_modules/kivy/uix/behaviors/button.html
        '''
    
        if self.state == 'normal':
            # ボタンを押されてない場合は状態を変更する
            ToggleButtonBehavior._do_press(self)

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#ffffff')   # ウィンドウの色を白色に変更する
    MyPaintApp().run()