from tkinter import *
import datetime as dt

class App:
    def __init__(self):
        self.w = Tk()
        self.w.geometry("400x300")
        
        self.tag =  Label(self.w, text="Hola, ingresa una frase:")
        self.tag.pack(pady=20)

        self.entry = Entry(self.w)
        self.entry.pack(pady=20)

        self.btn = Button(self.w, text="Aceptar", command=self.btn_callback)
        self.btn.pack(pady=20)

        self.output_str = StringVar()
        self.output = Label(self.w, textvariable=self.output_str)
        self.output.pack(pady=20)

    def get_txt(self, entry):
        txt = entry.get()
        return txt

    def set_output(self, txt):
        now = dt.datetime.now()
        self.output_str.set(txt + " - Fecha de hoy: " + str(now.date()))

    def btn_callback(self):
        txt = self.get_txt(self.entry)
        if len(txt) != 0:
            self.set_output(txt)

    def run(self):
        self.w.mainloop()


app = App()
app.run()