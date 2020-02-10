import ui
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

class MyClass(ui.View):
    def __init__(self, p1=1, p2=2, p3=3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.img = None
        self.make_view()

    def make_view(self):

        slider1 = ui.Slider(x=0, y=self.height-32 , width=self.bounds.width,
                            value=self.y, action=self.slider_action)
        self.add_subview(slider1)
        self.img = ui.ImageView(frame=self.bounds.inset(30, 30))
        self.add_subview(self.img)
        self.set_needs_display()

    def draw(self):
        # called by ui Module when set_needs_display() is called.
        # as per the docs you should not call this method yourself.
        plt.plot([self.p1, self.p2, self.p3])
        b = BytesIO()
        plt.savefig(b)
        img = ui.Image.from_data(b.getvalue())
        self.img.image = img

    def slider_action(self, sender):
        self.p1 *= sender.value+1
        self.p2 *= sender.value+2
        self.p3 *= sender.value+3
        self.set_needs_display()

if __name__ == '__main__':
    f = (0, 0, 400, 400)
    mc= MyClass(frame=f, name='*** WTF ***')
    mc.present('sheet')
