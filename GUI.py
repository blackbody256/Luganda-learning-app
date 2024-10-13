# import kivy module 

import kivy 

    

# this restrict the kivy version i.e 

# below this kivy version you cannot 

# use the app or software 

kivy.require("1.9.1") 

    

# base Class of your App inherits from the App class. 

# app:always refers to the instance of your application 

from kivy.app import App 

    

# creates the button in kivy 

# if not imported shows the error 

from kivy.uix.button import Button

  

# Widgets are elements of a graphical user 

# interface that form part of the User Experience. 

from kivy.uix.widget import Widget

  

  

# Creating a widget class 

# through this we add button 

# the commands of the class is in .kv file 

class Button_Widget(Widget):

  

    def __init__(self, **kwargs):

  

        # Python super() function allows us to

        # refer to the parent class explicitly.

          

        super(Button_Widget, self).__init__(**kwargs)

  

        # creating Button    

        btn1 = Button(text ='Hello World 1', font_size ="15sp",

                   background_color =(1, 1, 1, 1), 

                   color =(1, 1, 1, 1), 

                   # size =(32, 32), 

                   # size_hint =(.2, .2), 

                   pos =(300, 250)) 

  

        # Arranging a callback to a button using

        # bind() function in kivy.

        btn1.bind(on_press = self.callback)

        self.add_widget(btn1)

  

    # callback function tells when button pressed

    # It tells the state and instance of button.

    def callback(self, instance):

        print("Button is pressed")

        print('The button % s state is <%s>' % (instance, instance.state))

  

# create App class 

class ButtonApp(App):

  

    def build(self):

        # return the widget 

        return Button_Widget()

  

# run the App

if __name__ == "__main__":

    ButtonApp().run()

