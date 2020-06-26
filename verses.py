### Synth Chris 666
### https://synthchrismusic.wixsite.com/music
### verses.py
### This file contains all the loose structures for verses

import random
from functions import getChordProgression

### 'The Browning' style riff
# Follow the synthesizer for a bit
# Open palm-muted chugs for a bit
# Repeat
def v0(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]

    for j in range(0, 2):
        for i in range(0, 16 * 4): # eighth notes for eight bars
            ### synth
            if(random.randint(0, 3) == 0 or i%8 == 0):
                # reinforce the key center
                randomNote = scale[0][0]
            else:
                randomNote = (random.choice(range(0, 2)) * 12) + random.choice(scale[0])
            listNotes[2][0].append(randomNote)
            listNotes[2][1].append(.125)

            ### guitar and bass
            if i%16 < 8:
                # mirror the synth but an octave lower
                listNotes[0][0].append(listNotes[2][0][i] - 12)
                listNotes[0][1].append(-1)
                listNotes[0][2].append(-1)
                listNotes[0][3].append(int(listNotes[2][0][i] != scale[0][0] or j != 0))
                # bass is octave lower than guitar
                listNotes[1][0].append(listNotes[2][0][i] - 24)
            else:
                # open note palm-muted chugs
                listNotes[0][0].append(scale[0][0] - 12)
                listNotes[0][1].append(scale[0][0] - 5)
                listNotes[0][2].append(-1)
                listNotes[0][3].append(0)
                # bass is octave lower than guitar
                listNotes[1][0].append(scale[0][0] - 24)
            listNotes[0][4].append(.125)
            listNotes[1][1].append(.125)

            ### drums
            listNotes[3][0].append(scale[1][0])
            if i%4 == 2 and j == 0:
                # snare on 2 and 4
                listNotes[3][1].append(scale[1][1])
            elif i%8 == 4 and j == 1:
                # snare on 3
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if i%2 == 0:
                # cymbals on 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)
            listNotes[3][3].append(.125)

    return listNotes

### Metalcore style riff
# Some stereotypical metalcore riffs have a chord pattern
# Guitarist palm-mutes the root notes and plays other open notes
# The other notes usually revolve around the 3rd but I'm not gonna worry about that
def v1(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]

    # build a basic four-'chord' structure
    chords = getChordProgression(scale)
    randomNote = 0
    
    for i in range(0, 2):
        for j in range(0, 16 * 4):

            ### guitar and bass
            randomNote = 0
            # get an int from 0-3 using integer division
            # use this int as an index for chords[] to get a 'chord' note
            chordNote = chords[(int)((j/8)/2)]
            # defaults to palm-mutes
            velocity = 0
            # reinforce 'chord' note
            if(random.randint(0,2) == 0 or j%8 == 0):
                randomNote = chordNote
                listNotes[3][0].append(scale[1][0])
                listNotes[1][0].append(randomNote - 24)
            else:
                # open notes
                velocity = 1
                while(randomNote < chordNote or randomNote > chordNote + 15):
                    randomNote = 12 * random.choice(range(0, 2)) + random.choice(scale[0])
                if(i == 0):
                    # kick and bass match every guitar note for the first rep
                    listNotes[3][0].append(scale[1][0])
                    listNotes[1][0].append(randomNote - 24)
                else:
                    # for the second rep they only reinforce the palm-muted root notes
                    listNotes[3][0].append(-1)
                    listNotes[1][0].append(-1)

            # arpeggiates the 3rd of the 'chord' note
            # the 3rd is the degree of the root + 2
            # 3rd of the 1st degree is the 3rd degree because 1 + 2 = 3
            # 3rd of the 2nd degree is the 4th degree, etc.
            synthIndex = ((scale[0].index(chordNote) + 2)%len(scale[0]))
            listNotes[2][0].append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(chordNote) + 2)/len(scale[0])))))
            listNotes[2][1].append(.125)
                    
            listNotes[3][3].append(.125)
            listNotes[0][0].append(randomNote - 12)
            listNotes[0][1].append(-1)
            listNotes[0][2].append(-1)
            listNotes[0][3].append(velocity)
            listNotes[0][4].append(.125)
            listNotes[1][1].append(.125)
            if j%4 == 2 and i == 0:
                # snare on every 2 and 4
                listNotes[3][1].append(scale[1][1])
            elif j%8 == 4 and i == 1:
                # snare on every 3
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if j%2 == 0:
                # cymbal on every 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)

    return listNotes
            
### Four-chord riff
# Four-chord progression
# Lots of palm-muting
# Sick arpeggiating synth
def v2(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]
    chords = getChordProgression(scale)
    chord = []

    for i in range(0, 2):
        for j in range(0, 16 * 4):
            chord.clear()
            rootNote = chords[(int)((j/8)/2)]
            chord.append(rootNote)

            # builds a chord from the root note
            # root + 2nd/3rd + 5th/6th
            for x in range(1, 3):
                synthIndex = ((scale[0].index(rootNote) + (x * 2))%len(scale[0]))
                chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + (x * 2))/len(scale[0])))))

            ### guitar
            if j%16 == 0:
                # reinforces the key center
                randomNote = scale[0][0] - 12
            else:
                # random note from the chord
                randomNote = random.choice(chord) - 12

            if i == 0:
                if random.randint(0, 5) == 0:
                    listNotes[0][0].append(randomNote + 12)
                else:
                    listNotes[0][0].append(randomNote)
                listNotes[0][1].append(-1)
                listNotes[0][2].append(-1)
                listNotes[0][3].append(random.randint(0, 1))
                listNotes[0][4].append(.125)
            else: # repeat the first rep
                for k in range(0, len(listNotes[0])):
                    listNotes[0][k].append(listNotes[0][k][j])

            ### synth
            # arpeggiates up and down the chord
            if not j%4 == 3:
                listNotes[2][0].append(chord[j%4])
            else:
                listNotes[2][0].append(chord[len(chord) - 2])
            listNotes[2][1].append(.125)

            ### bass
            # copies the guitar
            listNotes[1][0].append(listNotes[0][0][j] - 12)
            listNotes[1][1].append(.125)

            ### drums
            listNotes[3][0].append(scale[1][0])
            if j%4 == 2 and i == 0:
                # snare on 2 and 4
                listNotes[3][1].append(scale[1][1])
            elif j%8 == 4 and i == 1:
                # snare on 3
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if j%2 == 0:
                # cymbals on 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)
            listNotes[3][3].append(.125)

    return listNotes

def v3(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]
    chords = getChordProgression(scale)
    chord = []

    for i in range(0, 2):
        for j in range(0, 16 * 4):
            chord.clear()
            rootNote = chords[(int)((j/8)/2)]
            chord.append(rootNote)

            # builds a chord from the root note
            # root + 2nd/3rd + 5th/6th
            for x in range(1, 3):
                synthIndex = ((scale[0].index(rootNote) + (x * 2))%len(scale[0]))
                chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + (x * 2))/len(scale[0])))))

            if random.randint(0, 1) == 0:
                listNotes[0][0].append(rootNote - 12)
                listNotes[0][1].append(-1)
                listNotes[0][2].append(-1)
                listNotes[0][3].append(0)
                listNotes[0][4].append(.125)
                listNotes[1][0].append(rootNote - 24)
                listNotes[1][1].append(.125)
            else:
                randomNote = random.choice(chord)
                for k in range(0, 2):
                    listNotes[0][0].append(randomNote - 12)
                    listNotes[0][1].append(-1)
                    listNotes[0][2].append(-1)
                    listNotes[0][3].append(1)
                    listNotes[0][4].append(.0625)
                    listNotes[1][0].append(randomNote - 24)
                    listNotes[1][1].append(.0625)

            if i == 0:
                listNotes[3][0].append(-1)
                listNotes[3][0].append(scale[1][0])
                listNotes[3][1].append(scale[1][1])
                listNotes[3][1].append(-1)
                listNotes[3][2].append(scale[1][2])
                listNotes[3][2].append(-1)
                listNotes[3][3].append(.0625)
                listNotes[3][3].append(.0625)
            else:
                if j%8 == 4:
                    listNotes[3][1].append(scale[1][1])
                else:
                    listNotes[3][1].append(-1)
                listNotes[3][1].append(-1)
                if j%2 == 0:
                    listNotes[3][2].append(scale[1][2])
                else:
                    listNotes[3][2].append(-1)
                listNotes[3][2].append(-1)
                for i in range(0, 2):
                    listNotes[3][0].append(scale[1][0])
                    listNotes[3][3].append(.0625)

            if j%2 == 0:
                for l in range(0, 4):
                    if l == 3:
                        listNotes[2][0].append(chord[1])
                    else:
                        listNotes[2][0].append(chord[l])
                    listNotes[2][1].append(.0625)

    return listNotes

def v4(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]
    chords = getChordProgression(scale)
    chord = []

    for i in range(0, 2):
        for j in range(0, 16 * 4):
            chord.clear()
            rootNote = chords[(int)((j/8)/2)]
            chord.append(rootNote)

            # builds a chord from the root note
            # root + 2nd/3rd + 5th/6th
            for x in range(1, 4):
                synthIndex = ((scale[0].index(rootNote) + (x * 2))%len(scale[0]))
                chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + (x * 2))/len(scale[0])))))

            listNotes[2][0].append(chord[j%4])
            listNotes[2][1].append(.125)

            if i == 0:
                randomInt = random.randint(0, 7)
                if randomInt > 5:
                    listNotes[0][0].append(rootNote - 12)
                    listNotes[0][1].append(rootNote - 12 + 7)
                    listNotes[1][0].append(rootNote - 24)
                    listNotes[3][0].append(scale[1][0])
                elif j%16 == 0:
                    listNotes[0][0].append(-1)
                    listNotes[0][1].append(-1)
                    listNotes[1][0].append(-1)
                    listNotes[3][0].append(scale[1][0])
                else:
                    listNotes[0][0].append(-1)
                    listNotes[0][1].append(-1)
                    listNotes[1][0].append(-1)
                    listNotes[3][0].append(-1)
                listNotes[1][1].append(.125)
                listNotes[0][3].append(0)
            else:
                randomInt = random.randint(0, 5)
                listNotes[0][0].append(rootNote - 12)
                listNotes[0][1].append(chord[2] - 12)
                listNotes[1][0].append(rootNote - 24)
                listNotes[1][1].append(.125)
                listNotes[3][0].append(scale[1][0])
                if randomInt > 2:
                    listNotes[0][3].append(1)
                else:
                    listNotes[0][3].append(0)
            listNotes[0][2].append(-1)
            listNotes[0][4].append(.125)
            
            if j%8 == 4:
                # snare on 3
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if j%2 == 0:
                # cymbals on 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][4])
            else:
                listNotes[3][2].append(-1)
            listNotes[3][3].append(.125)


    return listNotes
