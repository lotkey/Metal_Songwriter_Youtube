### Synth Chris 666
### https://synthchrismusic.wixsite.com/music
### test.pyw
### I use this file to test code I'm working on

import random
from midiutil.MidiFile import MIDIFile
from verses import v0, v1, v2, v3, v4
from breakdowns import b0, b1, b2, b3, b4
from choruses import c0, c1, c2, c3, c4
from functions import writeAndExport, getFileName, add, getChordProgression, randStructGen

def generate(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]

    randStruct = randStructGen()
    #int array of 0, 1, 2
    #0 = verse, 1 = chorus, 2 = breakdown
    choruses = [c0(scale), c1(scale), c2(scale), c3(scale), c4(scale)]
    chorus = choruses[random.randint(0, 4)]
    for i in range(0, len(randStruct)):
        if(randStruct[i] == 0):
            verses = [v0(scale), v1(scale), v2(scale), v3(scale), v4(scale)]
            add(listNotes, verses[random.randint(0, 4)])
        if(randStruct[i] == 1):
            add(listNotes, chorus)
        if(randStruct[i] == 2):
            breakdowns = [b0(scale), b1(scale), b2(scale), b3(scale), b4(scale)]
            add(listNotes, breakdowns[random.randint(0, 4)])

    writeAndExport(listNotes)
