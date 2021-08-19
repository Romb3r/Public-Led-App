import requests, os
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from screen_helper import screenHelper


class MenuScreen(Screen):
    pass


class WohnzimmerScreen(Screen):
    def change_color(self, colorpicker):
        if colorpicker.color == [1, 0.8, 0.19999999999999996, 1] or colorpicker.color == [0, 0, 0, 0]:
            pass
        else:
            self.ids["color_label"].color = colorpicker.color

    def change_brightness_led(self, colorpicker, brightness_slider):
        color = colorpicker.color
        value = int(brightness_slider.value)
        r = color[0]
        g = color[1]
        b = color[2]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        percent = 100 * value / 255
        percent = percent / 100
        r = r * percent
        g = g * percent
        b = b * percent

        r = int(r) / 255
        g = int(g) / 255
        b = int(b) / 255

        self.ids["color_label"].color = [r, g, b, 1]


class SchlafzimmerScreen(Screen):
    def change_color(self, colorpicker):
        if colorpicker.color == [1, 0.8, 0.19999999999999996, 1] or colorpicker.color == [0, 0, 0, 0]:
            pass
        else:
            self.ids["color_label"].color = colorpicker.color

    def change_brightness_led(self, colorpicker, brightness_slider):
        color = colorpicker.color
        value = int(brightness_slider.value)
        r = color[0]
        g = color[1]
        b = color[2]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        percent = 100 * value / 255
        percent = percent / 100
        r = r * percent
        g = g * percent
        b = b * percent

        r = int(r) / 255
        g = int(g) / 255
        b = int(b) / 255

        self.ids["color_label"].color = [r, g, b, 1]


class KuecheScreen(Screen):
    def change_color(self, colorpicker):
        if colorpicker.color == [1, 0.8, 0.19999999999999996, 1] or colorpicker.color == [0, 0, 0, 0]:
            pass
        else:
            self.ids["color_label"].color = colorpicker.color

    def change_brightness_led(self, colorpicker, brightness_slider):
        color = colorpicker.color
        value = int(brightness_slider.value)
        r = color[0]
        g = color[1]
        b = color[2]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        percent = 100 * value / 255
        percent = percent / 100
        r = r * percent
        g = g * percent
        b = b * percent

        r = int(r) / 255
        g = int(g) / 255
        b = int(b) / 255

        self.ids["color_label"].color = [r, g, b, 1]


class RV(RecycleView):

    def get_faves(self):
        f = open("color_faves.txt", "r")
        faves = f.read()
        faves_list = faves.split("\n")
        f.close()
        return faves_list

    def send_fave_request(self, x, IP):
        x = x.split(", ")

        r = int(float(x[0]) * 255)
        g = int(float(x[1]) * 255)
        b = int(float(x[2]) * 255)

        requests.post(f"http://{IP}/change?color_R={r}&color_G={g}&color_B={b}")


class Faves_Schlafzimmer(Screen):
    pass

class Faves_Wohnzimmer(Screen):
    pass

class Faves_Kueche(Screen):
    pass

class P(Screen, FloatLayout):
    pass


class LedApp(MDApp, ScreenManager):

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screenHelper)
        return screen

    def submit_color(self, colorpicker, IP):
        color = colorpicker.color
        r = color[0]
        g = color[1]
        b = color[2]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        requests.post(f"http://{IP}/change?color_R={r}&color_G={g}&color_B={b}")


    def submit_brigthness(self, brightness_slider, IP):
        value = int(brightness_slider.value)
        requests.post(f"http://{IP}/brightness?value={value}")


    def set_faves(self, color_label):
        color = str(color_label.color)
        color = color.split("[")
        color = color[1].split("]")
        color = color[0]
        f = open("color_faves.txt", "a+")
        f.seek(0)
        lines = f.read().splitlines()
        if color in lines:
            return
        else:
            if os.stat("color_faves.txt").st_size != 0:
                f.write("\n" + color)
                f.close()
            else:
                f.write(color)
                f.close()


def hex_to_rgb(hex):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i + 2], 16)
        rgb.append(decimal)

    return tuple(rgb)


def show_popup(IP):
    show = P()
    if IP == "192.168.178.26":
        popup_window = Popup(title="Error Wohnzimmer", content=show, size_hint=(None, None), size=(300, 100))
    else:
        popup_window = Popup(title="Error wo anders", content=show, size_hint=(None, None), size=(300, 100))

    popup_window.open()


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(WohnzimmerScreen(name='wohnzimmer'))
sm.add_widget(SchlafzimmerScreen(name='schlafzimmer'))
sm.add_widget(KuecheScreen(name='kueche'))
sm.add_widget(Faves_Wohnzimmer(name='faves_wohnzimmer'))
sm.add_widget(Faves_Schlafzimmer(name='faves_schlafzimmer'))
sm.add_widget(Faves_Kueche(name='faves_kueche'))




LedApp().run()