from genericpath import isfile
from sys import path
from guizero import *
from classes_mood import *
import datetime
#Gotta clean my import statements


databs_obj = db_maker()
databs_obj.mood_db_setUp()

#This files contains a simple gui using GUIZERO for a mood tracking app.
# PS HOW HARD WILL IT BE TO REFACTOR THIS INTO MAIN FUNCTION? I WANNA START BEING 
# MORE PEP 8 COMPLIANT  

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

def submitter(x=1):
    date_now = datetime.date.today()
    date_now = str(date_now)
    feel_val = feel_Slide.value
    tomrrw_val = tmorrow_Slide.value
    hygiene_val = hygn_rate_slide.value
    spiritual_val = sprtlity_slide.value
    health_eating = eating_slide.value
    work_box_val = work_checkbox.value
    exercise_val = exercise_chckBox.value
    addiction_val = addict_checkbox.value 
    notes_Val = notes_txtBox.value

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
    

    databs_obj.db_adder(date_now, feel_val, tomrrw_val, hygiene_val, spiritual_val, health_eating, work_box_val, exercise_val, addiction_val, total_val, notes_Val)
 



    #MESSAGEBOX WIDGET TODAY
    mssg_percent = total_val/50

    if mssg_percent < .50:
        app.info("info", f"Your value for the day is {total_val} out of 45")

    elif mssg_percent >= .50:
        app.info("infoBad", f"Your value for the day is {total_val} out of 45. Please reach out to your support network")

#SOMEHOW WHEN WORKING WITH GUI FRAMEWORKS, THE INTERPRETED NATURE OF LANGUANGE FORCES ME TO CREATE CODE PASTA 
#BY INSERTING THE FUNC DEFINITION BEFORE I CAN CALL IT. I IMAGINE I COULD TECHNICALLY CALL IT IF I MAKE THE GUI INTO A 
# SEPARATE FUNCTION INSTEAD OF A RAW DATA. 

def second_Wind_app():
        second = App(title="Database Entry Display", width=740, height=750, layout="grid")
        box = Box(second, layout="grid", grid=[0, 0])
        box2 = Box(second, layout="grid", grid=[0, 1])
        box3 = Box(second, layout="grid", grid=(0, 2))
        title = Text(box, text="Data Selection Menu ", grid=[0,0],font="Times New Roman",size=20, color="Green")
        year_txt = Text(box2, text="Year:\t", grid=[0,1])
        month_txt = Text(box2, text="Month:\t", grid=[1,1])
        day_txt = Text(box2, text="Day:\t", grid=[2,1])
        combo1_yr = Combo(box2, options=["2020", "2021", "2023", "2024"], grid=[0, 2], width=5)
        combo2_month = Combo(box2, options=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"], grid=[1, 2], width=5)
        combo3_day = Combo(box2, options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"], grid=[2, 2], width=5)
        displaybx = TextBox(box3, width=50, height=19, grid=[0, 0], multiline=True, scrollbar=True)

       # THIS RIGHT HERE IS THE TROUBLESOME FUNCTION I CANT TELL IF THE COMPARE_DAT  Variable
       # IS CAUSING AN OPERATIONAL ERROR OR WHAT
        def button_sub():
            year_var = (combo1_yr.value)
            month_var = (combo2_month.value)
            day_var = (combo3_day.value)

            compare_dat = f'{year_var}-{month_var}-{day_var}'
            compare_dat = str(compare_dat)
                        
            databs_obj.db_id_Selector(compare_dat)

        buttn = PushButton(box3, text="Press here", command=button_sub, grid=[0, 1])
        
        second.display()

submit_button = PushButton(box_3, text="Submit" ,command=submitter, width=20, height=1, grid=[1, 2] )
secondwin_button = PushButton(box_3, text="View Data" ,command=second_Wind_app, width=20, height=1, grid=[1, 3] )

app.display()



