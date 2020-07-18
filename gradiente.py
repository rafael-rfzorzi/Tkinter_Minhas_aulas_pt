from tkinter import *

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        f1 = GradientFrame(self, "#535b80","gray", borderwidth=1, relief="sunken")
        f2 = GradientFrame(self, "gray", "#535b80", borderwidth=1, relief="sunken")
        f1.pack(side="top", fill="both", expand=True)
        f2.pack(side="bottom", fill="both", expand=True)

class GradientFrame(Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="red", color2="black", **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")

if __name__ == "__main__":
    root = Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()