import time
import webbrowser
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from FileShare import FileShare
from kivy.core.clipboard import Clipboard

Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
        """ Start the camera """
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """ Stop the camera """
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        """ Capture the image from camera"""
        current_time = time.strftime("%Y%m%d%H%M%S")
        self.filepath = f"imageFiles/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath

class ImageScreen(Screen):
    link_msg = "Create a Link first"
    def create_link(self):
        """ Create a link to the image"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        file_share = FileShare(file_path)
        self.url = file_share.share()
        self.ids.link_label.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link_label.text = self.link_msg

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link_label.text = self.link_msg

class RootWidget(ScreenManager):
    pass

class BaseApp(App):

    def build(self):
        return RootWidget()

BaseApp().run()