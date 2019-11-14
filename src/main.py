from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.uix.screenmanager import FadeTransition, SwapTransition, WipeTransition, SlideTransition
from collections.abc import Iterable
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget

#### Start UP
Window.size = (1024, 600)
from fonts import loadFonts
from circularProgressBar import CircularProgressBar

Builder.load_file('Screens/*.kv')
sm = ScreenManager(transition=FadeTransition())

# DECLARE SCREENS # 


class GrowBox(App):
    def animate(self,dt):
        circProgressBarT = self.root.get_screen('menu').ids.cpT
        circProgressBarH = self.root.get_screen('menu').ids.cpH

        if circProgressBarT.value<circProgressBarT.max:
            circProgressBarT.value+=1
        else:
            circProgressBarT.value=circProgressBarT.min

        if circProgressBarH.value<circProgressBarH.max:
            circProgressBarH.value+=1
        else:
            circProgressBarH.value=circProgressBarH.min

    def build(self):
        Clock.schedule_interval(self.animate, 0.1)
        return sm

def loadScreens():

    global sm
    sm.add_widget(StartScreen(name='start'))
    sm.add_widget(MenuScreen(name='menu'))
    sm.add_widget(MenuScreenDash(name='menudash'))
    sm.add_widget(GraphScreen(name='graph'))
    sm.add_widget(GraphScreenDash(name='graphdash'))
    sm.add_widget(ScheduleScreen(name='schedule'))
    sm.add_widget(ScheduleScreenDash(name='scheduledash'))
    sm.add_widget(TimelapseScreen(name='timelapse'))
    sm.add_widget(TimelapseScreenDash(name='timelapsedash'))
    sm.add_widget(SettingsScreen(name='settings'))
    sm.add_widget(SettingsScreenDash(name='settingsdash'))


if __name__ == '__main__':
    loadFonts()
    loadScreens()
    GrowBox().run()