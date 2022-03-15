from tkinter import filedialog

from search import search,getCorpusesReady
from tkinter import *

# Create the root window
window = Tk()

# Set window title
window.title('Differencing Tool')


# Set window background color
window.config(background = "white")
window.columnconfigure(4, {'minsize': 100})

#variables
tf_idf_var=StringVar(window)
sim_measure_var=StringVar(window)
#lists of choices
tf_idf_measures=['TF','IDF','TF-IDF']
sim_measures=['ED','Jaccard','Dice','PCC','Cosine']

#default
tf_idf_var.set(tf_idf_measures[2])#default is tf-idf
sim_measure_var.set(sim_measures[1]) #deafult is jacc
#dropdowns
tf_idf_menu=OptionMenu(window,tf_idf_var,*tf_idf_measures)
sim_measure_menu=OptionMenu(window,sim_measure_var,*sim_measures)
#main label sim tool
label_file_explorer = Label(window,
                            text = "Search Tool",
                            height = 4,width=110,
                            fg = "white",bg='brown',
                            justify= CENTER,font=('helvetica', 9, 'bold')
                            )
label_enter=Label(window, text="Enter your sequence",
                     width=20,height=4,bg='#ffffff',
                     justify=CENTER)
label_sim=Label(window, text="Choose measures",
                  width=20,height=4,bg='#ffffff',
                  justify=CENTER)
label_results = Label(window,
                            text = "Results",
                            height = 4,width=110,
                            fg = "black",
                            justify= CENTER
                            )
label_seq1 = Label(window,
                      text = "Sequence 1",
                      height = 2,width=100,
                      fg = "black",bg='white',
                      justify= CENTER
                      )
label_seq2 = Label(window,
                   text = "Sequence 2",
                   height = 2,width=100,
                   fg = "black",bg='white',
                   justify= CENTER
                   )
label_seq3 = Label(window,
                   text = "Sequence 3",
                   height = 2,width=100,
                   fg = "black",bg='white',
                   justify= CENTER
                   )
label_R = Label(window,
                   text = "Recall",
                   height = 2,bg='brown',
                   fg = "white",width=20,
                   justify= CENTER,font=('helvetica', 9, 'bold')
                   )
label_R_value = Label(window,
                text = "",
                height = 2,bg='white',
                fg = "black",width=20,
                justify= CENTER,font=('helvetica', 9, 'bold')
                )
label_PR = Label(window,
                text = "Precision",
                height = 2,bg='brown',
                fg = "white",width=20,
                justify= CENTER,font=('helvetica', 9, 'bold')
                )
label_PR_value = Label(window,
                text = "",
                height = 2,bg='white',
                fg = "black",width=20,
                justify= CENTER,font=('helvetica', 9, 'bold')
                )
label_time = Label(window,
                      text = "Searching Time",
                      height = 4,width=110,
                      fg = "black",
                      justify= CENTER
                      )
#entry of seq from user
entry1 = Entry (window,width=70)

#functions
def go():
    valid={'A','C','U','G','R','M','N','S','V'}
    seq=set((entry1.get()).upper())
    if seq.issubset(valid) and len(seq)>0:
        if sim_measure_var.get()=='ED':
            result,r,pr,total_time=(search(entry1.get().upper(),'ED',sim_measure_var.get()))
            result_list=list(result.keys())
            label_seq1.configure(text="1. "+result_list[0])
            label_seq2.configure(text="2. "+result_list[1])
            label_seq3.configure(text="3. "+result_list[2])
            label_R_value.configure(text=str(r))
            label_PR_value.configure(text=str(pr))
            label_time.configure(text="Searching Time: "+str(total_time)+" seconds")
            print("Total time"+str(total_time))
        elif tf_idf_var.get()=='TF':
            print("inside tf")
            result,r,pr,total_time=(search(entry1.get().upper(),'TF',sim_measure_var.get()))
            result_list=list(result.keys())
            label_seq1.configure(text="1. "+result_list[0])
            label_seq2.configure(text="2. "+result_list[1])
            label_seq3.configure(text="3. "+result_list[2])
            label_R_value.configure(text=str(r))
            label_PR_value.configure(text=str(pr))
            label_time.configure(text="Searching Time: "+str(total_time)+" seconds")
            print("Total time"+str(total_time))
        elif tf_idf_var.get()=='IDF':
            print("inside idf")
            result,r,pr,total_time=(search(entry1.get().upper(),'IDF',sim_measure_var.get()))
            result_list=list(result.keys())
            label_seq1.configure(text="1. "+result_list[0])
            label_seq2.configure(text="2. "+result_list[1])
            label_seq3.configure(text="3. "+result_list[2])
            label_R_value.configure(text=str(r))
            label_PR_value.configure(text=str(pr))
            label_time.configure(text="Searching Time: "+str(total_time)+" seconds")
            print("Total time"+str(total_time))
        elif tf_idf_var.get()=='TF-IDF':
            print("inside tf-idf")
            result,r,pr,total_time=(search(entry1.get().upper(),'TF-IDF',sim_measure_var.get()))
            result_list=list(result.keys())
            label_seq1.configure(text="1. "+result_list[0])
            label_seq2.configure(text="2. "+result_list[1])
            label_seq3.configure(text="3. "+result_list[2])
            label_R_value.configure(text=str(r))
            label_PR_value.configure(text=str(pr))
            label_time.configure(text="Searching Time: "+str(total_time)+" seconds")
            print("Total time"+str(total_time))
    else:
        print("Invalid seq")

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("XML files",
                                                        "*.xml*"),
                                                       ("all files",
                                                        "*.*")))
    getCorpusesReady(filename)
    # Change label contents
    # sequences1=parseSequences(filename)
    # sequences=(sequences1)


#button
button_search = Button(window,
                        text = "Search",width=10,
                       bg='brown',fg='white',font=('helvetica', 9, 'bold'),
                       command=go)
button_browse = Button(window,
                        text = "Get Fasta File",
                        command = browseFiles)


label_file_explorer.grid(column = 1, pady=0,row = 1,columnspan=4)
label_enter.grid(column = 1, pady=10,row = 2,columnspan=1)
entry1.grid(column = 2, pady=10,row = 2,columnspan=2)
button_browse.grid(column = 4, pady=10,row = 2,columnspan=1)
label_sim.grid(column = 1, pady=10,row = 3,columnspan=1)
tf_idf_menu.grid(column = 2, pady=10,row = 3,columnspan=1)
sim_measure_menu.grid(column = 3, pady=10,row = 3,columnspan=1)
button_search.grid(column = 4, pady=10,row = 3,columnspan=1)
label_results.grid(column = 1, pady=2,row = 4,columnspan=4)
label_seq1.grid(column = 1, pady=2,row = 5,columnspan=4)
label_seq2.grid(column = 1, pady=2,row = 6,columnspan=4)
label_seq3.grid(column = 1, pady=2,row = 7,columnspan=4)
label_R.grid(column = 1, pady=2,row = 8,columnspan=1)
label_R_value.grid(column = 2, pady=2,row = 8,columnspan=1)
label_PR.grid(column = 3, pady=2,row = 8,columnspan=1)
label_PR_value.grid(column = 4, pady=2,row = 8,columnspan=1)
label_time.grid(column = 1, pady=10,row = 9,columnspan=4)
# Let the window wait for any events
window.mainloop()
