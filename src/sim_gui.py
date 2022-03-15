from main import parseSequences
from tkinter import *
from set_based import jaccSim,dice,intersectSim
from vector_based import PCC,cosineSim
from tkinter import filedialog
from all_path import jaccSimPath,path_based,diceSimPath,intersectSimPath,cosSimPath,PCCPath
from time_stamps import calculateTime,calculateWagner
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
# Create the root window
window = Tk()

# Set window title
window.title('Similarity Tool')

# # Set window size
# window.geometry("700x500")

# Set window background color
window.config(background = "white")
window.columnconfigure(3, {'minsize': 100})

#variables
approach=StringVar(window)
model=StringVar(window)
set_measure_var=StringVar(window)
vector_measure_var=StringVar(window)

#lists to be used of choices
options_approach=['tag-based','path-based']
options_model=['set-based','vector-based']
set_measure=['Jaccard','Dice','Intersection']
vector_measure=['PCC','Cosine']

#default
approach.set(options_approach[0]) #default is tag
model.set(options_model[0]) #default is set
set_measure_var.set(set_measure[0])#deafult is jaccard
vector_measure_var.set(vector_measure[0])#default is PCC

#main label sim tool
label_file_explorer = Label(window,
                            text = "Similarity Tool",
                            height = 4,width=100,
                            fg = "white",bg='brown',
                            justify= CENTER,font=('helvetica', 9, 'bold')
                            )
label_approach=Label(window, text="Choose approach and similarity measure",
                     width=100,height=4,
                     justify=CENTER)
label_compute=Label(window, text="Press the below button to compute sim",
                     width=100,height=4,
                     justify=CENTER)
label_sim=Label(window, text="Similarity: Not Calculated Yet",
                width=100,height=4,
                justify=CENTER)
#radio buttons
radio_tag=Radiobutton(window,
                      text=options_approach[0],
                      variable=approach, bg='#fff',
                      value=options_approach[0])
radio_path=Radiobutton(window,
                  text=options_approach[1],
                  variable=approach,bg='#fff',
                  value=options_approach[1])
radio_set=Radiobutton(window,
                       text=options_model[0],
                       variable=model,bg='#fff',
                       value=options_model[0])
radio_vector=Radiobutton(window,
                      text=options_model[1],
                      variable=model,bg='#fff',
                      value=options_model[1])

#drop downs
set_measure_menu=OptionMenu(window, set_measure_var, *set_measure)
vector_measure_menu=OptionMenu(window, vector_measure_var, *vector_measure)

# functions to be used with buttons
def browseFiles():
    global sequences
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("XML files",
                                                        "*.xml*"),
                                                       ("all files",
                                                        "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: ")
    sequences1=parseSequences(filename)
    sequences=(sequences1)

def createNewWindow():
    newWindow = Toplevel(window)
    newWindow.wm_title("Comparison Graph")
    xAxis=list(range(99))
    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    time_stamps,measure=calculateTime(approach.get(),model.get(),set_measure_var.get(),vector_measure_var.get())
    wagTime=calculateWagner()
    fig.add_subplot(111).plot(xAxis,time_stamps,xAxis,wagTime)
    fig.legend([str(measure),'TED'])
    canvas = FigureCanvasTkAgg(fig, master=newWindow)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, newWindow)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


def compute():
    global sim;
    if approach.get()=="tag-based":
        if model.get()=="set-based":
            if set_measure_var.get()=="Jaccard":
                print("You are inside jacc")
                sim=jaccSim(sequences[0],sequences[1])
                label_sim.configure(text="Similarity: "+str(sim))
            elif set_measure_var.get()=="Dice":
                print("You are inside dice")
                sim=dice(sequences[0],sequences[1])
                label_sim.configure(text="Similarity: "+str(sim))
            elif set_measure_var.get()=="Intersection":
                print("You are inside intersection")
                sim=intersectSim(sequences[0],sequences[1])
                label_sim.configure(text="Similarity: "+str(sim))
        elif model.get()=='vector-based':
            if vector_measure_var.get()=="PCC":
                print("You are inside PCC")
                sim=PCC(sequences[0],sequences[1])
                label_sim.configure(text="Similarity: "+str(sim))
            elif vector_measure_var.get()=="Cosine":
                print("You are inside cosine")
                sim=cosineSim(sequences[0],sequences[1])
                label_sim.configure(text="Similarity: "+str(sim))
    if approach.get()=='path-based':
        seq1=path_based(sequences[0])
        seq2=path_based(sequences[1])
        if model.get()=='set-based':
            if set_measure_var.get()=="Jaccard":
                print("You are inside jacc")
                sim=jaccSimPath(seq1,seq2)
                label_sim.configure(text="Similarity: "+str(sim))
            elif set_measure_var.get()=="Dice":
                print("You are inside dice")
                sim=diceSimPath(seq1,seq2)
                label_sim.configure(text="Similarity: "+str(sim))
            elif set_measure_var.get()=="Intersection":
                print("You are inside intersection")
                sim=intersectSimPath(seq1,seq2)
                label_sim.configure(text="Similarity: "+str(sim))
        if model.get()=='vector-based':
            if vector_measure_var.get()=='Cosine':
                print("You are inside cosine")
                sim=cosSimPath(seq1,seq2)
                label_sim.configure(text="Similarity: "+str(sim))
            if vector_measure_var.get()=='PCC':
                print("You are inside pcc")
                sim=PCCPath(seq1,seq2)
                label_sim.configure(text="Similarity: "+str(sim))

# Buttons
button_explore = Button(window,
                        text = "Get Sequences",
                        command = browseFiles)
button_compute = Button(window,
                        text = "Compute",
                        command = compute)
button_view = Button(window,
                        text = "View Graph",
                        command = createNewWindow)
#grid
label_file_explorer.grid(column = 1, pady=10,row = 1,columnspan=3)
button_explore.grid(column = 1, pady=10,row = 2,columnspan=3)
label_approach.grid(column = 1, pady=10,row = 3,columnspan=3)
radio_tag.grid(column = 1, pady=10, row = 4, columnspan=1)
radio_path.grid(column = 1, pady=10, row = 5, columnspan=1)
radio_set.grid(column = 2, pady=10, row = 4, columnspan=1)
radio_vector.grid(column = 2, pady=10, row = 5, columnspan=1)
set_measure_menu.grid(column = 3, pady=10, row = 4, columnspan=1)
vector_measure_menu.grid(column = 3, pady=10, row = 5, columnspan=1)
label_compute.grid(column = 1, pady=10,row = 7,columnspan=3)
button_compute.grid(column = 1, pady=10,row = 8,columnspan=3)
label_sim.grid(column = 1, pady=10,row = 9,columnspan=3)
button_view.grid(column = 1, pady=10,row = 10,columnspan=3)
# Let the window wait for any events
window.mainloop()
