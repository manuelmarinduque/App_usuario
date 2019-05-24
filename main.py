from tkinter import Tk
from Interface.Frames import LienzoFrame

root = Tk()

frame = LienzoFrame(root)
frame.construir_menu()
frame.construir_frame()
frame.construir_botones()

root.mainloop()
