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


allTasks= [
	Task('Configure Ubuntu software to be downloaded from main, universe, restricted and multiverse repositories','[ "$(grep "deb http://archive.ubuntu.com/ubuntu trusty main universe restricted multiverse" /etc/apt/sources.list)" ]'),
	Task('Configure security updates to be downloaded and installed immiditately',[ "$(grep Unattended-Upgrade /etc/apt/apt.conf.d/10periodic | grep 1)" ]')  
]


numTasks = len(allTasks)
mainUser="cyber"
while True:
    compTasks = 0
    for i in allTasks:
        if i.isDone():
            compTasks = compTasks + 1
    update()
    #delay between each scoring loop
    time.sleep(60)
