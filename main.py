from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex


class CanvasWidget(Widget):
    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return

        with self.canvas:
            Color(*get_color_from_hex('#0080FF80'))
            Line(circle=(touch.x, touch.y, 25), width=4)

    def on_touch_move(self, touch):
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)

    def clear_canvas(self):
        saved = self.children[:]  # See below
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)


class PaintApp(App):
    def build(self):
        return CanvasWidget()


if __name__ == '__main__':

    Config.set('input', 'mouse', 'mouse,disable_multitouch')
    PaintApp().run()
