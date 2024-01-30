from genericpath import isdir
import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import os # to remove created audio files
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import subprocess
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import datetime
import wikipedia
from ecapture import ecapture as ec
import pyjokes
import re
import json
from urllib.request import urlopen
import operator
import math
import pywhatkit as kit
import winshell
from PyDictionary import PyDictionary
import ctypes
import screen_brightness_control as sbc
import os.path
import time
import randfacts
from englisttohindi.englisttohindi import EngtoHindi
import threading
from tkinter import filedialog as fd
from win32com.client import Dispatch
import easygui
import tkinter.font as font
import textwrap

voice_data=""
img=None
count = 0
count_wake_button = 0
is_on = True
wake_word = 'dora'

path2Notes = r"C://Users//Sakshi//Documents//Dora//Notes"
if (os.path.isdir(path2Notes)):
    files = os.listdir(path2Notes)
else:
    files = []

path2Screenshots = r"C://Users//Sakshi//Documents//Dora//Screenshots"
if (os.path.isdir(path2Screenshots)):
    ss = os.listdir(path2Screenshots)
else:
    ss=[]

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    global voice_data 
    for term in terms:
        if term in voice_data:
            return True

def there_does_not_exist(terms):
    global voice_data 
    for term in terms:
        if term in voice_data:
            return False
    return True        

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

# Define our switch function
def switch():
    global is_on
    global count_wake_button
    count_wake_button = count_wake_button + 1
    if (count_wake_button % 2 == 0):
        is_on = False
    else:
        is_on = True    
    print("Wake word is "+ str(is_on))    
    # Determine is on or off
    if  is_on:
        wake.config(text = "Wake word is on")
        while is_on ==True:
            if (count_wake_button % 2 == 0):
                is_on = False
            if is_on==False:
                label.config(text="")
                label1.config(text="")
                exit()
            else:
                label.config(text="Say Dora to wake me up!")
                print("Listening switch()")
                if is_on==False:
                    label.config(text="")
                    label1.config(text="")
                    exit()
                voice_data = record_audio2()
                if voice_data.count(wake_word)>0:
                    engine_speak("I am ready")
                    start()
    else:
        wake.config(text = "wake word is off")
        label.config(text="")
        label1.config(text="")
        exit()


# listen for audio and convert it to text:
def record_audio2():
    with sr.Microphone() as source: # microphone as source  
        voice_data = ''
        global is_on
        global count_wake_button
        if (count_wake_button % 2 == 0):
            is_on = False
        if is_on==False:
            label.config(text="")
            label1.config(text="")
            exit()    
        else:
            try:  
                r.adjust_for_ambient_noise(source, duration=1)
                r.dynamic_energy_threshold = True
                #r.pause_threshold = 1
                if is_on==False:
                    label.config(text="")
                    label1.config(text="")
                    exit()
                audio = r.listen(source)
                print("(Done Listening-recordaudio2)")
                if is_on==False:
                    label.config(text="")
                    label1.config(text="")
                    exit()
                voice_data = r.recognize_google(audio)  # convert audio to text
            except sr.RequestError:
                engine_speak('Sorry, the service is down') # error: recognizer is not connected
            except Exception as e:
                if is_on==False:
                    label.config(text="")
                    label1.config(text="")
                    exit()
                engine_speak("Listening timed out while waiting for phrase to start")
                print("record-audio2")
                return "None"
            print(">>", voice_data.upper()) # print what user said
            return voice_data.lower()

# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask) 
        #r.adjust_for_ambient_noise(source,duration = 1)
        #audio = r.listen(source)     # listen for the audio via source, 5s timeout,15sec long phrase accepted
        voice_data = ''
        try:
            audio = r.listen(source, 5, 10)
            print("(Done Listening)")
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        except sr.WaitTimeoutError as k:
            engine_speak("Listening timed out while waiting for phrase to start")
            print("waiting timeout recordaudio()")
        except Exception as e:
            engine_speak("Listening timed out while waiting for phrase to start")
            print("recordaudio() timeout")
        print(">>", voice_data.upper()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    global voice_data
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    print(asis_obj.name + ":", audio_string) # print what app said
    wrapper=textwrap.TextWrapper(width=50)
    word_list=wrapper.wrap(text=audio_string)
    typestr=""
    for ele in word_list:
        typestr += str(ele)+"\n"
    label.config(text=typestr)
    playsound.playsound(audio_file) # play the audio file 
    os.remove(audio_file) # remove audio file

#start listening
def start(): 
    global count
    global voice_data
    global label
    label1.config(text='')
    count = count+1
    if count==1:
        wishMe()    
    voice_data = record_audio("Listening...") # get the voice input
    print("Done")
    label1.config(text=voice_data)
    print("Q:", voice_data)
    respond(voice_data) # respond

#start wish me
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<4:
        engine_speak("Welcome. I am your personal assistant Dora. How may I help you?")
        print("Welcome. I am your personal assistant Dora. How may I help you?")
    elif hour>=4 and hour<12:
        engine_speak("Hello,Good Morning. I am your personal assistant Dora. How may I help you?")
        print("Hello,Good Morning. I am your personal assistant Dora. How may I help you?")
    elif hour>=12 and hour<17:
        engine_speak("Hello,Good Afternoon. I am your personal assistant Dora. How may I help you?")
        print("Hello,Good Afternoon. I am your personal assistant Dora. How may I help you?")
    else:
        engine_speak("Hello,Good Evening. I am your personal assistant Dora. How may I help you?")
        print("Hello,Good Evening. I am your personal assistant Dora. How may I help you?")

def get_operator_fn(op):
    return {'+' : operator.add,
            'plus': operator.add,
            'add' : operator.add,
            '-' : operator.sub,
            'minus' : operator.sub,
            'subtract' : operator.sub,
            'x' : operator.mul,
            'multiply' : operator.mul,
            'multiplied' : operator.mul,
            'into' : operator.mul,
            '*' : operator.mul,
            'divide' :operator.__truediv__,
            'divided' :operator.__truediv__,
            '/' :operator.__truediv__,
            'by' :operator.__truediv__,
            'Mod' : operator.mod,
            'mod' : operator.mod,
            '^' : operator.xor,
            'power':operator.pow,
            'raised':operator.pow,
            'raise':operator.pow
            }[op]

def get_language(language):
    lang = {'english':'en',
            'chinese':'zh-TW',
            'french':'fr',
            'german':'de',
            'gujarati':'gu',
            'japanese':'ja',
            'kannada':'kn',
            'malayalam':'ml',
            'marathi':'mr',
            'punjabi':'pa',
            'russian':'ru',
            'spanish':'es',
            'tamil':'ta',
            'telugu':'te'}
    return lang.get(language)



    
def eval_binary_expr(op1,oper,op2):
    try:
        op1,op2 = float(op1),float(op2)
        if(math.ceil(op1)==math.floor(op1)):
            op1=int(op1)
        if(math.ceil(op2)==math.floor(op2)):
            op2=int(op2)    
        return get_operator_fn(oper)(op1,op2)
    except ValueError as ve:
        engine_speak("Please provide valid numbers.")
        start()  
    except ZeroDivisionError:
        engine_speak("Dividing any number by zero does not make sense.There's no solution,so any non-zero number divided by 0 is undefined.")    
    except ArithmeticError:
        return True  

def showcontent(event):
    global path2Notes
    x = lbox.curselection()
    if x != ():
        file = lbox.get(x)
        completepath=os.path.join(path2Notes,file)
        #,'r',encoding='utf-8'
        with open(completepath) as file:
            file = file.read()
        print(file)    
        text.config(state=NORMAL)
        text.delete('1.0',tk.END)
        text.insert(tk.END,file)
        text.config(state=DISABLED)   

def tasks(event):
    x3=lbox3.curselection()
    if x3!=():
        selection = lbox3.get(x3)
        if selection == "Desktop Apps":
            Tasks.config(text="Open Microsoft word\nOpen Notepad\nOpen Wordpad\nOpen Paint\nOpen Powerpoint\nOpen Excel\nOpen OneNote\nOpen Calculator\nOpen Google Chrome\nOpen file explorer",font=('Times New Roman',25))
        elif selection == "Websites":
            Tasks.config(text="Open Amazon.in\nOpen Flipkart.com\nOpen Geeksforgeeks.com\nOpen Twitter.com\nOpen pce.ac.in\n Open Stackoverflow\n Open quora\n Open wikipedia\n",font=('Times New Roman',25))
        elif selection == "Search Questions":
            Tasks.config(text="What is Artificial Intelligence?\nSearch for Artificial Intelligence\nWho is the Prime Minister of India?\nWhen is Diwali?\nHow are paints made?\nWhich is the language spoken in Maharashtra?\nWhere is Navi Mumbai?\nWhere am I?\nHow many people are there in the world?\nWhich are the top selling Books?\n Search for Dude Perfect on youtube\n Who is the Richest Person?\nLocate Navi Mumbai\nFind Navi Mumbai\nWhat kind of Language is Hindi?",font=('Times New Roman',25))
        elif selection == "General info":
            Tasks.config(text="Tell me the time\nTell me the day\nTell me the date\n What is the day today?\nWhich month is going on?\nWhat time is it?",font=('Times New Roman',25))
        elif selection == "Entertainment":
            Tasks.config(text="Play Stay on Youtube\nTell me a joke\nTell me some facts\nPlay songs\nPlay a game\nToss a coin\n Who am I?\n Thank You!\nGoodbye\nGood Morning\nHello\nWhat's your name?\nMy name is David\nYour name should be Dave\nHow are you?",font=('Times New Roman',25))
        elif selection == "Google Apps":
            Tasks.config(text="Open Gmail\nOpen Youtube\nOpen Google doc\n Create google document\nOpen Google sheet\nCreate google sheet\nOpen google slide\n Open google form\n Open google map\nOpen google meet\n Open googleclassroom\n Open google calender\n Open google translate\n Open google drive\nOpen google photos",font=('Times New Roman',25))
        elif selection == "Web Apps":
            Tasks.config(text="Open zoom\n Open whatsapp web\n Open cowin",font=('Times New Roman',25))
        elif selection == "Utilities":
            Tasks.config(text="Capture my screen\nTake a screenshot\nTake a photo\n Who created you?\n Who are you?\n Shutdown my computer\nRestart my computer\nLock my computer\nHibernate\nEmpty recycle bin\nIncrease the brightness of the screen\nDecrease the brightness of the screen\nDon't Listen\n Make a note\n Show my timetable",font=('Times New Roman',25))
        elif selection == "News and Information":
            Tasks.config(text="What are the headlines today?\nWhat's the news?\nWhat is the price of TATA Motors today?\nWhat's the weather today?\nWhat's the meaning of adorable?\nWhat is trending on twitter?\n What is the meaning of adorable?\n Flowers in hindi\nTell me about Artificial Intelligence\n Search for flowers on wkipedia\n Where am I?\n What is my exact location?\nBook my vaccination\nCovid updates\nTell me who is the Prime Minister of India",font=('Times New Roman',25))
        elif selection == "Calculations":
            Tasks.config(text="12+45\n4 power 3\n12 into 2\n10 mod 4\nAdd 4 and 2\nAdd 4 to 6\nCalculate 12 plus 13\nCalculate 45 minus 15\nCalculate 2 raise 5\nSubtract 15 from 36\nMultiply 4 into 60\nDivide 19 by 3\nRaise 4 to 3\n10 multilied by 12\n20 divided by 4\n7 raised to 2\n4 raise to 3\nWhat is the factorial of 5\nHow many degrees is 40\n53 in degrees\n30 radians is\n60 in radian",font=('Times New Roman',21)) 

#working
def showimage(event):
    global path2Screenshots
    x2 = lbox2.curselection()
    fname = lbox2.get(x2)
    completepath=os.path.join(path2Screenshots,fname)
    img = (Image.open(completepath))
    img = img.resize((1525,980),Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(img) 
    #w = new_image.width()
    #h = new_image.height()
    canvas.image = new_image
    canvas.create_image((0,0),image=new_image,anchor=NW)
    print(fname)

#response to Commands
def respond(voice_data):
    if(voice_data != ''):
        #today's date
        if there_exists(["what is today's date","date","today's date","tell me the date","tell me today's date","what is the date"]) and there_does_not_exist(["update","updates","in"]):
            today = datetime.datetime.now()
            date = today.strftime("%B %d, %Y")
            print(date)
            engine_speak("Today's date is: " + date)

        #today's day
        elif voice_data=="what's the day today" or voice_data=="what is the day today" or voice_data=="day":
        #elif there_exists(["what's the day today","what is the day today","day"]) and there_does_not_exist(["date","birthday","weather"]):
            x = datetime.datetime.now()
            day = x.strftime("%A")
            print(day)
            engine_speak("Today is " + day)    

        #month
        elif there_exists(["what's the month","which month is going on","month","tell me the month","which month is it","what is the month","what's the month"]):
            x = datetime.datetime.now()
            month = x.strftime("%B")
            print(month)
            engine_speak("The current month is "+month)    

        #current time
        elif there_exists(["what's the time","tell me the time","what time is it","what is the time","time","tell the time"]) and there_does_not_exist(["time table","timetable","in"]):
            search_term=voice_data.split()
            if len(search_term)<=4:   #what is the time in New York
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                print(time.ctime())
                engine_speak(f"The time is {strTime}")
            else:
                pass

        #search on google
        elif there_exists(["search","browse for"]) and 'youtube' not in voice_data and 'wikipedia' not in voice_data:
            search_term = voice_data.replace("search","").replace("for","").replace("on google","").replace("browse","")
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found for" + search_term)

        #open google
        elif there_exists(['open google','google']) and there_does_not_exist(["search","map","meet","doc","docs","document","form","sheet","slide","drive","translate","translator","photos","calendar","classroom"]):
            url = "https://www.google.com"
            webbrowser.get().open(url)
            engine_speak("Google chrome is open now")
            #time.sleep(5)    

        #open gmail
        elif there_exists(['open gmail','gmail']) and there_does_not_exist(["com"]): 
            url = "https://www.gmail.com"
            webbrowser.get().open(url)
            engine_speak("Google Mail is open now")
            #time.sleep(5)    

        #search on youtube
        elif there_exists(["youtube"]) and there_does_not_exist(["open","play"]):
            search_term = voice_data.split("for")[-1]
            search_term = search_term.replace("on youtube","").replace("search","").replace("for","")
            url = "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found for " + search_term + "on youtube")

        #open youtube
        elif there_exists(['open']) and 'youtube' in voice_data:
            url = "https://www.youtube.com"
            webbrowser.get().open(url)
            engine_speak("Youtube is open now")
            #time.sleep(5)

        #play music on youtube
        elif there_exists(["play"]) and there_does_not_exist(['song','music','game']): #and #there_exists(["on youtube"]):
            search_term = voice_data.replace("play","").replace("on youtube","")
            song = search_term
            kit.playonyt(song)
            engine_speak("playing " + song + " on youtube")        

        #get stock price
        elif there_exists(["price of"]):
            search_term = voice_data.replace("what","").replace("is","").replace("the","").replace("what's","").replace("'s","")
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found for " + search_term + " on google")
        
        #show time table
        elif there_exists(["show my time table","time table","timetable","schedule"]):
            im = Image.open(r"D:/photos 2020/IMG_20201005_180004.jpg")
            im.show()
        
        #weather
        elif "weather" == voice_data:
            #search_term = voice_data.replace("")
            search_term = voice_data.split("for")[-1]
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            engine_speak("Here is the weather for this week")

        #stone paper scisorrs
        elif there_exists(["game"]):
            voice_data = record_audio("choose among rock paper or scissor")
            moves=["rock", "paper", "scissor"]
        
            cmove=random.choice(moves)
            pmove=voice_data
            
            if pmove not in moves:
                engine_speak("Invalid move. Game exited")
            else:
                engine_speak("The computer chose " + cmove)
                engine_speak("You chose " + pmove)
                #engine_speak("hi")
                if pmove==cmove:
                    engine_speak("the match is draw")
                elif pmove== "rock" and cmove== "scissor":
                    engine_speak("Player wins")
                elif pmove== "rock" and cmove== "paper":
                    engine_speak("Computer wins")
                elif pmove== "paper" and cmove== "rock":
                    engine_speak("Player wins")
                elif pmove== "paper" and cmove== "scissor":
                    engine_speak("Computer wins")
                elif pmove== "scissor" and cmove== "paper":
                    engine_speak("Player wins")
                elif pmove== "scissor" and cmove== "rock":
                    engine_speak("Computer wins")

        #open any website
        elif there_exists(['open']) and there_exists(['com','.com','.in','in','org','.org','.co.in','co.in','edu','.edu']):
            reg_ex = re.search('open (.+)', voice_data)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain.strip() 
                webbrowser.open(url)
                engine_speak('The website you have requested has been opened for you')
            else:
                pass        

        #toss a coin
        elif there_exists(["toss","flip","coin"]) and there_does_not_exist(["what is","what's","how is","how's","tell me","tell me about"]):
            moves=["head", "tails"]   
            cmove=random.choice(moves)
            engine_speak("The computer chose " + cmove)

        #calculator
        elif there_exists(["plus","minus","into","by","power","+","-","*","/","x","mod"]) and there_does_not_exist(["exit","what is","what's","calculate","bye","excel","add","subtract","multiply","divide","and","powerpoint"]):
            oprs = voice_data.split()
            if len(oprs)==3:
                res = eval_binary_expr(oprs[0],oprs[1],oprs[2])
                if res is True:
                    engine_speak("Sorry,cannot perform the operation")
                elif res is not None:
                    if type(res)==float: #isinstance(res,float):
                        res= round(res,4)
                    engine_speak(res)
            else:
                engine_speak("I did not get that. Could you please repeat?")
                start()

        elif (there_exists(["calculate"]) and there_exists(["plus","minus","into","by","power","raise","+","-","*","/","x","mod"])) and there_does_not_exist(["exit","to","what is","what's","bye","excel","add","subtract","multiply","divide","and","powerpoint"]):
            oprs = voice_data.split()
            if len(oprs)==4:
                res = eval_binary_expr(oprs[1],oprs[2],oprs[3])
                if res is True:
                    engine_speak("Sorry,cannot perform the operation")
                elif res is not None:
                    if type(res)==float: #isinstance(res,float):
                        res= round(res,4)
                    engine_speak(res)
            else:
                engine_speak("I did not get that. Could you please repeat?")  
                start()  
    
        elif there_exists(["add","subtract","multiply","divide","raise"]) and there_does_not_exist(["to","what is","what's","calculate","multiplied by","divided by","raised to","from","into"]):
            opr = voice_data.split()
            if len(opr)==4:
                result = eval_binary_expr(opr[1], opr[0], opr[3])
                if result is True:
                    engine_speak("Sorry,cannot perform the operation")
                elif result is not None:
                    if type(result)==float: #isinstance(res,float):
                        result= round(result,4)
                    engine_speak(result)
            else:
                engine_speak("I did not get that. Could you please repeat?")
                start()  

        elif there_exists(["multiplied by","divided by","raised to","raise to"]) and there_does_not_exist(["what is","what's"]):
            opr = voice_data.split()
            if len(opr)==4:
                result = eval_binary_expr(opr[0], opr[1], opr[3])
                if result is True:
                    engine_speak("Sorry,cannot perform the operation")
                elif result is not None:
                    if type(result)==float: #isinstance(res,float):
                        result= round(result,4)
                    engine_speak(result)
            elif len(opr)==5:
                result = eval_binary_expr(opr[1], opr[2], opr[4])
                if result is True:
                    engine_speak("Sorry,cannot perform the operation")
                elif result is not None:
                    if type(result)==float: #isinstance(res,float):
                        result= round(result,4)
                    engine_speak(result)        
            else:
                engine_speak("I did not get that. Could you please repeat?")
                start()             
        
        elif there_exists(["subtract"]) and there_exists(["from"]):
            opr2 = voice_data.split()
            if len(opr2)==4:
                result2 = eval_binary_expr(opr2[3],opr2[0],opr2[1])
                if result2 is True:
                    engine_speak("Sorry,cannot perform the operation")
                elif result2 is not None:
                    if type(result2)==float: #isinstance(res,float):
                        result2= round(result2,4)
                    engine_speak(result2)
            else:
                engine_speak("I did not get that. Could you please repeat?")
                start()  

        elif there_exists(["add"]) and there_exists(["to"]):
            opr3 = voice_data.split()
            if len(opr3)==4:
                result3 = eval_binary_expr(opr3[1],opr3[0],opr3[3])
                if result3 is True:
                    engine_speak("Sorry,cannot perform the operation")
                elif result3 is not None:
                    if type(result3)==float: #isinstance(res,float):
                        result3= round(result3,4)
                    engine_speak(result3)
            else:
                engine_speak("I did not get that. Could you please repeat?")
                start()  

        elif there_exists(["multiply"]) and there_exists(["to","into"]):
            opr3 = voice_data.split()
            if len(opr3)==4:
                result3 = eval_binary_expr(opr3[1],opr3[0],opr3[3])
                if result3 is True:
                    engine_speak("Sorry,cannot perform the operation")
                elif result3 is not None:
                    if type(result3)==float: #isinstance(res,float):
                        result3= round(result3,4)
                    engine_speak(result3)
            else:
                engine_speak("I did not get that. Could you please repeat?")
                start()          
        
        elif there_exists(["how many degrees is","radians is", "radian is"]):
            search_term = voice_data.replace("how","").replace("many","").replace("degrees","").replace("degree","").replace("is","").replace("radians","").replace("radian","")
            try:
                search_term = float(search_term)
                if(math.floor(search_term)==math.ceil(search_term)):
                    search_term = int(search_term)
                #else:
                    #pass #engine_speak("I did not get that. Could you please repeat?")
                engine_speak(round(math.degrees(search_term),4))
            except ValueError as ve:
                engine_speak("Please provide valid numbers.")
                start()      

        elif there_exists(["in degrees","in degree"]):
            search_term = voice_data.split()
            try: 
                search_term[0] = float(search_term[0])
                if(math.floor(search_term[0])==math.ceil(search_term[0])):
                    search_term[0] = int(search_term[0])
                #else:
                    #engine_speak("I did not get that. Could you please repeat?")
                engine_speak(round(math.degrees(search_term[0]),4))  
            except ValueError as ve:
                engine_speak("Please provide valid numbers.")
                start()       

        elif there_exists(["how many radians is","degrees is","degree is"]):
            search_term = voice_data.replace("how","").replace("many","").replace("degrees","").replace("degree","").replace("is","").replace("radians","").replace("radian","")
            try: 
                search_term = float(search_term)
                if(math.floor(search_term)==math.ceil(search_term)):
                    search_term = int(search_term)
                #else:
                    #engine_speak("I did not get that. Could you please repeat?")
                engine_speak(round(math.radians(search_term),4))
            except ValueError as ve:
                engine_speak("Please provide valid numbers.")
                start()          

        elif there_exists(["in radians","in radian"]):
            search_term = voice_data.split()
            try:
                search_term[0] = float(search_term[0])
                if(math.floor(search_term[0])==math.ceil(search_term[0])):
                    search_term[0] = int(search_term[0])
                else:
                    engine_speak("I did not get that. Could you please repeat?")
                engine_speak(round(math.radians(search_term[0]),4))
            except ValueError as ve:
                engine_speak("Please provide valid numbers.") 
                start()     
        
        elif there_exists(["factorial of"]):
            operator = voice_data.split("of")[-1]
            operator = float(operator)
            if(math.floor(operator)==math.ceil(operator)):
                result = math.factorial(int(operator))
                operator = int(operator)
                engine_speak("factorial of " + str(operator) + " is " + str(result))
            else:
                engine_speak("Please provide an integer number")
                record_audio("Listening")  

        #meaning of a word
        elif there_exists(["what is the meaning of","what's the meaning of","meaning of"]):
            try:
                word = voice_data.split("of")[-1]
                dict = PyDictionary()  
                meaning = dict.meaning(word)
                print(meaning)
                if ('Noun' in meaning.keys() or 'Verb' in meaning.keys() or 'Adverb' in meaning.keys() or 'Adjective' in meaning.keys()):
                    if 'Noun' in meaning.keys():
                        engine_speak("Noun: " + meaning['Noun'][0] + "\n")
                    if 'Verb' in meaning.keys():     
                        engine_speak("Verb: " + meaning['Verb'][0] + "\n")
                    if 'Adverb' in meaning.keys():     
                        engine_speak("Adverb: "+ meaning['Adverb'][0] + "\n")
                    if 'Adjective' in meaning.keys():     
                        engine_speak("Adjective: "+ meaning['Adjective'][0] + "\n")   
                else:
                    engine_speak(meaning)           
            except AttributeError:
                engine_speak("Try saying what is " + word)        

        #meaning of word
        elif there_exists(["what does"]) and there_exists(["mean"]):
            try:
                word = voice_data.split()
                dict = PyDictionary()        
                meaning = dict.meaning(word[2])
                print(meaning)
                if ('Noun' in meaning.keys() or 'Verb' in meaning.keys() or 'Adverb' in meaning.keys() or 'Adjective' in meaning.keys()):
                    if 'Noun' in meaning.keys():
                        engine_speak("Noun: " + meaning['Noun'][0])
                    if 'Verb' in meaning.keys():     
                        engine_speak("Verb: " + meaning['Verb'][0])
                    if 'Adverb' in meaning.keys():     
                        engine_speak("Adverb: "+ meaning['Adverb'][0])
                    if 'Adjective' in meaning.keys():     
                        engine_speak("Adjective: "+ meaning['Adjective'][0])   
                else:
                    engine_speak(meaning)    
            except AttributeError:
                engine_speak("Try saying what is " + word)
                start()               
    
        
        #elif there_exist(["translate"]):
        #    try:
        #        search_term = voice_data.replace("translate","").replace("to","").replace("how to say","").replace("in","").replace("how to say","")
        #
                
        #translate
        elif there_exists(["in hindi"]) and there_does_not_exist(["google"]):
            try:
                word = voice_data.replace("in hindi","").replace("translate","").replace("can you","").replace("how to say","")
                translated_word = EngtoHindi(word).convert
                if translated_word is not None:
                    print(translated_word)
                    engine_speak(translated_word)
                else:
                    engine_speak("Try saying, flower in hindi, or try saying translate flower to hindi.")
            except TypeError:
                engine_speak("Try saying, flower in hindi, or try saying translate flower to hindi.")    
        
        #translate
        elif there_exists(["to hindi"]) and there_does_not_exist(["google"]):
            try: 
                word = voice_data.replace("to hindi","").replace("translate","").replace("can you","").replace("how to say","")
                translated_word = EngtoHindi(word)
                res=translated_word.convert
                if res is not None:
                    print(res)
                    engine_speak(res)
                else:
                    engine_speak("Try saying, flower to hindi, or try saying translate flower to hindi.")
            except TypeError:
                engine_speak("Try saying, flower to hindi, or try saying translate flower to hindi.") 

        #translate to something    
        elif there_exists(["translate"]) and there_does_not_exist(["hindi"]):
            sentence = voice_data
            print(sentence + "1")
            language = sentence.split("in")[-1].strip() 
            search_term = voice_data.replace("translate","").replace("to","").replace("how to say","").replace("in","").replace("how to say","").replace("english","").replace("french","").replace("chinese","")
            url = "https://translate.google.co.in/?sl=auto&tl="+get_language(language)+"&text="+search_term+"&op=translate"
            webbrowser.get().open(url)           
            engine_speak("Here is your translation")

        #tell me about something
        elif there_exists(["tell me about"]):
            statement = voice_data.replace("tell me about","")
            try:
                engine_speak("Searching...")
                results = wikipedia.summary(statement,sentences=3)    
                print(results)
                engine_speak(results) 
            except Exception:
                print("Problem")
                engine_speak("Try saying what is" + statement)

        elif there_exists(["who is the","who's the"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.")
   
        #who is 
        elif there_exists(["who is","who's"]) and there_does_not_exist(["tell me","tell me about"]):
            statement = voice_data.replace("who is","").replace("who's","")
            try:
                engine_speak(wikipedia.summary(statement,sentences=3))        
            except wikipedia.exceptions.PageError:
                engine_speak("Try once again")

        #Take a screenshot
        elif there_exists(["capture","my screen","screenshot"]) and "photo" not in voice_data:
            time.sleep(2)
            myScreenshot = pyautogui.screenshot()
            path = r"C://Users//Sakshi//Documents//Dora"
            path1 = r"C://Users//Sakshi//Documents//Dora//Screenshots"
            today = datetime.datetime.now()
            date = today.strftime("%b%d%Y")
            time1=datetime.datetime.now().strftime("%H%M%S")
            filename = "screen" + date + time1 + ".png"
            if not (os.path.isdir(path)):
                os.mkdir(path,0o666)  
            if not (os.path.isdir(path1)):
                os.mkdir(path1,0o666)  
            completepath = os.path.join(path1,filename)
            myScreenshot.save(completepath)
            engine_speak("Done")
            
        #search wikipedia for definition
        elif there_exists(["search"]) and 'wikipedia' in voice_data:
            engine_speak('Searching Wikipedia...')
            statement = voice_data.replace("wikipedia","").replace("on","").replace("for","").replace("search","")
            #statement = voice_data.split("for")[-1]
            #statement = statement.replace("on wikipedia","")
            results = wikipedia.summary(statement, sentences=3)
            engine_speak("According to Wikipedia")
            print(results)
            engine_speak(results)

        #open stackoverflow
        elif there_exists(["open stackoverflow", "stack overflow","stackoverflow"]):
            url = "https://stackoverflow.com"
            webbrowser.get().open(url)
            engine_speak("Here is stackoverflow")

        #show news
        elif there_exists(["news","headline","headlines"]):                             # voice_data == "news":
            url = "https://timesofindia.indiatimes.com/home/headlines"
            webbrowser.get().open(url)
            engine_speak('Here are some headlines from the Times of India,Happy reading')
            #time.sleep(6)

        #take a photo
        elif there_exists(["camera","take a photo","picture","photo"]) and "google" not in voice_data:
            ec.capture(0,False,"img.jpg")

        #video capture
        elif there_exists(["video", "take a video"]):
            ec.auto_vidcapture(0,False,"Demo.avi",5)    

        # Current city or region    
        elif there_exists(["where am i"]):
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)
            region=data['region']
            city=data['city']
            engine_speak(f"You must be somewhere in {city},{region}")
    
        #Current location as per Google maps
        elif there_exists(["what is my exact location", "what is my location", "what's my location", "find me"]):
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            engine_speak("You must be somewhere near here, as per Google maps")    

        #play music
        elif there_exists(["play music","play song","play a song"]) and there_does_not_exist(["youtube"]):  
            engine_speak("Here you go with music")
            music_dir = "C://Users//Sakshi//Music//Video Projects"
            songs = os.listdir(music_dir)
            print(songs)   
            os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs)-1)]))

        #who made you
        elif there_exists(["who made you","who created you"]):
            engine_speak("I have been created by Pakhi, Saniddhi, Sakshi and Tejaswini")

        #Tell a joke
        elif there_exists(["joke"]):
            engine_speak(pyjokes.get_joke(category="all"))  

        #Tell me random facts
        elif there_exists(["fact"]):
            engine_speak(randfacts.get_fact())      

        #who am i
        elif there_exists(["who am i"]):
            engine_speak("If you talk then definitely you are human.")
        
        #who are you
        elif there_exists(["who are you"]): 
            engine_speak("I am your virtual assistant. How can I help you?")

        #open quora
        elif there_exists(["open quora", "quora"]):
            url = "https://www.quora.com/"
            webbrowser.get().open(url)
            engine_speak("Here is Quora")    

        #open Wikipedia
        elif there_exists(["open wiki", "open wikipedia", "wikipedia", "wiki"]) and there_does_not_exist(["search"]):
            url = "https://www.wikipedia.org/"
            webbrowser.get().open(url)
            engine_speak("Here is Wikipedia")

        #open powerpoint
        elif there_exists(["create powerpoint","open powerpoint","open ppt", "open ms powerpoint","open microsoft powerpoint"]):
            engine_speak("opening Power Point presentation")
            power = r"C://Program Files//Microsoft Office//root//Office16//POWERPNT.exe"
            os.startfile(power)  

        #open word document
        elif there_exists(["create word","open word","word","word doc","open word document","open ms word","open microsoft word"]) and 'wordpad' not in voice_data:
            engine_speak("Opening Microsoft Word")
            doc = r"C://Program Files//Microsoft Office//root//Office16//WINWORD.exe"
            os.startfile(doc)

        #open excel
        elif there_exists(["create excel","open excel","excel sheet", "excel","open ms excel","open microsoft excel"]):
            engine_speak("Opening Microsoft Excel")
            excel = r"C://Program Files//Microsoft Office//root//Office16//EXCEL.exe"
            os.startfile(excel)  

        #open onenote
        elif there_exists(["create onenote","open onenote","onenote", "one note"]):
            engine_speak("Opening Onenote")
            onenote = r"C://Program Files//Microsoft Office//root//Office16//ONENOTE.exe"
            os.startfile(onenote)

        #open notepad
        elif there_exists(["create notepad","open notepad","notepad", "note pad"]):
            engine_speak("Opening Notepad")
            notepad = r"C://Windows//system32//notepad.exe"
            os.startfile(notepad)  

        #open paint
        elif there_exists(["open paint","paint","open ms paint", "open microsoft paint"]):
            engine_speak("Opening Paint Application")
            paint = r"C://Windows//system32//mspaint.exe"
            os.startfile(paint)    
    
        #open calculator
        elif there_exists(["open calc","calculator","calc","open calculator"]) and there_does_not_exist(["calculate"]):
            engine_speak("Opening Calculator")
            cal = r"C://Windows//system32//calc.exe"
            os.startfile(cal)

        #open wordpad
        elif there_exists(["open wordpad","wordpad"]):
            engine_speak("Opening Wordpad")
            wrdpad = r"C://Program Files//Windows NT//Accessories//wordpad.exe"
            os.startfile(wrdpad) 

        #open Google Docs
        elif there_exists(["open google doc", "google document", "google doc"]) and there_does_not_exist(["create","new"]):
            url = "https://www.google.com/docs/about/"
            webbrowser.get().open(url)
            engine_speak("Here is Google docs") 

        #create Google Docs
        elif there_exists(["create google doc", "create google document", "new google doc"]) and "open" not in voice_data :
            url = "https://docs.google.com/document/u/0/?tgif=d"
            webbrowser.get().open(url)
            engine_speak("Here is your Google doc")    

        #open Google Sheets
        elif there_exists(["open google sheet", "google sheets", "google sheet","open sheet"]) and there_does_not_exist(["create","new"]):
            url = "https://www.google.com/sheets/about/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Sheets")

        #create Google Sheets
        elif there_exists(["create google sheet", "new google sheet", "create sheet", "new sheet"]) and "open" not in voice_data :
            url = "https://docs.google.com/spreadsheets/u/0/?tgif=d"
            webbrowser.get().open(url)
            engine_speak("Here is your Google Sheets")    

        #open Google Slides
        elif there_exists(["open google slide", "google slide", "google slides","slides"]) and there_does_not_exist(["create","new"]):
            url = "https://www.google.com/slides/about/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Slides")

        #create Google Slides
        elif there_exists(["create google slide", "new google slide"]) and "open" not in voice_data :
            url = "https://docs.google.com/presentation/u/0/?tgif=d"
            webbrowser.get().open(url)
            engine_speak("Here is your Google Slide")

        #open Google Forms
        elif there_exists(["open google forms", "google form", "g form","gform","form"]) and there_does_not_exist(["create","new"]):
            url = "https://www.google.com/forms/about/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Forms")

        #create Google Forms
        elif there_exists(["create google form", "new google form", "create g form","new gform","create form","new form"]) and "open" not in voice_data :
            url = "https://docs.google.com/forms/u/0/?tgif=d"
            webbrowser.get().open(url)
            engine_speak("Here are Google Forms")       

        #open Google Maps
        elif there_exists(["open google map", "google maps", "map"]):
            url = "https://www.google.com/maps/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Maps")

        #open Google Meet
        elif there_exists(["open google meet", "google meet", "meet", "google meeting"]): 
            url = "https://meet.google.com/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Meet") 

        #open Zoom
        elif there_exists(["open zoom", "zoom"]): 
            url = "https://zoom.us/"
            webbrowser.get().open(url)
            engine_speak("Here is Zoom")

        #open Google Classroom
        elif there_exists(["open google classroom", "classroom","gc","g c", "google classroom","google class"]): 
            url = "https://classroom.google.com/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Classroom")

        #open Google Calendar
        elif there_exists(["open google calendar", "calendar","google calendar"]): 
            url = "https://www.google.com/calendar/about/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Calendar")

        #open Google Translate
        elif there_exists(["open google translate","translator"]) and there_does_not_exist(["hindi"]): 
            url = "https://translate.google.co.in/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Translate")

        #open Whatsapp Web
        elif there_exists(["open whatsapp", "whatsapp","whatsapp web"]): 
            url = "https://web.whatsapp.com/"
            webbrowser.get().open(url)
            engine_speak("Here is Whatsapp Web")     

        #open Google Drive
        elif there_exists(["open google drive", "drive","google drive"]) and there_does_not_exist(["com","where is","where's","find","locate"]): 
            url = "https://www.google.com/intl/en_in/drive/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Drive")

        #open Google Photos
        elif there_exists(["open google photos","google photo"]): 
            url = "https://www.google.com/photos/about/"
            webbrowser.get().open(url)
            engine_speak("Here is Google Photos")

        #locate
        elif there_exists(["where is","find", "locate"]) and "me" not in voice_data:
            query = voice_data.replace("where is","").replace("where's","").replace("find","").replace("me","").replace("locate","")
            location = query
            engine_speak("User asked to Locate")
            engine_speak(location)
            url = "https://www.google.com/maps/search/" + location + ""
            webbrowser.get().open(url)    

        #open Cowin portal
        elif there_exists(["open cowin","cowin website","cowin","cowin portal","vaccine","vaccination","co win"]): 
            url = "https://www.cowin.gov.in/"
            webbrowser.get().open(url)
            engine_speak("Here is Cowin website")

        #World covid updates
        elif there_exists(["covid updates","covid 19","corona","coronavirus","pandemic"]): 
            url = "https://www.worldometers.info/coronavirus/"
            webbrowser.get().open(url)
            engine_speak("Here are Covid updates")     
            
        #shutdown the laptop
        elif there_exists(['shutdown system','shutdown']):
            engine_speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown /p /f')   #shutdown /s /t 0

        #restart the laptop
        elif there_exists(["restart"]):
            subprocess.call(["shutdown", "/r"])

        #hibernation     
        elif there_exists(["hibernate"]) or there_exists(["sleep"]):
            engine_speak("Hibernating")
            subprocess.call("shutdown /h")    

        #empty recycle bin
        elif there_exists(['empty recycle bin']):
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            engine_speak("Recycle Bin Recycled")

        #lock the device
        elif there_exists(["lock the device","lock","lock window"]):
            engine_speak("locking the device")
            ctypes.windll.user32.LockWorkStation()    

        #increase the brightness of the screen
        elif there_exists(["increase the brightness","increase brightness"]):
            engine_speak("Increasing the brightness of the screen")
            brightness = sbc.get_brightness()
            sbc.set_brightness(brightness+5,display=0)

        #decrese the brightness of the screen
        elif there_exists(["decrease the brightness","decrease brightness"]):
            engine_speak("Decreasing the brightness of the screen")
            brightness = sbc.get_brightness()
            sbc.set_brightness(brightness-10,display=0)

        #launch google chrome
        elif there_exists(["launch chrome","open browser","browser","google chrome","launch google chrome","open google chrome","chrome"]):
            chrome = r"C://Program Files//Google//Chrome//Application//chrome.exe"
            os.startfile(chrome)  
            engine_speak("Google chrome is open now")
        #thank you
        elif there_exists(["thanks","thank you","thankyou"]):
            Thankyou = ["It is my pleasure" + person_obj.name,"You are welcome" + person_obj.name,"Don't mention it" + person_obj.name]
            engine_speak(Thankyou[random.randint(0,len(Thankyou)-1)])

        #farewell
        elif there_exists(["exit", "quit", "goodbye","bye","stop"]) and there_does_not_exist(["listen","listening"]):
            hour=datetime.datetime.now().hour
            if (hour>=20 and hour<24) or (hour>=0 and hour<4):
                engine_speak("Good Night. Logging off")
                print("Good Night.Logging off")
            else:
                farewell = ["Goodbye " + person_obj.name, "See you " + person_obj.name, "Adieu " + person_obj.name, "have a nice day " + person_obj.name, "see you later " + person_obj.name, "milte hain " + person_obj.name, "Bye, take care " + person_obj.name]
                end = farewell[random.randint(0,len(farewell)-1)]
                engine_speak(end)
            exit()      

        #don't listen
        elif there_exists(["don't listen","stop listening","wait"]):
            engine_speak("For how many seconds do you want to stop me from listening to you?") 
            try:
                a = record_audio("Listening").replace("seconds","")
                a=int(a)
                print(a) 
                engine_speak("I will rest now for " + str(a) + " seconds")  
                time.sleep(a)
                start()
            except ValueError as ve:
                engine_speak("Try again saying 10 seconds")

        #good morning,good evening,good night
        elif there_exists(["good"]) and there_exists(["morning"]):
            wishMe()
        elif there_exists(["good"]) and there_exists(["afternoon"]):
            wishMe()
        elif there_exists(["good"]) and there_exists(["evening"]):
            wishMe()
        elif there_exists(["good"]) and there_exists(["night"]):
            hour=datetime.datetime.now().hour
            if (hour>=20 and hour<=24) or (hour>=0 and hour<=4):
                engine_speak("Good night" + person_obj.name)
                
        #greeting
        elif there_exists(['hey','hello']) and there_does_not_exist(["youtube","google","wikipedia","search","play","hindi"]):
            greetings = ["Hey, how can I help you" + person_obj.name, "Hey, what's up?" + person_obj.name, "Hey, I'm listening" + person_obj.name, "How can I help you?" + person_obj.name, "Hello" + person_obj.name]
            greet = greetings[random.randint(0,len(greetings)-1)]
            engine_speak(greet)

        #what is your name
        elif there_exists(["what is your name","what's your name","tell me your name"]):
            if person_obj.name:
                engine_speak(f"My name is {asis_obj.name}, thanks for asking, {person_obj.name}") #gets users name from voice input
            else:
                engine_speak(f"My name is {asis_obj.name}. What's your name?") #incase you haven't provided your name.
                voice_data = record_audio("Listening")
                person_name = voice_data.replace("my name is ","")
                engine_speak("That's a beautiful name " + person_name + ". Nice to know you!")
                person_obj.setName(person_name) # remember name in person object
            
        #name of the user
        elif there_exists(["my name is"]):
            person_name = voice_data.split("is")[-1].strip()
            engine_speak("That's a beautiful name " + person_name + ". Nice to know you!")
            person_obj.setName(person_name) # remember name in person object
        
        #asking name of the user
        elif there_exists(["what is my name","what's my name"]):
            if (person_obj.name):
                engine_speak("Your name is " + person_obj.name)
            else:
                engine_speak("You haven't told me your name.")        
        
        #changing name of the assistant
        elif there_exists(["your name should be","your name must be","your name should now be"]):
            asis_name = voice_data.split("be")[-1].strip()
            engine_speak("Okay, i will remember that. My name is " + asis_name)
            asis_obj.setName(asis_name) # remember name in asis object

        #changing name of assistant 2
        elif there_exists(["change name","change your name"]):  
            engine_speak("What would you like to call me?")
            voice_data = record_audio("Listening") 
            asis_name = voice_data.split("you")[-1].strip()
            engine_speak("Okay, I will remember that. My name is " + asis_name)
            asis_obj.setName(asis_name) # remember name in asis object

        #asking the assistant it's well-being
        elif there_exists(["how are you","how are you doing"]):
            feeling = ["I m fine, after all I am hanging out with you.","I'm very well, thanks for asking " + person_obj.name +".How are you?","I am great " + person_obj.name +".How are you?"]
            feel = feeling[random.randint(0,len(feeling)-1)]
            engine_speak(feel)
        
        #reply of the user for how are you
        elif there_exists(["fine","i am good","i'm good","well","good","happy"]) and there_does_not_exist(["how", "when", "what", "why", "bye","not","unhappy","morning","evening","afternoon","night"]):
            feeling = ["That's great!", "Nice to know that.","Good to know that you are doing well.","Good to know that you are fine."]
            feel = feeling[random.randint(0,len(feeling)-1)]
            engine_speak(feel) 

        #I am not fine
        elif there_exists(["not fine","not well","not good","unhappy","not happy","sad"]) and there_does_not_exist(["how", "when", "what", "why", "bye","morning","evening","afternoon","night"]):
            feeling = ["What should I do to make you feel better?","How can I help you?","How can I make you happy?","What can I do for you?","If you want happiness take a nap"]
            feel = feeling[random.randint(0,len(feeling)-1)]
            engine_speak(feel)      
                
        #make a note
        elif there_exists(["make a note","take a note","remember my idea","remember","note"]):
            path = r"C://Users//Sakshi//Documents//Dora"
            path2 = r"C://Users//Sakshi//Documents//Dora//Notes"
            engine_speak("What should i note")
            today = datetime.datetime.now()
            date = today.strftime("%b%d%Y")
            time1=datetime.datetime.now().strftime("%H%M%S")
            filename = "dora_note" + date + time1 + ".txt"
            if not (os.path.isdir(path)):
                os.mkdir(path,0o666)  
            if not (os.path.isdir(path2)):
                os.mkdir(path2,0o666)  
            completepath = os.path.join(path2,filename)
            file = open(completepath,"w")
            file.write(record_audio("Listening"))
            file.close()    
            engine_speak("Noted")
            os.startfile(os.path.join(path2,filename))   
            #subprocess.Popen(["notepad",filename])   

        #what is
        elif there_exists(["what is","what's"]):
            search_term = voice_data.replace("what is","").replace("what's","").replace("on google","").replace("browse","")
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found for " + search_term)

        #how
        elif there_exists(["how", "how to", "how can"]) and there_does_not_exist(["tell me","are you","are you doing","show my timetable","many degrees","many radians"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.")

        #when
        elif there_exists(["when"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.")

        #tell me
        elif there_exists(["tell me"]) and there_does_not_exist(["day","fact","your","name","about","joke","today","month","date"]):
            search_term = voice_data.replace("tell me","")
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.")  
        
        elif there_exists(["why"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.") 

        elif there_exists(["where"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.") 

        elif there_exists(["which"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.") 

        elif there_exists(["who"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.") 

        elif there_exists(["whose"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.") 

        elif there_exists(["whom"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.") 

        elif there_exists(["what kind"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.") 

        elif there_exists(["what"]):
            search_term = voice_data
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            engine_speak("Here is what I found.") 

        elif there_exists(["file explorer","file manager"]):
            file=easygui.fileopenbox()
            
        else:
            engine_speak("Sorry, You may refer at the tasks I can perform.")     

#time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Dora'
person_obj.name = ""

engine = pyttsx3.init()
r = sr.Recognizer() # initialise a recogniser     

root = tk.Tk()
#root.geometry('800x800')
#root.attributes('-fullscreen', True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title('Voice Assistant')
f = ("Times bold", 15)

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True)

# create frames
tab1 = ttk.Frame(notebook, width=800, height=800)
tab2 = ttk.Frame(notebook, width=800, height=800)
tab3 = ttk.Frame(notebook, width=800, height=800)
tab4 = ttk.Frame(notebook, width=800, height=800)

tab1.pack(fill='both', expand=True)
tab2.pack(fill='both', expand=True)
tab3.pack(fill='both', expand=True)
tab4.pack(fill='both', expand=True)

s=ttk.Style()
s.configure('TNotebook.Tab',font='50')

# add frames to notebook
notebook.add(tab1, text='Welcome')
notebook.add(tab2, text='Notes')
notebook.add(tab3, text='Screenshots')
notebook.add(tab4, text='Things to Try')

#listbox for notes
lbox = Listbox(tab2,activestyle='dotbox',font=font.Font(size=12,weight='bold'),width=35, bg='#DAF7A6' )
lbox.place()
scrollbar = Scrollbar(lbox, orient=VERTICAL)
for items in files:
        lbox.insert(END,items)
lbox.config(yscrollcommand=scrollbar.set)   
scrollbar.config(command=lbox.yview)   
text = Text(tab2, bg='#D55FD1',font=font.Font(size=16,weight='bold'))
lbox.pack(side=LEFT,expand=True,fill=BOTH)
scrollbar.pack(side=RIGHT,fill=BOTH)
text.pack(side=LEFT,expand=True,fill=BOTH)  
lbox.bind("<<ListboxSelect>>", showcontent)

#listbox for screenshots
lbox2 = Listbox(tab3,activestyle='dotbox',font=font.Font(size=12,weight='bold'),bg='#DAF7A6')
lbox2.pack(side=LEFT,expand=True,fill=BOTH)
scrollbar2 = Scrollbar(lbox2, orient=VERTICAL)
lbox2.config(yscrollcommand=scrollbar2.set)   
scrollbar2.config(command=lbox2.yview)   
scrollbar2.pack(side=RIGHT,fill=BOTH)
lbox2.bind("<<ListboxSelect>>", showimage)
for items2 in ss:
        lbox2.insert(END,items2)
canvas = Canvas(tab3,bg='black')
canvas.config(width=1544, height=1000)
canvas.pack()

#Button(tab2, text = "List all Files in Directory", command = showcontent).pack(fill=BOTH, expand=True, side=TOP)
Button(tab1, text="Tap to speak", font=font.Font(size=22,weight='bold'), fg='white',activebackground='white', activeforeground='#B551C6', bd=8, bg='#634069',height=1,command=lambda:threading.Thread(target=start).start()).pack(fill=BOTH,side=TOP) 
label = Label(tab1, bg= '#B551C6',font=font.Font(size=22,weight='bold'),height=14) #bg='black'
label1 = Label(tab1, bg= 'white',font=font.Font(size=22,weight='bold'),height=1) #bg='black'
label.pack(fill=BOTH,side=BOTTOM,expand=True) 
label1.pack(fill=BOTH,side=BOTTOM,expand=True) 
wake = Button(tab1, text="Wake word is off",font=font.Font(size=22,weight='bold'), fg='white', activebackground='white', activeforeground='#B551C6', bd=8, bg='#634069', height=1,command=lambda:threading.Thread(target=switch).start())
wake.pack(fill=BOTH,side=TOP) 
lbox3 = Listbox(tab4,activestyle='dotbox',font=font.Font(size=12,weight='bold'),bg='#DAF7A6')
lbox3.pack(side=LEFT,fill=BOTH)
Tasks = Label(tab4,bg='white')
Tasks.pack(side=LEFT,fill=BOTH,expand=True)
lbox3.insert(END,"Desktop Apps")
lbox3.insert(END,"Websites")
lbox3.insert(END,"Search Questions")
lbox3.insert(END,"General info")
lbox3.insert(END,"Entertainment")
lbox3.insert(END,"Google Apps")
lbox3.insert(END,"Web Apps")
lbox3.insert(END,"Utilities")
lbox3.insert(END,"News and Information")
lbox3.insert(END,"Calculations")
#scrollbar3 = Scrollbar(Tasks,orient=VERTICAL) 
#scrollbar3.pack(side=RIGHT,fill=BOTH)
lbox3.bind("<<ListboxSelect>>", tasks)

root.mainloop()
