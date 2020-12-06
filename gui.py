import tkinter as tk
import tkinter.ttk as ttk


# Create a list of checkboxes
class Checkbar(tk.Frame):
    def __init__(self, parent=None, picks=[] ):
        tk.Frame.__init__(self, parent)
        self.vars = []
        for idx, pick in enumerate(picks):
            var = tk.IntVar()
            chk = tk.Checkbutton(self, text=pick, variable=var)

            chk.pack(side="top",anchor="w")

            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)







####################################### Definition ############################################

#Define Root
root = tk.Tk()
root.title("Storygenerator")
root.minsize(width="250", height="430")
root.maxsize(width="250", height="430")

#Define Tabs
tab_parent = ttk.Notebook(root)
t_main = tk.Frame(tab_parent)
t_settings = tk.Frame(tab_parent)

# Defines Frames
#Entrygrid
f_entry = tk.Frame(t_main, relief='ridge')
f_entrylabels = tk.Frame(f_entry,relief="ridge")
f_entryfields = tk.Frame(f_entry,relief="ridge")
f_entrybutton = tk.Frame(f_entry,relief="ridge")
#Componentgrid
f_components = tk.Frame(t_main, relief='ridge')
f_complabels = tk.Frame(f_components, relief='ridge')
f_compcheck = tk.Frame(f_components, relief='ridge')
#Issuegrid
f_issues = tk.Frame(t_main, relief='ridge')
f_issueslabels= tk.Frame(f_issues, relief='ridge')
f_issuescheck= tk.Frame(f_issues, relief='ridge')

# Define Label
l_issueID = tk.Label(f_entrylabels, text="IssueID:")
l_summary = tk.Label(f_entrylabels, text="Summary:")
l_epiclink = tk.Label(f_entrylabels, text="Epic Link:")
l_labels = tk.Label(f_entrylabels, text="Labels:")
l_component = tk.Label(f_complabels, text="Component/s:")
l_createissue = tk.Label(f_issueslabels, text="Create Issue:")
l_reporter = tk.Label(f_entrylabels, text="Reporter:")
l_assignee = tk.Label(f_entrylabels, text="Assignee:")

# Define Inpufield
e_issueID = tk.Entry(f_entryfields)
e_summary = tk.Entry(f_entryfields)
e_epiclink = tk.Entry(f_entryfields)
e_labels = tk.Entry(f_entryfields)
e_reporter = tk.Entry(f_entryfields)
e_assignee = tk.Entry(f_entryfields)


# Define Button
b_load = tk.Button(f_entrybutton, text='Load Issue')
b_addLabel = tk.Button(f_entrybutton,text='Add Label')
b_generateIssues = tk.Button(t_main,text='Generate Issues')


# Define Checkbox
chk_columns = Checkbar(f_compcheck, ["CMN", "AMS", "CF"])
chk_issues = Checkbar(f_issuescheck, ["Analysis", "Prep Business", "Prep Testdata", "Order"])


####################################### Initialise ############################################

#Tab
tab_parent.add(t_main,text="Issuegenerator")
tab_parent.add(t_settings,text="Settings")
tab_parent.grid(row=0, column=0, sticky="nsew")

# Frame
f_entry.grid(row=1, column=0, sticky="nsew")
f_entrylabels.grid(row=0, column=0,sticky="w")
f_entryfields.grid(row=0, column=1,sticky="w")
f_entrybutton.grid(row=0, column=2,sticky="wn")
f_components.grid(row=2, column=0, sticky="nsew")
f_complabels.grid(row=0, column=0, sticky="nsew")
f_compcheck.grid(row=1, column=1,columnspan=2, sticky="nsew")
f_issues.grid(row=3, column=0, sticky="nsew")
f_issueslabels.grid(row=0, column=0, sticky="nsew")
f_issuescheck.grid(row=1, column=1,columnspan=2, sticky="nsew")

# Labels
l_issueID.pack()
l_summary.pack()
l_epiclink.pack()
l_labels.pack()
l_component.pack()
l_createissue.pack()
l_reporter.pack()
l_assignee.pack()

# Inpufields
e_issueID.pack()
e_summary.pack()
e_epiclink.pack()
e_labels.pack()
e_reporter.pack()
e_assignee.pack()

# Buttons
b_load.grid(row=0,column=0)
b_addLabel.grid(row=5,column=0,pady=30)
b_generateIssues.grid()

# Checkbox
chk_columns.pack()
chk_issues.pack()

# loop root
root.mainloop()
