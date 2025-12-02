from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from Project3_PhotoSearch.CommonUtils import CommonUtils

Builder.load_file('frontend.kv')
common_utils = CommonUtils()

class FirstScreen(Screen):
    def search_image(self):
        query = self.manager.current_screen.ids.user_query.text
        image_url = common_utils.get_image(query)
        common_utils.download_image(image_url)
        self.manager.current_screen.ids.img.source = "files/output_file.jpg"

class RootWidget(ScreenManager):
    pass

class BaseApp(App):

    def build(self):
        return RootWidget()