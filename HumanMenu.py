# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:15:41 2020

@author: Sini
"""


import os

while True:
    print("Chat with me with your requirements:")
    p=input()
    
    if(("run" in p) or ("RUN" in p) or ("Run" in p) or
       ("execute" in p)or ("EXECUTE" in p) or ("Execute" in p)  or 
       ("launch" in p) or ("LAUNCH" in p) or ("Launch" in p) or 
       ("start" in p) or ("START" in p) or ("Start" in p) or 
       ("open" in p) or ("OPEN" in p) or ("Open" in p)) and (("Notepad" in p) or 
       ("NOTEPAD" in p) or ("notepad"in p)):
        os.system("notepad")
    elif(("run" in p) or ("RUN" in p) or ("Run" in p) or
       ("execute" in p)or ("EXECUTE" in p) or ("Execute" in p)  or 
       ("launch" in p) or ("LAUNCH" in p) or ("Launch" in p) or 
       ("start" in p) or ("START" in p) or ("Start" in p) or 
       ("open" in p) or ("OPEN" in p) or ("Open" in p)) and (("Explorer" in p) or 
       ("EXPLORER" in p) or ("explorer"in p)):
        os.system("explorer")
    elif(("run" in p) or ("RUN" in p) or ("Run" in p) or
       ("execute" in p)or ("EXECUTE" in p) or ("Execute" in p)  or 
       ("launch" in p) or ("LAUNCH" in p) or ("Launch" in p) or 
       ("start" in p) or ("START" in p) or ("Start" in p) or 
       ("open" in p) or ("OPEN" in p) or ("Open" in p)) and (("Control Panel" in p) or 
       ("CONTROL PANEL" in p) or ("control panel"in p)):
        os.system("control panel")
    elif (("do not run" in p) or ("don't run" in p) or ("DO NOT RUN" in p) or ("DON'T RUN" in p ) or
        ("do not execute" in p) or ("don't execute" in p) or ("DO NOT EXECUTE" in p) or ("DON'T EXECUTE" in p ) or
        ("do not start" in p) or ("don't start" in p) or ("DO NOT START" in p) or ("DON'T START" in p ) or
        ("do not launch" in p) or ("don't launch" in p) or ("DO NOT LAUNCH" in p) or ("DON'T LAUNCH" in p ) or
        ("do not open" in p) or ("don't open" in p) or ("DO NOT OPEN" in p) or ("DON'T OPEN" in p ) ):
        print("No execution as requested")
    elif (("exit" in p) or ("stop" in p) or ("quit" in p) or ("Exit" in p) or ("Stop" in p) or ("Quit" in p) or
        ("EXIT" in p) or ("STOP" in p) or ("QUIT" in p)):
        break
    else:
        print("Invalid command")
