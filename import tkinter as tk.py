import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.color = "black"
        self.pen_width = 2

        self.setup_toolbar()

        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.stop_paint)

    def setup_toolbar(self):
        self.toolbar = tk.Frame(self.root)

        color_label = tk.Label(self.toolbar, text="Color:")
        color_label.pack(side=tk.LEFT)

        color_var = tk.StringVar()
        self.color_menu = tk.OptionMenu(self.toolbar, color_var, "black", "red", "blue", "green")
        self.color_menu.pack(side=tk.LEFT)
        color_var.trace("w", self.change_color)

        width_label = tk.Label(self.toolbar, text="Width:")
        width_label.pack(side=tk.LEFT)

        width_var = tk.StringVar()
        self.width_menu = tk.OptionMenu(self.toolbar, width_var, "2", "4", "6", "8")
        self.width_menu.pack(side=tk.LEFT)
        width_var.trace("w", self.change_width)

        self.toolbar.pack(side=tk.TOP, fill="both")

    def start_paint(self, event):
        self.x, self.y = event.x, event.y
        self.draw = True

    def paint(self, event):
        if self.draw:
            x1, y1 = (self.x, self.y)
            x2, y2 = (event.x, event.y)
            self.canvas.create_line(x1, y1, x2, y2, fill=self.color, width=self.pen_width)
            self.x, self.y = x2, y2

    def stop_paint(self, event):
        self.draw = False

    def change_color(self, *args):
        self.color = self.color_menu.var.get()

    def change_width(self, *args):
        self.pen_width = int(self.width_menu.var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()