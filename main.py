import requests, os
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from screen_helper import screenHelper

Config.set('graphics', 'resizeable', True)


class Funcs:
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


class MenuScreen(Screen):
    pass


class TVScreen(Screen, Funcs):
    pass


class P(Screen, FloatLayout):
    pass


class RV(RecycleView):

    @staticmethod
    def get_faves():
        f = open("color_faves.txt", "r")
        faves = f.read()
        faves_list = faves.split("\n")
        f.close()
        return faves_list

    @staticmethod
    def send_fave_request(x, IP):
        x = x.split(", ")

        r = int(float(x[0]) * 255)
        g = int(float(x[1]) * 255)
        b = int(float(x[2]) * 255)
        send_post_request(f"http://{IP}/change?color_R={r}&color_G={g}&color_B={b}")
        LedApp.get_running_app().root.get_screen('tv').ids["color_label"].color = [r / 255, g / 255, b / 255, 1]


class ContentNavigationDrawer(RV):
    nav_drawer = ObjectProperty()


class LedApp(MDApp, ScreenManager):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A200"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screenHelper)
        return screen

    @staticmethod
    def submit_color(colorpicker, IP):
        color = colorpicker.color
        r = color[0]
        g = color[1]
        b = color[2]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        send_post_request(f"http://{IP}/change?color_R={r}&color_G={g}&color_B={b}")

    @staticmethod
    def submit_brigthness(brightness_slider, IP):
        value = int(brightness_slider.value)
        send_post_request(f"http://{IP}/brightness?value={value}")

    @staticmethod
    def set_faves(color_label):
        color = str(color_label.color)
        color = color.split("[")
        color = color[1].split("]")
        color = color[0]
        f = open("color_faves.txt", "a+")
        f.seek(0)
        lines = f.read().splitlines()
        if color in lines:
            show_popup("Farbe schon in Favoriten!")
            return

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


def show_popup(text):
    popup_window = Popup(title="Error", content=Label(text=text), size_hint=(None, None), size=(500, 300))
    popup_window.open()

def send_post_request(route):
    pass
    try:
        requests.post(route)
        # hier neue esps ergänzen
    except:
        show_popup("LED's nicht erreichbar!")

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(TVScreen(name='tv'))


LedApp().run()


#          ================             ||                  ||
#        //                \\           ||                  ||
#       ||                  ||          ||                  ||
#       ||                  ||          ||                  ||
#       ||                  ||          ||                  ||
#       ||                  ||          ||                  ||
#       ||                  ||          ||                  ||
#       ||                  ||          ||                  ||
#       ||                  ||          ||                  ||\
#       ||                  ||          ||                  ||\\
#        \\                //            \\                //  \\
#          ================                ================     \\
