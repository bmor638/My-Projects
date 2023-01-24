# https://projectgurukul.org/python-mad-libs-generator-game/
# https://data-flair.training/blogs/python-mad-libs-generator-game/
# https://codeinplace.stanford.edu/2021/showcase/761
# Beckett Morris | 13 January 2022 | Honorbound

from tkinter import *

def madlib1():
    # Create a new window for the first lib
    wn = Toplevel(root)
    wn.configure(bg='#daa520')
    wn.title("The Gold")
    wn.geometry('375x575')
    wn.resizable(False, False)
    
    # Create the labels that will display the text
    Label(wn, text='The Gold', font=("Times", 20, 'bold'), bg='#daa520').place(x=120, y=0)
    Label(wn, text='Animal:', font=("Times", 15), bg='#daa520').place(x=0, y=35)
    Label(wn, text='Choose a parent:', font=("Times", 15), bg='#daa520').place(x=0, y=70)
    Label(wn, text='Choose a month:', font=("Times", 15), bg='#daa520').place(x=0, y=105)
    Label(wn, text='Noun:', font=("Times", 15), bg='#daa520').place(x=0, y=140)
    Label(wn, text='Verb (past tense):', font=("Times", 15), bg='#daa520').place(x=0, y=175)
    Label(wn, text='Number:', font=("Times", 15), bg='#daa520').place(x=0, y=210)
      
    # Create the entry boxes for user input
    animal_entry = Entry(wn, width=19)
    animal_entry.place(x=250, y=35)

    noun_entry = Entry(wn, width=19)
    noun_entry.place(x=250, y=140)

    movement_entry = Entry(wn, width=19)
    movement_entry.place(x=250, y=175)

    num_entry = Entry(wn, width=19)
    num_entry.place(x=250, y=210)
      
    # Create the option menus for user input
    parents = ["Mom", "Dad"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
   
    parent_opt=StringVar(wn)
    parent_opt.set(parents[0])
    OptionMenu(wn, parent_opt, *parents).place(x=250, y=70)
      
    month_opt=StringVar(wn)
    month_opt.set(months[0])
    OptionMenu(wn, month_opt, *months).place(x=250, y=105)

    # Function to put the story together
    def submission():
        # Get the user's inputs
        animal=animal_entry.get()
        parent=parent_opt.get()
        month=month_opt.get()
        noun=noun_entry.get()
        movement=movement_entry.get()
        num=num_entry.get()
        # Add the user's inputs to the story and place as a label
        story=f'''
        There was once a {animal}. 
        He was always getting told off. 
        One day while his {parent} 
        was sitting in the garden
        in {month}, he sneaked out. 
        He did not mean to go far, 
        but he saw a glittery thing 
        on the {noun} and
        {movement} over to it. 
        He found out it was gold
        and became rich because 
        he had {num} pieces of gold.'''
        Label(wn, text=story, font=("Times", 12), anchor=CENTER, background='#daa520').place(x=55, y=310)

    # Create a submit button to execute the submission function
    submit_btn=Button(wn, text="Submit", command=submission, font=("Times", 12))
    submit_btn.place(x=150, y=270)

def madlib2():
    # Create a new window for the second lib
    wn = Toplevel(root)
    wn.configure(bg='#fdd7e4')
    wn.title("The Ring")
    wn.geometry('375x575')
    wn.resizable(False, False)

    # Create the labels for user input
    Label(wn, text='The Ring', font=("Georgia", 17, "bold"), bg='#fdd7e4').place(x=130, y=0)
    Label(wn, text='Boy\'s name:', font=("Georgia", 12), bg='#fdd7e4').place(x=0, y=35)
    Label(wn, text='Another boy\'s name:', font=("Georgia", 12), bg='#fdd7e4').place(x=0, y=70)
    Label(wn, text='Girl\'s name:', font=("Georgia", 12), bg='#fdd7e4').place(x=0, y=110)
    Label(wn, text='Another girl\'s name:', font=("Georgia", 12), bg='#fdd7e4').place(x=0, y=150)
    Label(wn, text='Animal:', font=("Georgia", 12), bg='#fdd7e4').place(x=0, y=190)
    Label(wn, text='Exclamation:', font=("Georgia", 12), bg='#fdd7e4').place(x=0, y=230)
      
    # Create the entry boxes for user input
    boy1_name_entry=Entry(wn, width=19)
    boy1_name_entry.place(x=250, y=35)
     
    boy2_name_entry=Entry(wn, width=19)
    boy2_name_entry.place(x=250, y=70)
      
    girl1_name_entry=Entry(wn, width=19)
    girl1_name_entry.place(x=250, y=110)
      
    girl2_name_entry=Entry(wn, width=19)
    girl2_name_entry.place(x=250, y=150)
      
    animal_entry=Entry(wn, width=19)
    animal_entry.place(x=250, y=190)
      
    exclamation_entry=Entry(wn, width=19)
    exclamation_entry.place(x=250, y=230)

    # Function to put the story together
    def submission():
        # Get the user's inputs
        boy1=boy1_name_entry.get()
        boy2=boy2_name_entry.get()
        girl1=girl1_name_entry.get()
        girl2=girl2_name_entry.get()
        animal=animal_entry.get()
        exclamation=exclamation_entry.get()
        # Add the user's inputs to the story and place as a label
        story=f'''
        Once upon a time, two people, 
        {girl1} and {boy1} were walking
        in the park. They were talking about
        his {animal}. Then {boy1} exclaimed, 
        "{exclamation}!" "What is it, {boy1}?" cried {girl1}.
        "I just remembered something, 
        I have this ring in my pocket," said {boy1}.
        "Why would you have that?" asked {girl1}.
        "Will you marry me?" {boy1} asked. 
        {girl1} replied, 
        "Ummmm...Yes, I LOVE YOU, {boy1}!" 
        So they left on {boy1}'s {animal} 
        to their kingdom and had two children 
        named {girl2} and {boy2}, 
        and they lived 
        happily ever after 
        as every story should end!'''
        Label(wn, text=story, font=("Georgia", 8), anchor=CENTER, background='#fdd7e4').place(x=50, y=310)
      
    # Create a submit button to execute the submission function
    submit_btn = Button(wn, text="Submit", command=submission, font=('Georgia', 12))
    submit_btn.place(x=150, y=270)

def madlib3():
    # Create a new window for the third lib
    wn = Toplevel(root)
    wn.configure(bg='Aquamarine')
    wn.title("Magic Computers")
    wn.geometry('375x585')
    wn.resizable(False, False)

    # Create the labels for user input
    Label(wn, text='The Magic Computers', font=("Courier", 17, "bold"), bg='Aquamarine').place(x=55, y=0)
    Label(wn, text='Noun:', font=("Courier", 12), bg='Aquamarine').place(x=0, y=35)
    Label(wn, text='Noun (plural):', font=("Courier", 12), bg='Aquamarine').place(x=0, y=70)
    Label(wn, text='Verb:', font=("Courier", 12), bg='Aquamarine').place(x=0, y=110)
    Label(wn, text='Verb:', font=("Courier", 12), bg='Aquamarine').place(x=0, y=150)
    Label(wn, text='Body part (plural):', font=("Courier", 12), bg='Aquamarine').place(x=0, y=190)
    Label(wn, text='Adjective:', font=("Courier", 12), bg='Aquamarine').place(x=0, y=230)
    Label(wn, text='Noun (plural):', font=("Courier", 12), bg='Aquamarine').place(x=0, y=270)
    Label(wn, text='Adjective:', font=("Courier", 12), bg='Aquamarine').place(x=0, y=310)

    # Create the entry boxes for user input
    noun_entry=Entry(wn, width=19)
    noun_entry.place(x=250, y=35)
     
    pnoun_entry=Entry(wn, width=19)
    pnoun_entry.place(x=250, y=70)
      
    v1_entry=Entry(wn, width=19)
    v1_entry.place(x=250, y=110)
      
    v2_entry=Entry(wn, width=19)
    v2_entry.place(x=250, y=150)
      
    body_part_entry=Entry(wn, width=19)
    body_part_entry.place(x=250, y=190)
      
    adj_entry=Entry(wn, width=19)
    adj_entry.place(x=250, y=230)

    pnoun2_entry=Entry(wn, width=19)
    pnoun2_entry.place(x=250, y=270)

    adj2_entry=Entry(wn, width=19)
    adj2_entry.place(x=250, y=310)

    # Function to put the story together
    def submission():
        # Get the user's inputs
        noun=noun_entry.get()
        pnoun=pnoun_entry.get()
        verb1=v1_entry.get()
        verb2=v2_entry.get()
        body_part=body_part_entry.get()
        adj1=adj_entry.get()
        pnoun2=pnoun2_entry.get()
        adj2=adj2_entry.get()
        # Add the user's inputs to the story and place as a label
        story=f'''
        Today, every student has a computer small 
        enough to fit into her {noun}. She can 
        solve any math problem by simply pushing 
        the computer's little {pnoun}. 
        Computers can add, multiply, divide, 
        and {verb1}. They can also {verb2} 
        better than a human. Some computers are
        {body_part}. Others have 
        a/an {adj1} screen that 
        shows all kinds of 
        {pnoun2} and {adj2} figures.'''
        Label(wn, text=story, font=('Courier', 9), anchor=CENTER, background='Aquamarine').place(x=-10, y=390)
      
    # Create a submit button to execute the submission function
    submit_btn = Button(wn, text="Submit", command=submission, font=('Courier', 12))
    submit_btn.place(x=150, y=350)

# Create the main window
root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
root.configure(background='#872657')
Label(root, text= '', bg='#872657').pack()
Label(root, text= 'MAD LIBS', fg='thistle', bg='#872657', font = 'arial 20 bold').pack()
Label(root, text = 'Select a lib:', fg='thistle', bg='#872657', font = 'arial 15 bold').pack()

# Create a button for each lib
Button(root, text='The Gold', font=("Arial", 15), command=madlib1, foreground='#872657', bg = 'Thistle').place(x=100, y=100)
Button(root, text='The Ring', font=("Arial", 15), command=madlib2, foreground='#872657', bg = 'Thistle').place(x=100, y=160)
Button(root, text='The Magic Computers', font=("Arial", 15), command=madlib3, foreground='#872657', bg = 'Thistle').place(x=40, y=220)

root.mainloop()