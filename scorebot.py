# coding: utf=8
from __future__ import division
import os
import sys
import time


class Task:

    def __init__(self, desc, boolean):
        self.desc = desc
        self.boolean = boolean
    def getDescription(self):
        return self.desc
    #returns true if a Task is done, false if it is not
    def isDone(self):
        if os.system(self.boolean) == 0:
            return True
        else:
            return False



def update():
	circle="&#1F534" # red circle
    #autogenerates a report with baked in html
    with open('/home/'+mainUser+'/Desktop/Task_Report.html', 'w') as f:
        f.write('<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1"> <style> * { box-sizing: border-box; } .column { float: left; padding: 10px; height: 1500px; } .left, .right { width: 25%; } .middle { width: 50%; } .row:after { content: ""; display: table; clear: both; }</style> </head> <body><div class="row"> <div class="column left" style="background-color:#0d60bf;"></div> <div class="row"> <div class="column middle" style="background-color:#fff;"><h1 style="text-align: center;"><span style="font-family: arial, helvetica, sans-serif;">Task Report</span></h1><h2 style="text-align: center;"><br /><span style="font-family: arial, helvetica, sans-serif;">'
                 + compTasks + ' out of ' + numTasks ' completed</span></h2><p> </p>')
        for i in allTasks:
            if i.isDone():
				circle="&#1F7E2" #green circle
        f.write('<p><span style="font-size: 10pt; font-family: arial, helvetica, sans-serif;">' + i.getDescription() + ' ' + circle + ' </span></p>')
        f.write('</div> <div class="row"> <div class="column right" style="background-color:#0d60bf;"></div> </body>'
                )
        f.write('<meta http-equiv="refresh" content="20">')
        f.write('<footer><h6>Henry Mackay</h6></footer>')


mainUser = 'analyst'
allTasks= [
Task('1: Create a file in /home/cyber/Downloads named "object" (do not include quotes in the file name)','[ -e /home/cyber/Downloads ]'),
Task('2: Edit the file you created in /home/cyber/Downloads to say "flag07" (do not include quotes in the file name)','[ "$(grep flag07 /home/cyber/Downloads/object)" ]'), 
Task('3: Create a directory in /edit named "directory with spaces" (do not include quotes in the directory name)','[ -e /edit/directory\ with\ spaces ]'),
Task('4: Remove the empty directory /home/cyber/trash'
Task('5: Remove the file /edit/pencil'
Task('6: Remove the directory /chair and everything in it'
Task('7: EMPTY the directory /train/shift'

    ]


numTasks = len(allTasks)

while True:
    compTasks = 0
    for i in allTasks:
        if i.isDone():
            compTasks = compTasks + 1
    update()
    #delay between each scoring loop
    time.sleep(60)
