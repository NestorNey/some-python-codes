import tkinter as tk

class JoystickButton(tk.Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.width = kw.get("width", 100)
        self.height = kw.get("height", 100)
        self.radius = self.width / 2
        self.bind("<Button-1>", self.move)
        self.bind("<B1-Motion>", self.move)
        self.bind("<ButtonRelease-1>", self.reset)
        self.x = self.radius
        self.y = self.radius
        self.create_oval(0, 0, self.width, self.height, fill="#ccc")
        self.create_oval(self.x - self.radius / 2, self.y - self.radius / 2,
                         self.x + self.radius / 2, self.y + self.radius / 2, fill="#999")

    def move(self, event):
        x, y = event.x, event.y
        distance = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        if distance <= self.radius:
            self.x, self.y = x, y
            self.delete("all")
            self.create_oval(0, 0, self.width, self.height, fill="#ccc")
            self.create_oval(self.x - self.radius / 2, self.y - self.radius / 2,
                             self.x + self.radius / 2, self.y + self.radius / 2, fill="#999")

    def reset(self, event):
        self.x, self.y = self.radius, self.radius
        self.delete("all")
        self.create_oval(0, 0, self.width, self.height, fill="#ccc")
        self.create_oval(self.x - self.radius / 2, self.y - self.radius / 2,
                         self.x + self.radius / 2, self.y + self.radius / 2, fill="#999")

root = tk.Tk()
joystick = JoystickButton(root, width=100, height=100)
joystick.pack(padx=10, pady=10)
root.mainloop()
