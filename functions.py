### Synth Chris 666
### https://synthchrismusic.wixsite.com/music
### functions.py
### Assorted functions for generator.py to use and such

import random
from midiutil.MidiFile import MIDIFile

# returns int array[5] of random ints from [0,2]
def randStructGen():
    randInts = [0, 1, 2]
    structArr = []
    for i in range(0,5):
        if(i == 0):
            structArr.append(random.choice(randInts))
        else:
            # no repeats... unless it's a breakdown of course
            randInt = random.choice(randInts)
            while(randInt == structArr[i-1] and randInt != 2):
                randInt = random.choice(randInts)
            structArr.append(randInt)
    return structArr

# for some reason, I can't figure out using .extend() or .append()
# so I just made my own function reg[] to dest[]
def add(dest, reg):
    for i in range(len(reg)):
        for j in range(len(reg[i])):
            for k in range(len(reg[i][j])):
                dest[i][j].append(reg[i][j][k])
    
# choose a random verse structure
def verse(scale):
    randInt = random.randint(0, 4)
    if(randInt == 0):
        return v0(scale)
    if(randInt == 1):
        return v1(scale)
    if(randInt == 2):
        return v2(scale)
    if(randInt == 3):
        return v3(scale)
    if(randInt == 4):
        return v4(scale)

# choose a random chorus structure
def chorus(scale, index):
    if(index == 0):
        return c0(scale)
    if(index == 1):
        return c1(scale)
    if(index == 2):
        return c2(scale)
    if(index == 3):
        return c3(scale)
    if(index == 4):
        return c4(scale)
    
#choose a random breakdown structure
def breakdown(scale):
    randInt = random.randint(0, 4)
    if(randInt == 0):
        return b0(scale)
    if(randInt == 1):
        return b1(scale)
    if(randInt == 2):
        return b2(scale)
    if(randInt == 3):
        return b3(scale)
    if(randInt == 4):
        return b4(scale)

def getChordProgressionIndices():
    s = open("chords.txt","r")
    m = s.readlines()
    l = []
    for i in range(0, len(m) - 1):
        x = m[i]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[i + 1])
    o = random.choice(l)

    chords = []
    for i in range(0, len(o)):
        chords.append(int(o[i]) - 1)

    random.shuffle(chords)
    return chords

def getChordProgression(scale):
    chords = getChordProgressionIndices()
    for i in range(0, len(chords)):
        if len(scale[0]) > chords[i]:
            chords[i] = scale[0][chords[i]]
        else:
            chords[i] = scale[0][0]
    return chords

def getFileName():
    # read in fileName.txt
    # increment it
    # write that number to the file and return that as a string for the filename
    prevInt = (open("fileName.txt", "r").read())
    fileInt = str(int((open("fileName.txt", "r").read())) + 1)
    fout = open("fileName.txt", "w")
    fout.write(fileInt)
    return "./midi/" + fileInt

def writeAndExport(listNotes):
    # multitrack midifile of 4 tracks
    # first track: guitar
    # second track: bass
    # third track: synth
    # fourth track: drums
    midiFile = MIDIFile(4)
    midiChannel = 0
    midiVolume = 127

    ### drums
    midiTrackBeatCounter = 0
    midiTrack = 0
    midiFile.addTrackName(midiTrack, 0, "Drum MIDI")
    for i in range(0, len(listNotes[3][0])):
        for j in range(0, len(listNotes[3]) - 1):
            if(listNotes[3][j][i] != -1):
                midiFile.addNote(midiTrack, midiChannel, listNotes[3][j][i], midiTrackBeatCounter, listNotes[3][3][i] * 4, midiVolume)
        midiTrackBeatCounter += listNotes[3][3][i] * 4

    ### guitar
    midiTrackBeatCounter = 0
    midiTrack = 1
    midiFile.addTrackName(midiTrack, 0, "Guitar MIDI")
    for i in range(0, len(listNotes[0][0])):
        for j in range(0, len(listNotes[0]) - 2):
            if(listNotes[0][j][i] != -1):
                midiFile.addNote(midiTrack, midiChannel, listNotes[0][j][i], midiTrackBeatCounter, listNotes[0][4][i] * 4, (listNotes[0][3][i] * 126) + 1)
        midiTrackBeatCounter += listNotes[0][4][i] * 4

    ### bass
    midiTrackBeatCounter = 0
    midiTrack = 2
    midiFile.addTrackName(midiTrack, 0, "Bass MIDI")
    for i in range(0, len(listNotes[1][0])):
        if(listNotes[1][0][i] != -1):
            midiFile.addNote(midiTrack, midiChannel, listNotes[1][0][i], midiTrackBeatCounter, listNotes[1][1][i] * 4, midiVolume)
        midiTrackBeatCounter += listNotes[1][1][i] * 4

    ### synth
    midiTrackBeatCounter = 0
    midiTrack = 3
    midiFile.addTrackName(midiTrack, 0, "Synth MIDI")
    for i in range(0, len(listNotes[2][0])):
        if(listNotes[2][0][i] != -1):
            midiFile.addNote(midiTrack, midiChannel, listNotes[2][0][i], midiTrackBeatCounter, listNotes[2][1][i] * 4, midiVolume)
        midiTrackBeatCounter += listNotes[2][1][i] * 4
        
    with open(getFileName() + '.mid', 'wb') as outf:
        midiFile.writeFile(outf)
