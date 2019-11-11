from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt


Window.clearcolor = (1, 1, 1, 1)
btns = ["-2", "-1", " 0", "+1", "+2", "+3"]
scores = [Label(text="[color=000] "+str(i+1)+"[/color]"+"\n\n", markup=True) for i in range(18)]
totalScore = Label(text="0", color=[0, 0, 0, 1], font_size="50dp")
count = 0
chartinfo = [0, 0, 0]
plt.pie(chartinfo, labels=chartinfo)
chart = FigureCanvasKivyAgg(plt.gcf())



def addScore(instance):
	global chartinfo
	global chart
	global count
	global totalScore
	if count < 18:
		if int(instance.text) < 0:
			clr = "005dff"
			chartinfo[0] += 1
		elif int(instance.text) > 0:
			clr = "ff0000"
			chartinfo[2] += 1
		else:
			clr = "00971c"
			chartinfo[1] += 1

		scores[count].text += "[color="+clr+"]"+instance.text+"[/color]"
		totalScore.text = str(int(totalScore.text)+int(instance.text))
		if int(totalScore.text) > 0:
			totalScore.text = "+"+totalScore.text
		count += 1

		plt.clf()
		plt.pie(chartinfo, labels=["UNDER", "PAR", "OVER"], colors=["gray"],
				autopct="%1.f%%", explode=(0.02, 0.02, 0.02))
		chart.draw()


	else:
		pass


class MasterLayout(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		self.rows = 3
		self.add_widget(TulosLayout())
		self.add_widget(InfoLayout())
		self.add_widget(NappiLayout())

class NappiLayout(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 3
		self.rows = 2
		for btn in btns:
			nappi = Button(text=btn)
			nappi.bind(on_press=addScore)
			self.add_widget(nappi)


class TulosLayout(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 9
		self.rows = 2


		for score in scores:
			self.add_widget(score)


class InfoLayout(GridLayout):
	def __init__(self, **kwargs):
		global totalScore
		global chart
		super().__init__(**kwargs)
		self.cols = 2
		self.rows = 1
		self.add_widget(totalScore)
		self.add_widget(chart)


class Fbg(App):
	def build(self):
		return MasterLayout()

if __name__ == "__main__":
	Fbg().run()
