from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.uix.behaviors import TouchRippleBehavior  
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivymd.uix.card import MDCard
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.resources import resource_find

#Window.size=(dp(1080),dp(1920))

#Builder.load_file("mymd.kv")

class DIALOG_BOX(MDDialog):
    pass


#class Date (MDDatePicker):
 #   def __init__(self,**kwargs):
  #      super().__init__ (**kwargs)
   #     self.ids.calendar.size_hint_y=None
    #    self.ids.calendar.height=dp(200)


#app_image\missal\2023-12-01.txt


class Test(MDApp):
    
    #value=StringProperty()
    #select_date
    #missal=StringProperty("")
    def selec_date(self,instance,value,date_range):
        print("logout---->",str(value))
        try:
            self.filename=f'app_image\\missal\\{value}.txt'
            print(f'logout------>filename is {self.filename}')
            #self.file=open("C:\\Users\\Nnonyelume\\Desktop\\clone\\R@1n.txt")
            #print(self.path)
            self.path= resource_find(self.filename)
            if self.path:
                print(f'logout----->located{resource_find(self.filename)}')
                with open(self.path,"r",encoding="ISO-8859-1") as file:
                    print('logout----->--------------located and file is open------------------')
                    self.missal = file.read()
                    print('logout----->file is read ')
                    self.root.ids.Missal.text=self.missal
                    print('logout----->file is read to MDLabel')
            else:
                #self.dialog_open()
                print('logout----->folder not found and not open ')
                print ('logout----->and error may have occour')
                

            
        except FileNotFoundError:
            pass
              #<-------------------------------------------------------------------------------------
         #   print("No such file or directory")
        #print(f'missal\\{value}.txt')
        


    def dialog_open(self):
        self.dialog = MDDialog(
            text="Not Available..",
            #buttons=[
                #MDFlatButton(
                    #text="CANCEL",
                    #theme_text_color="Custom",
                    #text_color=self.theme_cls.primary_color,
                    #),
                #MDFlatButton(
                    #text="DISCARD",
                    #theme_text_color="Custom",
                    #text_color=self.theme_cls.primary_color,
                    #),
                #],
            )
        self.dialog.open()

    def testing(self):
        self.root.current = "screen c"
        self.root.transition.direction="left"

    def hmm(self, instance):
        value=str(instance.value)
        print(value)
    
    def date(self):
        date_=MDDatePicker()
        date_.adaptive_size= True
        date_.open()
        date_.bind(on_save=self.selec_date)
    
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file("mymd.kv")   #Builder.load_string(KV) #Builder.load_file("mymd.kv")
    def on_start(self):
        pass
    

Test().run()
