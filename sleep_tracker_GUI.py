from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from collections import Counter

#Add a label to "place" with font width "width" in order to create a space
def space(place, width):
    Label(place, text="", fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", width)).pack()





#SLEEP SLEEP SLEEP
def sleep():
    wn = Toplevel(root)
    wn.configure(bg='#d5c6e0')
    wn.geometry("300x300")
    wn.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
    wn.title("Sleep")

    def add_sleep():
        wn2 = Toplevel(wn)
        wn2.configure(bg='#d5c6e0')
        wn2.resizable(False, False)
        wn2.geometry("300x350")
        wn2.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
        wn2.title("Add sleep data")
        Label(wn2, text="Hint: You can cancel data entry\nat any time by typing \"Cancel.\"", fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 8)).pack()
        space(wn2, 8)
        Label(wn2, text="Enter the date\nof your sleep below (mm/dd/yyyy):", fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 12)).pack()
        date_entry = Entry(wn2, width=20)
        date_entry.place(x=90, y=100)
        Label(wn2, text="Enter the hours\nof your sleep below (00.0):", fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 12)).place(x=50, y=153)
        hrs_entry = Entry(wn2, width=20)
        hrs_entry.place(x=90, y=200)

        def submit_sd():
            date = date_entry.get()
            hrs = hrs_entry.get()
            f = open("sleep_data.txt", "a") #change to test
            if date == "cancel" or date == "Cancel":
                f.write("")
                Label(wn2, text="                          ", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 30)).place(x=50, y=255) #cover button
                Label(wn2, text="Canceled", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 14)).place(x=110, y=255)
            else:
                if hrs == "cancel" or hrs == "Cancel":
                    f.write("")
                    Label(wn2, text="                          ", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 30)).place(x=50, y=255) #cover button
                    Label(wn2, text="Canceled", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 14)).place(x=110, y=255)
                else:
                    f.write("\n" + date + " " + hrs)
                    Label(wn2, text="                          ", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 30)).place(x=50, y=255) #cover button
                    Label(wn2, text="Logged!", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 14)).place(x=110, y=255)
            f.close()

        Button(wn2, text="Submit", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=submit_sd).place(x=50, y=255)

    def avg_sleep():
        wn2 = Toplevel(wn)
        wn2.configure(bg='#d5c6e0')
        #wn2.geometry("300x300")
        wn2.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
        wn2.title("Average sleep")
        total_hrs = 0.0
        total_days = 0
        f = open("sleep_data.txt")
        for line in f:
            total_days = total_days + 1
            hours = float(line[11:].strip())
            total_hrs = total_hrs + hours
        avg = total_hrs / total_days
        f.close()
        output = "Average hours\nof sleep per night:\n\n" + str(avg)
        Label(wn2, text=output, fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 12)).pack()

    def least_sleep():
        wn2 = Toplevel(wn)
        wn2.configure(bg='#d5c6e0')
        #wn2.geometry("300x300")
        wn2.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
        wn2.title("Least sleep")
        least = 100.0
        date_least = ""
        f = open("sleep_data.txt")
        for line in f:
            hours = float(line[11:].strip())
            if hours < least:
                least = hours
                date_least = line[:10]
            elif hours == least:
                date_least = date_least + " and\n" + line[:10]
        f.close()
        output = "Least sleep:\n\n" + str(least) + " hours on\n" + date_least
        Label(wn2, text=output, fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 12)).pack()

    def greatest_sleep():
        wn2 = Toplevel(wn)
        wn2.configure(bg='#d5c6e0')
        #wn2.geometry("300x300")
        wn2.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
        wn2.title("Greatest sleep")
        most = -100.0
        date_most = ""
        f = open("sleep_data.txt")
        for line in f:
            hours = float(line[11:].strip())
            if hours > most:
                most = hours
                date_most = line[:10]
            elif hours == most:
                date_most = date_most + " and " + line[:10]
        f.close()
        output = "Greatest sleep:\n\n" + str(most) + " hours on\n" + date_most
        Label(wn2, text=output, fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 12)).pack()

    def graph():
        x = []
        x2 = []
        y = []
        counter = 1
        for line in open("sleep_data.txt"):
            lines = [i for i in line.split()]
            x.append(lines[0])
            counter = counter + 1
            x2.append(counter)
            y.append(float(lines[1]))
        plt.title("Zzzzzzzz")
        plt.xlabel("Date")
        plt.ylabel("Hours of sleep")
        plt.plot(x, y, marker = 'o', c = '#b78be8')
        plt.xticks(fontsize=6)
        plt.show()


    #Buttons with options
    space(wn, 8)
    Button(wn, text="Add sleep data", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=add_sleep).pack()
    space(wn, 5)
    Button(wn, text="Find your average sleep", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=avg_sleep).pack()
    space(wn, 5)
    Button(wn, text="Find your least sleep", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=least_sleep).pack()
    space(wn, 5)
    Button(wn, text="Find your greatest sleep", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=greatest_sleep).pack()
    space(wn, 5)
    Button(wn, text="View a graph of your sleep", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=graph).pack()





#DREAMS DREAMS DREAMS
def dreams():
    wn = Toplevel(root)
    wn.configure(bg='#d5c6e0')
    wn.geometry("300x300")
    wn.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
    wn.title("Dreams")

    def add_dreams():
        wn2 = Toplevel(wn)
        wn2.configure(bg='#d5c6e0')
        wn2.geometry("300x350")
        wn2.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
        wn2.title("Add dream data")
        Label(wn2, text="Hint: You can cancel data entry\nat any time by typing \"Cancel.\"", fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 8)).pack()
        space(wn2, 8)
        Label(wn2, text="Enter the date\nof your dream below (mm/dd/yyyy):", fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 12)).pack()
        date_entry = Entry(wn2, width=20)
        date_entry.place(x=90, y=100)
        Label(wn2, text="Describe\nyour dream below:", fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 12)).place(x=77, y=153)
        dream_entry = Entry(wn2, width=20)
        dream_entry.place(x=90, y=200)

        def submit_sd():
            date = date_entry.get()
            dream = dream_entry.get()
            f = open("dream_data.txt", "a") #change to test
            if date == "cancel" or date == "Cancel":
                f.write("")  
                Label(wn2, text="                          ", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 30)).place(x=47, y=255) #cover button
                Label(wn2, text="Canceled", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 14)).place(x=105, y=255)
            else:
                if dream == "cancel" or dream == "Cancel":
                    f.write("")
                    Label(wn2, text="                          ", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 30)).place(x=47, y=255) #cover button
                    Label(wn2, text="Canceled", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 14)).place(x=105, y=255)
                else:
                    f.write("\n" + date + " | " + dream)
                    Label(wn2, text="                          ", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 30)).place(x=47, y=255) #cover button
                    Label(wn2, text="Logged!", fg="#4d5075", bg="#d5c6e0", font=("Lucida Bright", 14)).place(x=110, y=255)
            f.close()

        Button(wn2, text="Submit", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=submit_sd).place(x=47, y=255)
        

    def view_dreams():
        wn2 = Toplevel(wn)
        wn2.configure(bg='#d5c6e0')
        wn2.geometry("1000x400")
        wn2.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
        wn2.title("View your dreams")
        scroll = Scrollbar(wn2, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)
        scroll_horiz = Scrollbar(wn2, orient='horizontal')
        scroll_horiz.pack(side=BOTTOM, fill=X)
        t = Text(wn2, bg='#d5c6e0', wrap=NONE, yscrollcommand=scroll.set, xscrollcommand=scroll_horiz.set)
        f = open("dream_data.txt")
        for line in f:
            t.insert(END, line)
        t.pack(side=TOP, fill=X)
        scroll.config(command=t.yview)
        scroll_horiz.config(command=t.xview)

    def dream_fixation():
        wn2 = Toplevel(wn)
        wn2.configure(bg='#d5c6e0')
        #wn2.geometry("300x300")
        wn2.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
        wn2.title("Dream fixation")
        new_words = []
        insignificant = ["and", "or", "I", "that", "with", "the", "get", "am", "is", "are", "was", "were", "have", "has", "had", "will", "other", "on", "to", "a", "in", "it"]
        with open("dream_data.txt", 'r') as dreams:
            for line in dreams:
                dream = line[13:]
                words = dream.split()
                for word in words:
                    new_words.append(word)
        word_frequency = Counter(new_words)
        max_frequency = 0
        most_repeated = ""
        #second_repeated = ""
        for word in word_frequency:
            if word in insignificant:
                continue
            if word_frequency[word] > max_frequency:
                max_frequency = word_frequency[word]
                #second_repeated = most_repeated
                most_repeated = word
        output = "Your most common theme is:\n" + most_repeated
        #output2 = "Your second\nmost common theme is:\n" + second_repeated
        Label(wn2, text=output, fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 12)).pack()
        #space(wn2, 20)
        #Label(wn2, text=output2, fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 12)).pack()


    #Buttons with options
    space(wn, 24)
    Button(wn, text="Add dream data", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=add_dreams).pack()
    space(wn, 24)
    Button(wn, text="View your dreams", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=view_dreams).pack()
    space(wn, 24)
    Button(wn, text="Dream fixation", font=("Lucida Bright", 10), height=2, width=25, fg="#d5c6e0", bg="#5f4b66", command=dream_fixation).pack()





#MAIN MAIN MAIN
root = Tk()
root.iconphoto(False, PhotoImage(file="sleepy.png")) #setting the icon photo
root.geometry("400x500")
root.title("Beckett's Sleep Tracker Program")
root.configure(background="#d5c6e0")
Label(root, text="Beckett's Sleep\nTracker Program", fg="#5f4b66", bg="#d5c6e0", font=("Lucida Bright", 25)).pack()
#Add commands to buttons :)
space(root, 5)
Button(root, text="SLEEP", font=("Lucida Bright", 20), height=2, width=15, fg="#d5c6e0", bg="#5f4b66", command=sleep).pack()
space(root, 8)
Button(root, text="DREAMS", font=("Lucida Bright", 20), height=2, width=15, fg="#d5c6e0", bg="#5f4b66", command=dreams).pack()
img = Image.open("s1.png")
space(root, 5)
img = img.resize((300, 175), Image.ANTIALIAS)
s = ImageTk.PhotoImage(img)
s_label = Label(image=s)
s_label.pack()
root.mainloop()
