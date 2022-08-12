import kivy

from kivy.app import App
from kivy.uix.label import Label


# Kivy Version to use
kivy.require('1.11.1')

class HelloWorld(App):
	
	def build(self):
		""" Simple Hello World Label"""
		return Label(text="Hello World!",
                     size_hint=(.5, .5),
                     pos_hint={"center_x": .5, "center_y": .5})


if __name__ == '__main__':
    hw = HelloWorld()
    hw.run()
