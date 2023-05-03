import tkinter as tk
import math

class JoystickButton:
    def __init__(self, parent):
        self.parent = parent
        self.width = 200
        self.height = 200
        self.center = (self.width // 2, self.height // 2)
        self.radius = self.width // 2 - 20
        self.speed = 0
        self.direction = 0
        
        self.canvas = tk.Canvas(self.parent, width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.bind('<B1-Motion>', self.move_joystick)
        self.canvas.bind('<ButtonRelease-1>', self.reset_joystick)

        self.joystick = self.canvas.create_oval(self.center[0] - self.radius,
                                                self.center[1] - self.radius,
                                                self.center[0] + self.radius,
                                                self.center[1] + self.radius,
                                                fill='blue')

        self.info_label = tk.Label(self.parent, text='X: 0, Y: 0, Speed: 0')
        self.info_label.pack()

    def move_joystick(self, event):
        x, y = event.x, event.y
        dist = math.sqrt((x - self.center[0])**2 + (y - self.center[1])**2)
        if dist > self.radius:
            x = self.center[0] + (x - self.center[0]) * self.radius / dist
            y = self.center[1] + (y - self.center[1]) * self.radius / dist
            dist = self.radius
        self.canvas.coords(self.joystick, x - 10, y - 10, x + 10, y + 10)

        x_diff = x - self.center[0]
        y_diff = self.center[1] - y
        self.direction = math.atan2(y_diff, x_diff)
        self.speed = int(dist / self.radius * 100)

        self.info_label.config(text='X: {}, Y: {}, Speed: {}'.format(x - self.center[0], self.center[1] - y, self.speed))

    def reset_joystick(self, event):
        self.canvas.coords(self.joystick, self.center[0] - 10, self.center[1] - 10, self.center[0] + 10, self.center[1] + 10)
        self.speed = 0
        self.direction = 0
        self.info_label.config(text='X: 0, Y: 0, Speed: 0')

root = tk.Tk()
joystick = JoystickButton(root)
root.mainloop()
