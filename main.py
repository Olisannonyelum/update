import os
import re
from kivymd.app import MDApp 
from kivy.lang import Builder
from threading import Thread
from kivy.clock import Clock
from time import sleep
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFlatButton
from kivy.clock import Clock


class Dialog(Popup):
    pass

#Peter
class myapp(MDApp):
    #    Clock.schedule_once(lambda dt: self.load_text_file(self.path),0)

    def load_text_file(self,path):  
    #try:ISO-8859-1
        
        with open(path,'r',encoding="UTF-8") as file:
            self.chunk_size=100
            while True:
                print(path) 
                self.chunk=file.read(self.chunk_size)
                
                if not self.chunk:
                    break
    def next_screen(self,instance):
        self.dialogBox=Dialog(title=instance.text)
        self.dialogBox.open()
        self.dialogBox.ids.ok.bind(on_press=self.ok)
        self.dialogBox.ids.cancel.bind(on_press=self.cancel)
        self.book_pressed=instance.text
        
        #####LOADING ENGINE########
#######################################################################
    def ok(self,instance):
        self.dialogBox.dismiss()

       #### This enclose block of code handle any wrong entery of vers in the popup ### 
                                    ##widget###
#########################################################################
        self.Chapter=self.dialogBox.ids.chapter.text                    # 
        self.Verse=self.dialogBox.ids.vers.text                         #   
        try:                                                            #
            if self.Chapter=='':                                        #
                pass                                                    #
            else:                                                       #
                self.Chapter=int(self.dialogBox.ids.chapter.text)       #
                                                                        #
            if self.Verse=='':                                          #
                pass                                                    #    
            else:                                                       #
                self.Verse=int(self.dialogBox.ids.vers.text)            #
        except:                                                         #
            pass                                                        #
#########################################################################
        self.To=self.dialogBox.ids.To.text
        #self.To=int(to)
        print(self.To)
        print(type(self.To))


        self.filename=os.path.join(os.path.dirname(__file__),'vers',f'{self.book_pressed}.txt') ### obtainning file name  
        try:
            with open(self.filename,'r',encoding="UTF-8") as bible_book:
                self.bible_content=bible_book.read()###########################
                #print(self.bible_content)
        except:
            print('no shuch file exist')

        Clock.schedule_once(self.Loader,0)
        #self.root.current='2'
        #pass

    def Loader(self,intance):###  this function load the verse in to the bible label
        self.containner=self.get_verses_range()

        self.root.ids.bible.text='\n'.join(self.containner)
        #sleep(1)
        self.root.current='2'
    
###the vers selection engin   ##########
    def get_verses_range(self):
        verse_ =[]
        if self.Chapter=='':
            pass  ##<-----A dialog box should be here 

        try:

            if self.To == '':
                #self.To=0
                #verse_ =[]
                verse = self.get_verse(self.book_pressed, self.Chapter, self.Verse)
                verse_.append(verse)

            else:
                self.To=int(self.dialogBox.ids.To.text)
                for current_verse in range(self.Verse, self.To + 1):
                    verse = self.get_verse(self.book_pressed, self.Chapter, current_verse)
                    verse_.append(verse)

            return verse_

        except:
            pass


    def get_verse(self,book, chapter, verse):## pattern matching engine 
        #try:
        pattern = re.compile(fr"{book} {chapter}:{verse}\s+(.*?)\n", re.DOTALL)
        match = pattern.search(self.bible_content)
        #sleep(3)
        print('detecte',f'{book}',f'{chapter}',f'{verse}')
        if match:
            return match.group()
        else:
            return f"Verse {self.book_pressed} {self.Chapter}:{self.Verse} not found."
       # except:
        #    pass
 ###################


#######################################################################
    def cancel(self,instance):
        self.dialogBox.dismiss()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette='Blue'
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.theme_hue='500'
        return Builder.load_file('mybible.kv')
if __name__ =="__main__":  
    myapp().run()