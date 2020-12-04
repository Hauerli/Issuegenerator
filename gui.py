import tkinter as tk


# Create a list of checkboxes
class Checkbar(tk.Frame):
    def __init__(self, parent=None, picks=[], ):
        tk.Frame.__init__(self, parent)
        self.vars = []

        cnt = 0

        for pick in picks:
            if cnt == 2:
                cnt = 0
            var = tk.IntVar()
            chk = tk.Checkbutton(self, text=pick, variable=var)
            chk.grid(row=1, column=cnt)
            self.vars.append(var)
            cnt+=1
    def state(self):
        return map((lambda var: var.get()), self.vars)


window = tk.Tk()
window.title("Storygenerator")

# Define Label
l_issueID = tk.Label( text="IssueID:")
l_summary = tk.Label( text="Summary:")
l_epiclink = tk.Label( text="Epic Link:")
l_labels = tk.Label( text="Labels:")
l_component = tk.Label( text="Component/s:")
l_createissue = tk.Label( text="Create Issue:")
l_reporter = tk.Label( text="Reporter:")
l_assignee = tk.Label( text="Assignee:")

# Define Inpufield
e_issueID = tk.Entry()
e_summary = tk.Entry()
e_epiclink = tk.Entry()
e_labels = tk.Entry()
e_reporter = tk.Entry()
e_assignee = tk.Entry()

# Define Button
b_load = tk.Button( text='Load Issue')
b_addLabel = tk.Button( text='Add Label')
b_pushIssues = tk.Button( text='Generate Issues')


# Define Checkbox
chk_columns = Checkbar(window, ["CMN", "AMS", "CF", "SF"])
chk_issues = Checkbar(window,["Analysis","Prep Business","Prep Testdata","Order"])


# Initialise
# Labels
l_issueID.grid(row=0, column=0, padx=5, pady=5)
l_summary.grid(row=1, column=0, padx=5, pady=5)
l_epiclink.grid(row=2, column=0, padx=5, pady=5)
l_labels.grid(row=3, column=0, padx=5, pady=5)
l_component.grid(row=4, column=0, padx=5, pady=5)
l_createissue.grid(row=6, column=0, padx=5, pady=5)
l_reporter.grid(row=8, column=0, padx=5, pady=5)
l_assignee.grid(row=9, column=0, padx=5, pady=5)

# Inpufields
e_issueID.grid(row=0, column=1, padx=5, pady=5)
e_summary.grid(row=1, column=1, padx=5, pady=5)
e_epiclink.grid(row=2, column=1, padx=5, pady=5)
e_labels.grid(row=3, column=1, padx=5, pady=5)
e_reporter.grid(row=8, column=1, padx=5, pady=5)
e_assignee.grid(row=9, column=1, padx=5, pady=5)

# Buttons
b_load.grid(row=0, column=2, padx=5, pady=5)
b_addLabel.grid(row=3, column=2, padx=5, pady=5)
b_pushIssues.grid(row=9, column=0, columnspan=3, padx=5, pady=5)

# Checkbox
chk_columns.grid(row=5,column=1)
chk_issues.grid(row=7,column =1)

print("Hallo")

# loop window
window.mainloop()
