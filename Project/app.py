from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang  import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineIconListItem
from kivymd.uix.relativelayout import MDRelativeLayout

Window.size = (300,500)


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class ContentNavigationDrawer(MDBoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )
class AITrainer(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.material_style = "M3"

        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("getstarted.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("main_page.kv"))
        return screen_manager
    
if __name__ =="__main__":
    LabelBase.register(name="MPoppins", fn_regular="Roboto-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="Roboto-Bold.ttf")
    AITrainer().run()