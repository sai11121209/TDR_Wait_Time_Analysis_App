import ui,sys
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from matplotlib.dates import DateFormatter
from matplotlib.font_manager import FontProperties
from io import BytesIO

class MyClass(ui.View):
    def __init__(self, waittime, date, Avg, name):
        self.sitepath = [s for s in sys.path if s.endswith('Documents/site-packages')]
        self.fp = FontProperties(fname = f"{self.sitepath[0]}/ipaexg.ttf", size = 14)
        self.waittime = waittime
        self.waittime.reverse()
        self.date = date2num(date)
        self.Avg = Avg
        self.title = name
        self.img = None
        self.make_view()

    def make_view(self):
        self.img = ui.ImageView(frame=(0,0,375,300))
        self.add_subview(self.img)
        self.set_needs_display()

    def draw(self):
        fig = plt.figure(figsize = (6, 5))
        ax = fig.add_subplot(111)
        ax.grid()
        ax.set_xlabel('時刻', fontproperties = self.fp)
        ax.set_ylabel('待ち時間', fontproperties = self.fp)
        ax.set_title(self.title, fontproperties = self.fp)
        ax.axhline(self.Avg, ls = '-', color = 'red')
        ax.plot(self.date,self.waittime)
        plt.autoscale(enable=True, tight=True)
        ax.patch.set_facecolor('black')
        ax.patch.set_alpha(0.6) 
        #plt.legend(loc='upper left', borderaxespad=0, fontsize=18)
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
        plt.ylim(min(self.waittime)-3,max(self.waittime)+3)
        b = BytesIO()
        plt.savefig(b,dpi=600)
        img = ui.Image.from_data(b.getvalue())
        self.img.image = img

if __name__ == '__main__':
    pass
