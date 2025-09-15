import downloader as dw
from tkinter import ttk
import tkinter 
import sv_ttk
class Window ():
   

    def __init__(self):
         self.Title="Descarga tus videos favoritos"
         self.BackgroundColor="gray20"
         
        
         root =tkinter.Tk()
         root.title(self.Title)
         
         screen_width = root.winfo_screenwidth()
         screen_height = root.winfo_screenheight()
         root.geometry(f"{screen_width-5}x{screen_height}+0+0")

         root.config(bg=self.BackgroundColor)
         entry=ttk.Entry(root,justify="left",width=70, font=("Arial",20))
         entry.pack(pady=70)
        
         button=ttk.Button(root,width=35, text="Descargar", command=lambda:dw.Download(entry.get()))
         button.pack()
         sv_ttk.set_theme("dark")
         root.mainloop()

Window()