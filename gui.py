"""
Inputbar Class erstellt, als nächstes muss
der entry type erstellt werden 
"""

import tkinter as tk
import tkinter.ttk as ttk

# Create variables
all_label = []


# Create a list of checkboxes
class Checkbar(tk.Frame):
    def __init__(self, parent=None, picks=[]):
        tk.Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = tk.IntVar()
            chk = tk.Checkbutton(self, text=pick, variable=var)
            chk.pack(side="top", anchor="w")
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)

# Create a list of checkboxes
class Inputbar(tk.Frame):
    def __init__(self, parent=None, picks=[]):
        tk.Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = tk.StringVar()
            var = tk.Label(self, text=pick)
            var.pack(side="top", anchor="w")
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)

# Create dynamicall Entryfields
def add_label_entry():
    lbl = tk.Label(f_entryLabel, text="Label:")
    lbl.pack()
    ent = tk.Entry(f_entryfields)
    ent.pack()
    all_label.append(ent)


####################################### Definition ############################################
# Define Root
root = tk.Tk()
root.title("Storygenerator")
root.minsize(width="250", height="430")
#root.maxsize(width="250", height="430")

# Define Tabs
tab_parent = ttk.Notebook(root)
t_main = tk.Frame(tab_parent)
t_settings = tk.Frame(tab_parent)

# Defines Frames
# Entrygrid
f_entry = tk.Frame(t_main, relief='ridge')
f_entryLabel = tk.Frame(f_entry, relief="ridge")
f_entryfields = tk.Frame(f_entry, relief="ridge")
f_entrybutton = tk.Frame(f_entry, relief="ridge")
# Componentgrid
f_components = tk.Frame(t_main, relief='ridge')
f_compLabel = tk.Frame(f_components, relief='ridge')
f_compcheck = tk.Frame(f_components, relief='ridge')
# Issuegrid
f_issues = tk.Frame(t_main, relief='ridge')
f_issuesLabel = tk.Frame(f_issues, relief='ridge')
f_issuescheck = tk.Frame(f_issues, relief='ridge')

# Define Label
l_issueID = tk.Label(f_entryLabel, text="IssueID:")
l_summary = tk.Label(f_entryLabel, text="Summary:")
l_epiclink = tk.Label(f_entryLabel, text="Epic Link:")
l_reporter = tk.Label(f_entryLabel, text="Reporter:")
l_assignee = tk.Label(f_entryLabel, text="Assignee:")
l_label = tk.Label(f_entryLabel, text="Label:")
l_component = tk.Label(f_compLabel, text="Component/s:")
l_createissue = tk.Label(f_issuesLabel, text="Create Issue:")

# Define Inputfield variables
varIssueID = tk.StringVar()
varSummary = tk.StringVar()
varEpiclink = tk.StringVar()
varReporter = tk.StringVar()
varAssignee = tk.StringVar()

# Define Inpufield
e_issueID = tk.Entry(f_entryfields, textvariable=varIssueID)
e_summary = tk.Entry(f_entryfields, textvariable=varSummary,
                     state='readonly')
e_epiclink = tk.Entry(
    f_entryfields, textvariable=varEpiclink, state='readonly')
e_reporter = tk.Entry(f_entryfields, textvariable=varReporter)
e_assignee = tk.Entry(f_entryfields, textvariable=varAssignee)
e_Label = tk.Entry(f_entryfields)

# add first label to array
all_label.append(e_Label)

# Define Button
b_load = tk.Button(f_entrybutton, text='Load Issue')
b_addLabel = tk.Button(f_entrybutton, text='Add Label',
                       command=add_label_entry)
b_generateIssues = tk.Button(t_main, text='Generate Issues')

# Define Checkbox
chk_columns = Checkbar(f_compcheck, ["CMN", "AMS", "CF"])
chk_issues = Checkbar(
    f_issuescheck, ["Analysis", "Prep Business", "Prep Testdata", "Order"])

ent_fields = Inputbar(f_entryLabel, ["DynLabel1","DynLabel2"])

####################################### Initialise ############################################
# Tab
tab_parent.add(t_main, text="Issuegenerator")
tab_parent.add(t_settings, text="Settings")
tab_parent.grid(row=0, column=0, sticky="nsew")

# Frame
f_entry.grid(row=1, column=0, sticky="nsew")
f_entryLabel.grid(row=0, column=0, sticky="w")
f_entryfields.grid(row=0, column=1, sticky="w")
f_entrybutton.grid(row=0, column=2, sticky="wn")
f_components.grid(row=2, column=0, sticky="nsew")
f_compLabel.grid(row=0, column=0, sticky="nsew")
f_compcheck.grid(row=1, column=1, columnspan=2, sticky="nsew")
f_issues.grid(row=3, column=0, sticky="nsew")
f_issuesLabel.grid(row=0, column=0, sticky="nsew")
f_issuescheck.grid(row=1, column=1, columnspan=2, sticky="nsew")

# Label
l_issueID.pack()
l_summary.pack()
l_epiclink.pack()
l_reporter.pack()
l_assignee.pack()
l_component.pack()
l_createissue.pack()
l_label.pack()

# Inpufields
e_issueID.pack()
e_summary.pack()
e_epiclink.pack()
e_reporter.pack()
e_assignee.pack()
e_Label.pack()


# Buttons
b_load.grid(row=0, column=0)
b_addLabel.grid(row=2, column=0)
b_generateIssues.grid()

# Checkbox
chk_columns.pack()
chk_issues.pack()
ent_fields.pack()

# loop root
root.mainloop()
