import tkinter as tk
import phrases
import audiobooks
import soundBoard
import music


win=tk.Tk()
win.title("TalkBox")
win.attributes('-fullscreen',True)
win.config(bg="black")




# components

#buttons
phrase= tk.Button(win,text="Phrases/Words",command=phrases,pady=10,padx=10)
audioBook= tk.Button(win,text="Audio Books", command=audiobooks,pady=10,padx=10)
soundboard= tk.Button(win,text="Sound Board", command=soundBoard,pady=10,padx=10)
music=tk.Button(win,text="Music",command=music,padx=10,pady=10)

#arrangment in a grid
phrase.grid(column=0,row=0)
audioBook.grid(column=1,row=0)
soundboard.grid(column=0,row=1)
music.grid(column=1,row=1)




win.mainloop()














