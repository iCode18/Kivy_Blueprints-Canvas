from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.base import EventLoop
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton


class RadioButton(ToggleButton):
    def _do_press(self):
        if self.state == 'normal':
            ToggleButtonBehavior._do_press(self)


class CanvasWidget(Widget):
    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return

        with self.canvas:
            Color(*get_color_from_hex('#0080FF80'))
            touch.ud['current_line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)

    def clear_canvas(self):
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)

    def set_color(self, new_color):
        self.canvas.add(Color(*new_color))


class PaintApp(App):
    def build(self):
        self.canvas_widget = CanvasWidget()
        self.canvas_widget.set_color(
            get_color_from_hex('#2980B9')
        )
        return self.canvas_widget



if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    Config.set('input', 'mouse', 'mouse,disable_multitouch')
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')
    PaintApp().run()
