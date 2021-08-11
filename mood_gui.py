from tkinter import Spinbox
from guizero import *
from classes_mood import *
import random

databs_obj = db_maker()
databs_obj.mood_db_setUp()

#This files contains a simple gui using GUIZERO for a mood tracking app. 

app = App(title="Luis' Mood Tracker", width=780, height=1000, layout="grid")
box = Box(app, layout="grid", grid=[0, 0])
box_2 = Box(app, layout="grid", grid=[0, 1])
box_3 = Box(app, layout="grid", grid=[0, 2]) #I had to use three different boxex to add a textbox

title_txt = Text(box, text="Luis' Mood Tracker", size=20, font="Times New Roman", color="Green", grid=[1,1])

#Consider making the font more lively, maybe fool around with BG colors. 
happy_sad_txt = Text(box_2, text="Happy <---------------vs---------------->Sad",grid=[2, 1])

feel_txt = Text(box_2, text="How i feel today:", grid=[1, 2])
feel_Slide = Slider(box_2, start=1, end=5, horizontal=True, grid=[2, 2], width=400)

feelTmrw_txt = Text(box_2, text="Tomorrow will be: ", grid=[1, 3])
tmorrow_Slide = Slider(box_2, start=1, end=5, horizontal=True, grid=[2, 3], width=400)

good_bad_txt = Text(box_2, text="\n\nGood<---------------vs---------------->Bad",grid=[2,4])

hygiene_txt = Text(box_2, text="My Hygiene:", grid=[1, 5])
hygn_rate_slide = Slider(box_2, start=1, end=5, horizontal=True, grid=[2, 5], width=400)

spirituality_txt = Text(box_2, text="Spirituality: ", grid=[1, 6])
sprtlity_slide = Slider(box_2, start=1, end=5, horizontal=True, grid=[2, 6], width=400)

eating_txt = Text(box_2, text="Eat Healthy: ", grid=[1, 7])
eating_slide = Slider(box_2, start=1, end=5, horizontal=True, grid=[2, 7], width=400)

wild_cards_Text = Text(box_2, text="\nNon-rigorous tracked\nactivities.\n Adds 5 point\nto score", grid=[1, 8])

work_checkbox = CheckBox(box_2, text="Called off work", grid=[2, 8])
exercise_chckBox = CheckBox(box_2, text="Did not work out", grid=[2, 9])
addict_checkbox = CheckBox(box_2, text="\nEngaged in Addictive behavior", grid=[2, 10])

notes_txtBox = TextBox(box_3, width=50, height=5, grid=[1, 1], multiline=True, scrollbar=True)

#this function serves as the logic of the db_adder it takes the collection of values and 
# and adds them in their right spot in the db. 
#\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/

def submitter():
    feel_val = feel_Slide.value
    tomrrw_val = tmorrow_Slide.value
    hygiene_val = hygn_rate_slide.value
    spiritual_val = sprtlity_slide.value
    health_eating = eating_slide.value
    work_box_val = work_checkbox.value
    exercise_val = exercise_chckBox.value
    addiction_val = addict_checkbox.value 

    if work_checkbox.value == 0:
        work_box_val = 1
    
    elif work_checkbox.value == 1:
        work_box_val = 5   

    if exercise_chckBox.value == 0:
        exercise_val = 1

    elif exercise_chckBox.value == 1:
        exercise_val = 5

    if addict_checkbox.value == 0:
        addiction_val = 1
    elif addict_checkbox.value == 1:
        addiction_val = 5

    total_val = feel_val + tomrrw_val + hygiene_val + spiritual_val + health_eating + work_box_val + exercise_val + addiction_val
    
    id_val = random.randint(1, 9999999)

    databs_obj.db_adder(id_val, feel_val, tomrrw_val, hygiene_val, spiritual_val, health_eating, work_box_val, exercise_val, addiction_val, total_val)
 
    # FROM THIS POINT I AM WORKING ON A FILE SYSTEM THAT TAKES A VARIABLE NAME AND STORES IT 
    # MY HOPE IS TO EVENTUALLY CREATE A SUBDIRECTORY AND TAKE THOSE SAVED FILES AND SERVE THEM BACK
    # IN A GUIZERO APP TO VIEW READ AND USE.
    # I ATTEMPTED RECURSION TO CREATE THE MUTABLE FILE NAMES BUT I FEEL I DID IT WRONG 
    # AND A SIMPLE FOR LOOP ALSO DID NOT WORK
    
    items_to_display = "Your ID is:\t\n" + "\n" + str(id_val) + "\n" + "Today you feel\t\n" + "\n" + str(feel_val) + "\n" + "Tomorrow seems hopefully\t\n" + "\n" + str(tomrrw_val) + "\n" + "my grooming was:\t\n " + "\n" +str(hygiene_val) + "\n" + "my Spiritual life was:\t \n" + "\n" + str(health_eating) + "\n" + "i went to work\t\n" + "\n" + str(work_box_val) + "\n" + "Exercise:\t\n " + "\n" + str(exercise_val) +"\n" + "Addiction:\t\n" + "\n" + str(addiction_val) + "\n"  
    file_1 = open("hello.txt", "a+")
    full_note = items_to_display + notes_txtBox.value
    file_1.write(full_note)
    file_1.close

    #MESSAGEBOX WIDGET TODAY
    mssg_percent = total_val/50

    if mssg_percent < .50:
        app.info("info", f"Your value for the day is {total_val} out of 45")

    elif mssg_percent >= .50:
        app.info("infoBad", f"Your value for the day is {total_val} out of 45. Please reach out to your support network")

submit_button = PushButton(box_3, text="Submit" ,command=submitter, width=20, height=1, grid=[1, 2] )

app.display()