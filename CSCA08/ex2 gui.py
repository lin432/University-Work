# a simple gui to use for testing E2 in CSCA08
# author: Brian Harrington
# 2013
# based on code by Michelle Craig
# This code is provided without comments on purpose. Students should
# not feel that they have to try to understand this code. Any student
# who particularly wants a commented version may ask the instructor
try:
    import ex2 as mf
    imported_correctly = True
except ImportError:
    imported_correctly = False

from tkinter import *


def functions_implemented():
    functions_needed = ['term_work_mark', 'final_mark',
                        'percentage', 'is_pass']
    for fun in functions_needed:
        if fun not in mf.__dict__:
            return False
    return True


class Application(Frame):

    def recalculate_percentages(self, event):
        for work in self.term_work_items:
            new_val = mf.percentage(self.raw[work].get(),
                                    self.max_mark[work])
            self.percent[work]["text"] = "(%.2f percent)" % (new_val)

    def post_no_import_message(self):
        self.create_quit_button()
        message = '''You do not have the required module called ex2.py.
Go back and look at the exercise instructions.'''
        message_label = Label(text=message)
        message_label.pack({"padx": 10})

    def post_message(self):
        self.create_quit_button()
        message = '''You have the required file called ex2.py but it
needs to contain all the functions listed in the handout before this code will
work properly.  Go back and look at the instructions.'''
        message_label = Label(text=message)
        message_label.pack({"padx": 10})

    def create_labelled_entry(self, item):
        my_frame = Frame(self)
        max_score = self.max_mark[item]
        self.labels[item] = Label(my_frame,
                                  text="%s out of %d" % (item, max_score))
        self.labels[item].pack({"side": "left"})
        raw_enterbox = Entry(my_frame)
        raw_enterbox.pack({"side": "left"})
        raw_enterbox["textvariable"] = self.raw[item]
        percent = mf.percentage(self.raw[item].get(), max_score)
        self.percent[item] = Label(my_frame, text="%.2f percent" % (percent))
        self.percent[item].pack({"side": "left"})
        raw_enterbox.bind('<Key-Return>', self.recalculate_percentages)
        raw_enterbox.bind('<Key-Tab>', self.recalculate_percentages)
        my_frame.pack()

    def calc_term(self):
        self.term_work = mf.term_work_mark(self.raw['a0'].get(),
                                           self.raw['a1'].get(),
                                           self.raw['a2'].get(),
                                           self.raw['exercises'].get(),
                                           self.raw['quizzes'].get(),
                                           self.raw['term tests'].get())
        self.recalculate_percentages(None)
        label_text = "Term work total is: " + str(self.term_work)
        if self.term_work_total is None:
            self.term_work_total = Label(self, text=label_text)
            self.term_work_total.pack({"side": "top"})
        else:
            self.term_work_total["text"] = label_text

    def calc_final(self):
            self.final = mf.final_mark(self.raw['a0'].get(),
                                       self.raw['a1'].get(),
                                       self.raw['a2'].get(),
                                       self.raw['exercises'].get(),
                                       self.raw['quizzes'].get(),
                                       self.raw['term tests'].get(),
                                       self.raw['exam'].get())
            self.recalculate_percentages(None)
            message = "Final mark is: " + str(self.final) + "\n"
            if mf.is_pass(self.raw['a0'].get(),
                          self.raw['a1'].get(),
                          self.raw['a2'].get(),
                          self.raw['exercises'].get(),
                          self.raw['quizzes'].get(),
                          self.raw['term tests'].get(),
                          self.raw['exam'].get()):
                message += " Congratulations! You passed!"
            else:
                message += " Looks like we'll be seeing you again next year"
            if self.final_total is None:
                self.final_total = Label(self,
                                         text=message)
                self.final_total.pack({"side": "top"})
            else:
                self.final_total["text"] = message

    def create_quit_button(self):
        QUIT = Button(self)
        QUIT["text"] = "QUIT"
        QUIT["command"] = self.quit
        QUIT.pack({"padx": 20, "pady": 10, "side": "top"})

    def create_term_work_button(self):
        term_work = Button(self)
        term_work["text"] = "Click to (re)calculate term work mark"
        term_work["command"] = self.calc_term
        term_work.pack()

    def create_final_button(self):
        final = Button(self)
        final["text"] = "Click to (re)calculate final mark"
        final["command"] = self.calc_final
        final.pack()

    def create_widgets(self):
        message = '''Enter your raw marks, and this program will calculate
        your term/final grades \n and tell you whether you passed CSCA08'''
        message_label = Label(text=message)
        message_label.pack({"side": "top"})
        for work in self.term_work_items:
            self.raw[work] = DoubleVar()
            self.create_labelled_entry(work)
        self.create_term_work_button()
        self.create_final_button()
        self.create_quit_button()

    def __init__(self, master=None):
        self.term_work_items = ['exercises', 'quizzes',
                                'a0', 'a1', 'a2', 'term tests', 'exam']
        self.max_mark = {'a0': mf.get_max('a0'), 'a1': mf.get_max('a1'),
                         'a2': mf.get_max('a2'),
                         'exercises': mf.get_max('exercises'),
                         'term tests': mf.get_max('term tests'),
                         'quizzes': mf.get_max('quizzes'),
                         'exam': mf.get_max('exam')}
        self.term_work_total = None
        self.final_total = None
        self.goal_mark = DoubleVar()
        self.exam_goal = 0.0
        self.labels = {}
        self.raw = {}
        self.percent = {}
        Frame.__init__(self, master)
        if imported_correctly and functions_implemented():
            self.create_widgets()
        elif imported_correctly:
            self.post_message()
        else:
            self.post_no_import_message()
        self.pack()

root = Tk()
app = Application(master=root)
app.master.title("Simple Marks Calculator Using Functions from E2")
app.mainloop()
root.destroy()
