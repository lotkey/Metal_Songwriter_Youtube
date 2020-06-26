### Synth Chris 666
### https://synthchrismusic.wixsite.com/music
### verses.py
### This file contains all of the loose structures for breakdowns

import random
from functions import getChordProgression

### 'Galloping' style breakdown
# No rests
# Palm-muted tritones (first fret on 6th string, open 5th string in drop tuning)
# Switches between eighth notes or two sixteenth notes for galloping feel
def b0(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]

    for i in range(0, 2):
        for j in range(0, 16 * 4):
            
            ### guitar and bass
            if(random.randint(0, 2) == 0):
                # two sixteenth notes
                for k in range(0, 2):
                    listNotes[0][0].append(scale[0][0] + 1 - 12)
                    listNotes[0][1].append(scale[0][0] + 7 - 12)
                    listNotes[0][2].append(-1)
                    listNotes[0][3].append(0)
                    listNotes[0][4].append(.0625)

                    # bass
                    listNotes[1][0].append(scale[0][0] + 1 - 24)
                    listNotes[1][1].append(.0625)

                    # kick drum
                    listNotes[3][0].append(scale[1][0])
            else:
                if i == 0:
                    # eighth note palm-muted for first rep
                    listNotes[0][0].append(scale[0][0] + 1 - 12)
                    listNotes[0][1].append(scale[0][0] + 7 - 12)
                    listNotes[0][2].append(-1)
                    listNotes[0][3].append(0)
                
                    listNotes[1][0].append(scale[0][0] + 1 - 24)
                else:
                    # eighth note open for second rep
                    listNotes[0][0].append(scale[0][0] - 12)
                    listNotes[0][1].append(-1)
                    listNotes[0][2].append(-1)
                    listNotes[0][3].append(1)

                    # bass
                    listNotes[1][0].append(scale[0][0] - 24)
                    
                listNotes[0][4].append(.125)
                listNotes[1][1].append(.125)

                # kick drum
                listNotes[3][0].append(scale[1][0])
                listNotes[3][0].append(-1)

            ### drums
            if j%8 == 4:
                # snare on every 3
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            listNotes[3][1].append(-1)
            if j%2 == 0:
                # cymbals on 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)
            listNotes[3][2].append(-1)

            for l in range(0, 2):
                listNotes[3][3].append(.0625)

            ### synth
            # just some random stuff
            if(j%2 == 0):
                if(j%8 == 0):
                    # reinforce the key center
                    randomNote = scale[0][0] + 12
                else:
                    randomNote = (random.choice(range(1, 3)) * 12) + random.choice(scale[0])
            else:
                randomNote = listNotes[2][0][i-1] - 12
            listNotes[2][0].append(randomNote)
            listNotes[2][1].append(.125)
                

    return listNotes 

### Dissonant deathcore/metalcore breakdown
# Lots of breakdowns use dissonant noises
# This can be achieved with minor 2nd intervals, or notes a half-step apart (C and C#, E and F, etc.)
# Also includes power chords on first fret and '0th' fret, both palm-muted and open
def b1(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]

    for i in range(0, 2):
        for j in range(0, 16 * 4):

            randomInt = random.randint(0, 5)

            # guitar and bass
            if randomInt >= 3:
                # power chord on '0th' fret
                # probably 2/5
                listNotes[0][0].append(scale[0][0] - 12)
                if random.randint(0, 2) == 0:
                    # palm-muted
                    listNotes[0][1].append(scale[0][0] - 12 + 7)
                    listNotes[0][3].append(0)
                else:
                    # open
                    listNotes[0][1].append(-1)
                    listNotes[0][3].append(1)
                listNotes[0][2].append(-1)
                
                # bass
                listNotes[1][0].append(scale[0][0] - 24)
                if i == 1:
                    # kick drum
                    listNotes[3][0].append(scale[1][0])
            elif randomInt >= 1:
                # power chord on first fret
                # probability 2/5
                listNotes[0][0].append(scale[0][0] + 1 - 12)
                if random.randint(0, 2) == 0:
                    # palm-muted
                    listNotes[0][1].append(scale[0][0] - 12 + 8)
                    listNotes[0][3].append(0)
                else:
                    # open
                    listNotes[0][1].append(-1)
                    listNotes[0][3].append(1)
                listNotes[0][2].append(-1)
                
                # bass
                listNotes[1][0].append(scale[0][0] - 24 + 1)
                if i == 1:
                    # kick drum
                    listNotes[3][0].append(scale[1][0])
            else:
                # dissonant minor 2nd interval
                # probability 1/5
                listNotes[0][0].append(scale[0][0] + 12)
                listNotes[0][1].append(scale[0][0] + 13)
                listNotes[0][2].append(-1)
                listNotes[0][3].append(1)

                # bass
                listNotes[1][0].append(-1)
                if i == 1:
                    # kick drum
                    listNotes[3][0].append(-1)
            listNotes[0][4].append(.125)
            listNotes[1][1].append(.125)
            if i == 0:
                # kick drum
                # every eighth note for the first rep
                listNotes[3][0].append(scale[1][0])
            if j%4 == 2 and i == 0:
                # snare on 2 and 4 for the first rep
                listNotes[3][1].append(scale[1][1])
            elif j%8 == 4 and i == 1:
                # snare on every 3 for the second rep
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if j%2 == 0:
                # cymbals on 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)
            listNotes[3][3].append(.125)

            ### synth
            # just some random stuff
            if(j%2 == 0):
                if(j%8 == 0):
                    # reinforce the key center
                    randomNote = scale[0][0] + 12
                else:
                    randomNote = (random.choice(range(1, 3)) * 12) + random.choice(scale[0])
            else:
                randomNote = listNotes[2][0][i-1] - 12
            listNotes[2][0].append(randomNote)
            listNotes[2][1].append(.125)

    return listNotes
    
def b2(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]

    for i in range(0, 2):
        midiBeatCounter = 0
        length = 8
        while midiBeatCounter < length:
            if (random.randint(0, 7) > 2 or midiBeatCounter == 0) and not(midiBeatCounter + .375 > length):
                for l in range(0, 5):
                    listNotes[0][0].append(scale[0][0] - 12)
                    listNotes[0][1].append(scale[0][0] - 12 + 7)
                    listNotes[0][2].append(-1)
                    listNotes[0][3].append(0)

                    listNotes[1][0].append(scale[0][0] - 24)
                for l in range(0, 4):
                    listNotes[0][4].append(.0625)
                    listNotes[1][1].append(.0625)
                listNotes[0][4].append(.125)
                listNotes[1][1].append(.125)
                midiBeatCounter += .375

                for l in range(0, 5):
                    listNotes[3][0].append(scale[1][0])
                listNotes[3][0].append(-1)
                
            elif midiBeatCounter + .25 > length:
                finalLength = length - midiBeatCounter
                listNotes[0][0].append(-1)
                listNotes[0][1].append(-1)
                listNotes[0][2].append(-1)
                listNotes[0][3].append(0)
                listNotes[1][0].append(-1)
                
                listNotes[0][4].append(finalLength)
                listNotes[1][1].append(finalLength)
                midiBeatCounter += finalLength

                for l in range(0, (int)(finalLength / .0625)):
                    listNotes[3][0].append(-1)
            else:
                listNotes[0][0].append(-1)
                listNotes[0][1].append(-1)
                listNotes[0][2].append(-1)
                listNotes[0][3].append(0)
                listNotes[1][0].append(-1)
                
                listNotes[0][4].append(.25)
                listNotes[1][1].append(.25)
                midiBeatCounter += .25

                for l in range(0, 4):
                    listNotes[3][0].append(-1)

        for j in range(0, 16 * 8):
            if j%2 == 0 and ((int)(j/2))%8 == 4:
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if j%2 == 0 and ((int)(j/2))%2 == 0:
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)
            listNotes[3][3].append(.0625)

        for j in range(0, 16 * 4):
            if(j%2 == 0):
                if(j%8 == 0):
                    # reinforce the key center
                    randomNote = scale[0][0] + 12
                else:
                    randomNote = (random.choice(range(1, 3)) * 12) + random.choice(scale[0])
            else:
                randomNote = listNotes[2][0][i-1] - 12
            listNotes[2][0].append(randomNote)
            listNotes[2][1].append(.125)

    return listNotes
    
def b3(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]

    for i in range(0, 2):
        for j in range(0, 16 * 4):
            if i == 0:
                if j%16 == 0:
                    randomNote = scale[0][0]
                else:
                    randomNote = scale[0][0] + random.randint(0, 6)
                listNotes[0][0].append(randomNote - 12)
                listNotes[0][1].append(randomNote - 12 + 7)
                listNotes[0][2].append(-1)
                listNotes[0][3].append(random.randint(0, 1))
                listNotes[0][4].append(.125)
            else:
                for k in range(0, len(listNotes[0])):
                    listNotes[0][k].append(listNotes[0][k][j])

            listNotes[1][0].append(listNotes[0][0][j] - 12)
            listNotes[1][1].append(.125)

            listNotes[3][0].append(scale[1][0])

            if j%2 == 0 and i == 0:
                # snare on 2 and 4 for the first rep
                listNotes[3][1].append(scale[1][1])
            elif j%8 == 4 and i == 1:
                # snare on every 3 for the second rep
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if j%2 == 0:
                # cymbals on 1, 2, 3, and 4
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)
            if int(j / 8) > 3:
                listNotes[3][0].append(scale[1][0])
            else:
                listNotes[3][0].append(-1)
            listNotes[3][1].append(-1)
            listNotes[3][2].append(-1)
            listNotes[3][3].append(.0625)
            listNotes[3][3].append(.0625)

            listNotes[2][0].append(-1)
            listNotes[2][1].append(.125)
            
    return listNotes
    
def b4(scale):
    listNotes = [[[], [], [], [], []], [[], []], [[], []], [[], [], [], []]]
    lengths = [.5, .25]
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

            randomLength = random.choice(lengths)
            if randomLength + midiBeatCounter > 8:
                randomLength = 8 - midiBeatCounter

            rest = random.randint(0,1)
            if rest == 0:
                listNotes[0][0].append(scale[0][0] - 12 + 1)
                listNotes[0][1].append(scale[0][0] - 12 + 7)
                listNotes[1][0].append(scale[0][0] - 24 + 1)
            else:
                listNotes[0][0].append(-1)
                listNotes[0][1].append(-1)
                listNotes[1][0].append(-1)
            listNotes[0][2].append(-1)
            listNotes[0][3].append(0)
            listNotes[0][4].append(randomLength)
            listNotes[1][1].append(randomLength)
            midiBeatCounter += randomLength
            
            for i in range(0, int(randomLength * 4)):
                if i == 0 and rest == 0:
                    listNotes[3][0].append(scale[1][0])
                else:
                    listNotes[3][0].append(-1)
                listNotes[3][3].append(.25)

            if random.randint(0, 1) == 0:
                listNotes[2][0].append(random.choice(scale[0]))
            else:
                listNotes[2][0].append(random.choice(chord))
            listNotes[2][1].append(randomLength)

    for i in range(0, 2):
        for j in range(0, 8 * 4):
            if (j%8 == 4 and i == 0) or (j%16 == 8 and i == 1):
                listNotes[3][1].append(scale[1][1])
            else:
                listNotes[3][1].append(-1)
            if (j%2 == 0 and i == 0) or (j%4 == 0 and i == 1):
                listNotes[3][2].append(scale[1][2])
            else:
                listNotes[3][2].append(-1)
                

    return listNotes
