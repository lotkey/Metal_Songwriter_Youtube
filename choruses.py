### Synth Chris 666
### https://synthchrismusic.wixsite.com/music
### choruses.py
### This file contains all the loose structures for choruses

import random
from functions import getChordProgression

### Basic four chord progression
# Slower than verses, uses quarter notes
# More rests
# Some syncopation
def c0(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]
    chords = getChordProgression(scale)

    for i in range(0, 2):
        for j in range(0, 8 * 4):

            # I will either add two sixteenth notes or one quarter note
            # isDouble means I will add two sixteenth notes
            # otherwise, I will add a quarter note
            isDouble = False        
            randomInt = random.randint(0, 5)
            chordNote = chords[(int)((j/8))]

            ### guitar and bass
            if(randomInt >= 3):
                # one quarter note
                ### guitar and bass
                listNotes[0][0].append(chordNote - 12)
                listNotes[0][1].append(chordNote + 7 - 12)
                sixIndex = (scale[0].index(chordNote) + 2) % len(scale[0])
                listNotes[0][2].append(scale[0][sixIndex] + (12 * ((int)(scale[0].index(chordNote) + 2 > len(scale[0]) - 1))))
                listNotes[0][3].append(1)
                listNotes[0][4].append(.25)

                # bass
                listNotes[1][0].append(chordNote - 24)
                listNotes[1][1].append(.25)
                
                # kick drum
                listNotes[3][0].append(scale[1][0])
                listNotes[3][3].append(.25)
                
            elif(randomInt >= 1):
                # two sixteenth notes
                isDouble = True
                randInt = random.randint(0,3)

                ### guitar and bass
                if(randInt == 0):
                    # palm mute and rest
                    listNotes[0][0].append(chordNote - 12)
                    listNotes[0][1].append(chordNote + 7 - 12)
                    listNotes[0][2].append(-1)
                    listNotes[0][3].append(0)

                    listNotes[0][0].append(-1)
                    listNotes[0][1].append(-1)
                    listNotes[0][2].append(-1)
                    listNotes[0][3].append(0)

                    # bass
                    listNotes[1][0].append(chordNote - 24)
                    listNotes[1][0].append(-1)

                    # kick drum
                    listNotes[3][0].append(scale[1][0])
                    listNotes[3][0].append(-1)
                elif(randInt == 1):
                    # two palm mutes
                    for i in range(0, 2):
                        listNotes[3][0].append(scale[1][0])
                        listNotes[0][0].append(chordNote - 12)
                        listNotes[0][1].append(chordNote + 7 - 12)
                        listNotes[0][2].append(-1)
                        listNotes[0][3].append(0)
                        listNotes[1][0].append(chordNote - 24)
                else:
                    # rest and palm mute
                    listNotes[3][0].append(-1)
                    listNotes[3][0].append(scale[1][0])

                    listNotes[0][0].append(-1)
                    listNotes[0][1].append(-1)
                    listNotes[0][2].append(-1)
                    listNotes[0][3].append(0)

                    listNotes[0][0].append(chordNote - 12)
                    listNotes[0][1].append(chordNote + 7 - 12)
                    listNotes[0][2].append(-1)
                    listNotes[0][3].append(0)

                    listNotes[1][0].append(-1)
                    listNotes[1][0].append(chordNote - 24)
                for i in range(0, 2):   
                    listNotes[3][3].append(.125)
                    listNotes[0][4].append(.125)
                    listNotes[1][1].append(.125)
            else:
                # quarter note rest
                listNotes[3][0].append(-1)
                listNotes[3][3].append(.25)

                listNotes[0][0].append(-1)
                listNotes[0][1].append(-1)
                listNotes[0][2].append(-1)
                listNotes[0][3].append(0)
                listNotes[0][4].append(.25)

                listNotes[1][0].append(-1)
                listNotes[1][1].append(.25)

            ### drums
            listNotes[3][2].append(scale[1][2])
            if(j%4 == 2):
                # snare on every 3
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if(isDouble):
                listNotes[3][2].append(-1)
                listNotes[3][1].append(-1)

            ### synth
            # arpeggiates the third of the root note
            synthIndex = ((scale[0].index(chordNote) + 2)%len(scale[0]))
            listNotes[2][0].append(scale[0][synthIndex] + (12 * ((int)((chordNote + 2) > scale[0][len(scale) - 1]))))
            listNotes[2][0].append(scale[0][synthIndex])
            for i in range(0, 2):
                listNotes[2][1].append(.125)

    return listNotes

def c1(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]
    chords = getChordProgression(scale)

    for i in range(0, 2):
        for j in range(0, 16 * 4):
            chordNote = chords[(int)((j/16))]
            listNotes[0][0].append(chordNote - 12)
            listNotes[0][1].append(-1)
            listNotes[0][2].append(-1)
            listNotes[0][3].append(1)
            listNotes[0][4].append(.125)

            listNotes[1][0].append(chordNote - 24)
            listNotes[1][1].append(.125)

            listNotes[3][0].append(scale[1][0])
            listNotes[3][3].append(.125)         
            if j%8 == 4:
                # snare on every 3
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if j%2 == 0:
                # cymbal on every 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)

        for i in range(0, 4):
            listNotes[2][0].append(chords[i])
            
            randomInterval = random.randint(4,5)
            synthIndex = ((scale[0].index(chords[i]) + randomInterval)%len(scale[0]))
            listNotes[2][0].append(scale[0][synthIndex] + (12 * ((int)((chordNote + randomInterval) > scale[0][len(scale) - 1]))) - 12)

            randomInterval = random.randint(1,2)
            synthIndex = ((scale[0].index(chords[i]) + randomInterval)%len(scale[0]))
            listNotes[2][0].append(scale[0][synthIndex] + (12 * ((int)((chordNote + randomInterval) > scale[0][len(scale) - 1]))))
            listNotes[2][1].append(.75)
            listNotes[2][1].append(.75)
            listNotes[2][1].append(.5)

    return listNotes

def c2(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]
    
    chords = getChordProgression(scale)
    chord = []
    
    for i in range(0, 2):
        j = 0
        while j < 8 * 4:
            chord.clear()
            rootNote = chords[(int)((j/4)/2)]
            chord.append(rootNote)

            # builds a chord from the root note
            # root + 2nd/3rd + 5th/6th
            #for x in range(1, 3):
            #    synthIndex = ((scale[0].index(rootNote) + (x * 2))%len(scale[0]))
            #    chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + (x * 2))/len(scale[0])))))
                
            if int(j%4) == 3:
                listNotes[1][0].append(rootNote - 12)
                listNotes[1][1].append(.25)

                listNotes[3][0].append(scale[1][0])
                listNotes[3][0].append(-1)
            else:
                randInt = random.randint(0, 3)
                if randInt == 0 and j%4 == 0:
                    listNotes[1][0].append(rootNote - 24)
                    listNotes[1][1].append(.5)
                    
                    listNotes[3][0].append(scale[1][0])
                    for i in range(0, 3):
                        listNotes[3][0].append(-1)
                    
                    j += 1
                elif randInt == 1 and j%4 == 2:
                    listNotes[1][0].append(-1)
                    listNotes[1][1].append(.25)

                    listNotes[3][0].append(-1)
                    listNotes[3][0].append(-1)
                elif randInt == 2:
                    listNotes[1][0].append(rootNote - 24)
                    listNotes[1][1].append(.25)

                    listNotes[3][0].append(scale[1][0])
                    listNotes[3][0].append(-1)
                else:
                    for i in range(0, 2):
                        listNotes[1][0].append(rootNote - 24)
                        listNotes[1][1].append(.125)

                        listNotes[3][0].append(scale[1][0])
            j += 1

        chord = []
        for k in range(0, 16 * 4):

            chord.clear()
            rootNote = chords[(int)(k/16)]
            chord.append(rootNote)

            # builds a chord from the root note
            # root + 2nd/3rd + 4th/5th/6th
            randInt = random.randint(1, 2)
            synthIndex = ((scale[0].index(rootNote) + randInt)%len(scale[0]))
            chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + randInt)/len(scale[0])))))
            randInt = random.randint(3, 5)
            synthIndex = ((scale[0].index(rootNote) + randInt)%len(scale[0]))
            chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + randInt)/len(scale[0])))))

            if not k%4 == 3:
                listNotes[0][0].append(chord[k%4] - 12)
                listNotes[2][0].append(chord[k%4])
            else:
                listNotes[0][0].append(chord[1] - 12)
                listNotes[2][0].append(chord[1])
            listNotes[2][1].append(.125)
            listNotes[0][1].append(-1)
            listNotes[0][2].append(-1)
            listNotes[0][3].append(0)
            listNotes[0][4].append(.125)
            
            listNotes[3][3].append(.125)         
            if k%8 == 4:
                # snare on every 3
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if k%2 == 0:
                # cymbal on every 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)

    return listNotes

def c3(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]

    chords = getChordProgression(scale)
    chord = []

    for i in range(0, 2):
        for j in range(0, 16 * 4):

            chord.clear()
            rootNote = chords[(int)(j/16)]
            chord.append(rootNote)

            # builds a chord from the root note
            # root + 2nd/3rd + 4th/5th/6th
            randInt = random.randint(1, 2)
            synthIndex = ((scale[0].index(rootNote) + randInt)%len(scale[0]))
            chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + randInt)/len(scale[0])))))
            randInt = random.randint(3, 5)
            synthIndex = ((scale[0].index(rootNote) + randInt)%len(scale[0]))
            chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + randInt)/len(scale[0])))))

            if j%16 < 8:
                listNotes[0][0].append(rootNote - 12)
                listNotes[0][1].append(chord[1] - 12)
                listNotes[1][0].append(rootNote - 24)
            else:
                listNotes[0][0].append(chord[1] - 12)
                listNotes[0][1].append(chord[2] - 12)
                listNotes[1][0].append(chord[1] - 24)
            listNotes[0][2].append(-1)
            listNotes[0][3].append(random.randint(0, 1))
            listNotes[0][4].append(.125)
            listNotes[1][1].append(.125)

            listNotes[3][0].append(scale[1][0])
            if int(j/16)%2 == 0:
                listNotes[3][0].append(-1)
            else:
                listNotes[3][0].append(scale[1][0])

            if j%2 == 0:
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)
            listNotes[3][2].append(-1)

            if j%2 == 0 and int(j/16)%2 == 0:
                listNotes[3][1].append(scale[1][1])
            elif j%8 == 4 and int(j/16)%2 == 1:
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            listNotes[3][1].append(-1)
            
            for i in range(0, 2):
                listNotes[3][3].append(.0625)

            if j%16 < 8:
                listNotes[2][0].append(chord[1])
            else:
                listNotes[2][0].append(rootNote)
            listNotes[2][1].append(.125)

    return listNotes    

def c4(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]
    lengths = [.25, .125, .5]

    chords = getChordProgression(scale)
    chord = []

    for i in range(0, 2):
        midiBeatCounter = 0
        while midiBeatCounter < 8:

            chord.clear()
            rootNote = chords[(int)(midiBeatCounter/2)]
            chord.append(rootNote)

            # builds a chord from the root note
            # root + 2nd/3rd + 4th/5th/6th
            randInt = random.randint(1, 2)
            synthIndex = ((scale[0].index(rootNote) + randInt)%len(scale[0]))
            chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + randInt)/len(scale[0])))))
            randInt = random.randint(3, 5)
            synthIndex = ((scale[0].index(rootNote) + randInt)%len(scale[0]))
            chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + randInt)/len(scale[0])))))
            chord.append(scale[0][(scale[0].index(rootNote) + 6)%len(scale[0])] + (12 * ((int)((scale[0].index(rootNote) + 6)/len(scale[0])))))

            randomLength = random.choice(lengths)
            if randomLength + midiBeatCounter > 8:
                randomLength = 8 - midiBeatCounter

            if randomLength == .5:
                listNotes[0][0].append(scale[0][0] - 24)
                listNotes[1][0].append(scale[0][0] - 24)
            else:
                randInt = random.randint(0, 3)
                if randInt == 0:
                    listNotes[0][0].append(scale[0][0] - 24)
                    listNotes[1][0].append(scale[0][0] - 24)
                else:
                    randomNote = random.choice(chord) - 12
                    listNotes[0][0].append(randomNote)
                    listNotes[1][0].append(randomNote - 12)
            listNotes[0][1].append(-1)
            listNotes[0][2].append(-1)
            listNotes[0][3].append(1)
            listNotes[0][4].append(randomLength)
            listNotes[1][1].append(randomLength)

            midiBeatCounter += randomLength

            for j in range(0, int(randomLength * 8)):
                if j == 0:
                    listNotes[3][0].append(scale[1][0])
                else:
                    listNotes[3][0].append(-1)
                listNotes[3][3].append(.125)
        for j in range(0, 16 * 4):
            chord.clear()
            rootNote = chords[(int)(j/16)]
            chord.append(rootNote)

            # builds a chord from the root note
            # root + 2nd/3rd + 4th/5th/6th
            randInt = random.randint(1, 2)
            synthIndex = ((scale[0].index(rootNote) + randInt)%len(scale[0]))
            chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + randInt)/len(scale[0])))))
            randInt = random.randint(3, 5)
            synthIndex = ((scale[0].index(rootNote) + randInt)%len(scale[0]))
            chord.append(scale[0][synthIndex] + (12 * ((int)((scale[0].index(rootNote) + randInt)/len(scale[0])))))
            chord.append(scale[0][(scale[0].index(rootNote) + 6)%len(scale[0])] + (12 * ((int)((scale[0].index(rootNote) + 6)/len(scale[0])))))
            if ((j%8 == 2 or j%8 == 6) and i == 0) or (j%8 == 4 and i == 1):
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if j%2 == 0:
                # cymbal on every 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)
            listNotes[2][0].append(chord[j%4])
            listNotes[2][1].append(.125)

    return listNotes
