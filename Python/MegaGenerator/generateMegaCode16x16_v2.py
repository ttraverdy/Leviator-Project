#
# This code defines
#
#
#





# defines constants for generating the code for 2 4x4 transducer arrays

# defines the mapping between the port used on the arduino mega and the transducer
# each transducer is indentified with the triplet (s, x, y) with s being the side, and x, y being the position on the array
# two transducers on opposing arrays and with the same x,y are facing each other.
# side can be 0 or 1 (we consider only 2 opposiing array
sides = 2
sizeArray = 4

# number of ports used
nbPortsUsed = 32


# defines the number of frames/steps for each loop.
# this depends of the number of ports used and the time it takes to iterate, still maintiaining the 40Khz freq
# for the initial code (arduino uno, 4 ports it is 24 frames but for many ports, 12 frames should be used
#
MAX_FRAMES = 12
MAX_PORTS = 4

transducersPorts = [ 'PORTA','PORTA','PORTA','PORTA','PORTA','PORTA','PORTA','PORTA',
                     'PORTC','PORTC','PORTC','PORTC','PORTC','PORTC','PORTC','PORTC',
                     'PORTF','PORTF','PORTF','PORTF','PORTF','PORTF','PORTF','PORTF',
                     'PORTK','PORTK','PORTK','PORTK','PORTK','PORTK','PORTK','PORTK']

transducersBitmask = ['00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000',
                      '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000',
                      '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000',
                      '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000']

arduinoPorts = [ 'PORTA','PORTC','PORTF','PORTK']
arduinoPortValues = {}

# we consider that transducers can be at the following state
# 0 - off
# 1 - is the transducer that has the particle
# 2 - is a transducer around the one that has the particule
STATE_TRANSDUCER_OFF = 0
STATE_TRANSDUCER_NB = 1
STATE_TRANSDUCER_PART = 2

transducerFramesOff= [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
transducerFramesNeighbor= [0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,0x00,0x00,0x00,0x00]
transducerFramesParticle= [0x00,0x00,0x00,0x00,0x00,0x00,0xff,0xff,0xff,0xff,0xff,0xff]

MAX_ANIM_STEPS = 16

STATE_TRANSDUCER_NB2NB = 1
STATE_TRANSDUCER_NB2OFF = 2
STATE_TRANSDUCER_OFF2NB = 3
STATE_TRANSDUCER_OFF2OFF = 4
STATE_TRANSDUCER_NB2PART = 5
STATE_TRANSDUCER_PART2NB = 6

transducerAnimationParticleToNeighbor= [
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff],
    [0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0xee, 0xee, 0xee, 0xee, 0xee, 0xee],
    [0x22, 0x22, 0x22, 0x22, 0x22, 0x22, 0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0xdd],
    [0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc],
    [0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb],
    [0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa],
    [0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x99, 0x99, 0x99, 0x99, 0x99, 0x99],
    [0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88],
    [0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77],
    [0x99, 0x99, 0x99, 0x99, 0x99, 0x99, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66],
    [0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55],
    [0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44],
    [0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33],
    [0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0x22, 0x22, 0x22, 0x22, 0x22, 0x22],
    [0xee, 0xee, 0xee, 0xee, 0xee, 0xee, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
]

transducerAnimationNeighborToParticle= [
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xee, 0xee, 0xee, 0xee, 0xee, 0xee, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11],
    [0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0x22, 0x22, 0x22, 0x22, 0x22, 0x22],
    [0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33],
    [0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44],
    [0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55],
    [0x99, 0x99, 0x99, 0x99, 0x99, 0x99, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66],
    [0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77],
    [0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88],
    [0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x99, 0x99, 0x99, 0x99, 0x99, 0x99],
    [0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa],
    [0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb],
    [0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc],
    [0x22, 0x22, 0x22, 0x22, 0x22, 0x22, 0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0xdd],
    [0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0xee, 0xee, 0xee, 0xee, 0xee, 0xee],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
]

transducerAnimationNeighborToOff= [
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xee, 0xee, 0xee, 0xee, 0xee, 0xee, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x99, 0x99, 0x99, 0x99, 0x99, 0x99, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x22, 0x22, 0x22, 0x22, 0x22, 0x22, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
]

transducerAnimationOffToNeighbor= [
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x22, 0x22, 0x22, 0x22, 0x22, 0x22, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x99, 0x99, 0x99, 0x99, 0x99, 0x99, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0xaa, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0xdd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xee, 0xee, 0xee, 0xee, 0xee, 0xee, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
]

transducerAnimationOffToOff= [
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
]

transducerAnimationNeighborToNeighbor= [
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
]


particulePositionX = 1
particulePositionY = 1

# initial creation of the generated file
# will erase its content if already exists
arrayFileName = './generated/moveArray16x16.io'
arrayFile = open(arrayFileName,'w')

# this method generates the code for moving the particle from position x, y to the position w+deltaX and y+deltaY
# values for deltaX/deltaY are only within -1, 0, 1
# only one of the deltaX and deltaY should be different from 0
# x and y should be within 0..3
# x+deltaX and y+deltaY should be within 0..3

#
def updatePortFrames ( x, y, s, state ):
    # compute the index of the specific transducer
    transducerIndex = (s * (sizeArray*sizeArray)) + (y*sizeArray) + x

    transducerPort = transducersPorts[transducerIndex]
    transducerBitmask = transducersBitmask[transducerIndex]

    # get the bit values for the port
    if transducerPort not in arduinoPortValues.keys():
        portValue = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    else:
        portValue = arduinoPortValues[transducerPort]

    for cpt in xrange(0, 12):
        if state == STATE_TRANSDUCER_OFF:
            portValue[cpt] = portValue[cpt] | ( transducerFramesOff[cpt] & int (transducerBitmask,2))
        elif state == STATE_TRANSDUCER_NB:
            portValue[cpt] = portValue[cpt] | (transducerFramesNeighbor[cpt] & int(transducerBitmask, 2))
        else:
            portValue[cpt] = portValue[cpt] | (transducerFramesParticle[cpt] & int(transducerBitmask, 2))

    arduinoPortValues[transducerPort] = portValue
    return




# check if the selected transducer is the one holding the particle
def isParticleTransducer ( xPartTrans, yPartTrans, xTrans, yTrans):
    if (xPartTrans == xTrans and yPartTrans == yTrans):
        return True;
    else:
        return False;

# check if the selected transducer is a neighbor of the one holding the particle
def isNeighborTransducer ( xPartTrans, yPartTrans, xTrans, yTrans):
    if isParticleTransducer ( xPartTrans, yPartTrans, xTrans, yTrans):
        return False;
    tmpX = abs(xPartTrans - xTrans)
    tmpY = abs(yPartTrans - yTrans)
    if tmpX <= 1 and tmpY <= 1:
        return True;
    return False;

# check if the selected transducer is a neighbor of the one holding the particle
def isOffTransducer ( xPartTrans, yPartTrans, xTrans, yTrans):
    if isParticleTransducer ( xPartTrans, yPartTrans, xTrans, yTrans):
        return False;
    if isNeighborTransducer ( xPartTrans, yPartTrans, xTrans, yTrans):
        return False;
    return True;

# check if the selected transducer is a neighbor of the one holding the particle
def writeFileHeader ():
    # write the file header
    arrayFile.write("//\n")
    arrayFile.write("// automatically generated file with array for arduino mega movement\n")
    arrayFile.write("//\n")
    arrayFile.write("\n")
    arrayFile.write("#include <avr/sleep.h>\n")
    arrayFile.write("#include <avr/power.h>\n")
    arrayFile.write("\n")
    return;

def writePortArrayStart ():
    arrayFile.write("static byte frame = 0;\n")
    arrayFile.write("\n")
    arrayFile.write("#define N_PORTS 4\n")
    arrayFile.write("#define N_DIVS 1\n")
    arrayFile.write("#define N_FRAMES 12\n")
    arrayFile.write("\n")
    arrayFile.write("#define OUTPUT_WAVE_A(pointer, d)  PORTA = pointer[d]\n")
    arrayFile.write("#define OUTPUT_WAVE_C(pointer, d)  PORTC = pointer[d]\n")
    arrayFile.write("#define OUTPUT_WAVE_F(pointer, d)  PORTF = pointer[d]\n")
    arrayFile.write("#define OUTPUT_WAVE_K(pointer, d)  PORTK = pointer[d]\n")
    arrayFile.write("\n")
    arrayFile.write("const PROGMEM byte portValuesTransducerStates [%d][%d] = {\n"% (MAX_PORTS*sizeArray*sizeArray, MAX_FRAMES))
    return;

def writePortArrayEnd ():
    arrayFile.write("}\n")
    return;

def writeAnimArrayStart ():
    arrayFile.write("\n")
    arrayFile.write("const PROGMEM byte portValuesTransducerAnimations [%d][%d] = {\n"% (MAX_PORTS*sizeArray*sizeArray*MAX_ANIM_STEPS, MAX_FRAMES))
    return;

def writeAnimArrayEnd ():
    arrayFile.write("}\n")
    return;

def writePortValues ():
    arrayFile.write("  ")
    for nPort in xrange(0, MAX_PORTS):
        portName = arduinoPorts[nPort]
        portFrames = arduinoPortValues[portName]

        arrayFile.write("{")
        for nFrame in xrange(0, MAX_FRAMES):
            val = portFrames[nFrame]
            arrayFile.write( "%d " % val )
            if nFrame != 11:
                arrayFile.write(", ")
        arrayFile.write("}")
        if nPort != 3:
            arrayFile.write(", ")
    return;

def writeSetupCode():
    arrayFile.write("\n")
    arrayFile.write("\n")
    arrayFile.write("\n")
    arrayFile.write("// arduino mega setup code\n")
    arrayFile.write("void setup()\n")
    arrayFile.write("{\n")
    arrayFile.write("   DDRC = 0b00001111; //A0 to A3 are the signal outputs\n")
    arrayFile.write("   PORTC = 0b00000000; \n")
    arrayFile.write("   pinMode(10, OUTPUT); //pin 10 (B2) will generate a 40kHz signal to sync \n")
    arrayFile.write("   pinMode(11, INPUT_PULLUP); //pin 11 (B3) is the sync in\n")
    arrayFile.write("   //please connect pin 10 to pin 11\n")
    arrayFile.write("\n")
    arrayFile.write("   // set all needed pins to outpur mode\n")
    arrayFile.write("   for (int i = 2; i < 8; ++i){ //pin 2 to 7 (D2 to D7) are inputs for the buttons\n")
    arrayFile.write("    pinMode(i, INPUT_PULLUP);\n")
    arrayFile.write("   }\n")
    arrayFile.write("\n")
    arrayFile.write("  // generate a sync signal of 40khz in pin 10\n")
    arrayFile.write("  noInterrupts();           // disable all interrupts\n")
    arrayFile.write("  TCCR1A = bit (WGM10) | bit (WGM11) | bit (COM1B1); // fast PWM, clear OC1B on compare\n")
    arrayFile.write("  TCCR1B = bit (WGM12) | bit (WGM13) | bit (CS10);   // fast PWM, no prescaler\n")
    arrayFile.write("  OCR1A =  (F_CPU / 40000L) - 1;\n")
    arrayFile.write("  OCR1B = (F_CPU / 40000L) / 2;\n")
    arrayFile.write("  interrupts();             // enable all interrupts\n")
    arrayFile.write("\n")
    arrayFile.write("  // disable everything that we do not need \n")
    arrayFile.write("  ADCSRA = 0;  // ADC\n")
    arrayFile.write("  power_adc_disable ();\n")
    arrayFile.write("  power_spi_disable();\n")
    arrayFile.write("  power_twi_disable();\n")
    arrayFile.write("  power_timer0_disable();\n")
    arrayFile.write("  //power_usart0_disable();\n")
    arrayFile.write("  Serial.begin(115200);\n")
    arrayFile.write("\n")
    arrayFile.write("\n")
    arrayFile.write("\n")
    arrayFile.write("\n")
    arrayFile.write("\n")
    arrayFile.write("   byte* emittingPointerA = &portValuesTransducerStates[frame+0][0];\n")
    arrayFile.write("   byte* emittingPointerC = &portValuesTransducerStates[frame+1][0];\n")
    arrayFile.write("   byte* emittingPointerF = &portValuesTransducerStates[frame+2][0];\n")
    arrayFile.write("   byte* emittingPointerK = &portValuesTransducerStates[frame+3][0];\n")
    arrayFile.write("\n")
    arrayFile.write("   byte* animationPointerA = &portValuesTransducerAnimations[frame+0][0];\n")
    arrayFile.write("   byte* animationPointerC = &portValuesTransducerAnimations[frame+1][0];\n")
    arrayFile.write("   byte* animationPointerF = &portValuesTransducerAnimations[frame+2][0];\n")
    arrayFile.write("   byte* animationPointerK = &portValuesTransducerAnimations[frame+3][0];\n")
    arrayFile.write("\n")
    return;

def writeLoopCode():
    arrayFile.write("  // arduino mega loop code (static particle)\n")
    arrayFile.write("  LOOP_STEADY:\n")
    arrayFile.write("    while(PINB & 0b00001000); //wait for pin 11 (B3) to go low \n")
    arrayFile.write("\n")
    arrayFile.write("    // write to all ports and all frames\n")
    for nFrame in xrange(0, MAX_FRAMES):
        arrayFile.write("    OUTPUT_WAVE_A(emittingPointerA, %i);\n" % nFrame)
        arrayFile.write("    OUTPUT_WAVE_C(emittingPointerC, %i);\n" % nFrame)
        arrayFile.write("    OUTPUT_WAVE_F(emittingPointerF, %i);\n" % nFrame)
        arrayFile.write("    OUTPUT_WAVE_K(emittingPointerK, %i);\n" % nFrame)
    arrayFile.write("\n")
    arrayFile.write("  goto LOOP_STEADY;\n")
    arrayFile.write("\n")
    arrayFile.write("\n")
    arrayFile.write("  // arduino mega loop code (moving particle)\n")
    arrayFile.write("  LOOP_MOVE:\n")
    arrayFile.write("\n")
    for animStep in xrange(0, MAX_ANIM_STEPS):
        for nFrame in xrange(0, MAX_FRAMES):
            arrayFile.write("    OUTPUT_WAVE_A(animationPointerA, %i);\n" % (animStep*MAX_FRAMES+nFrame))
            arrayFile.write("    OUTPUT_WAVE_C(animationPointerC, %i);\n" % (animStep*MAX_FRAMES+nFrame))
            arrayFile.write("    OUTPUT_WAVE_F(animationPointerF, %i);\n" % (animStep*MAX_FRAMES+nFrame))
            arrayFile.write("    OUTPUT_WAVE_K(animationPointerK, %i);\n" % (animStep*MAX_FRAMES+nFrame))
    arrayFile.write("\n")
    arrayFile.write("  goto LOOP_MOVE;\n")
    arrayFile.write("\n")
    arrayFile.write("}\n")
    arrayFile.write("void loop(){}\n")
    return;

# returns true if destination within the 4*4 array, false otherwise
# array starts at zero and array size is sizeArray
def destinationValid (x, y):
    if x<0 or y<0:
        return False;
    if x>=sizeArray or y>=sizeArray:
        return False;
    return True;

def writeAnimation ():
    for stepAnim in xrange(1, MAX_ANIM_STEPS):
        arrayFile.write("  ")
        for nPort in xrange(0, MAX_PORTS):
            arrayFile.write("{")
            for nFrame in xrange(0, MAX_FRAMES):
                arrayFile.write( "0 " )
                if nFrame < (MAX_FRAMES-1):
                    arrayFile.write(", ")
            arrayFile.write("}")
            if nPort < (MAX_PORTS-1):
                arrayFile.write(", ")
        if stepAnim < (MAX_ANIM_STEPS - 1):
            arrayFile.write(", ")
        arrayFile.write("\n")
    return;

def writeNullAnimationBad ():
    for stepAnim in xrange(1, MAX_ANIM_STEPS):
        arrayFile.write("  ")
        for nPort in xrange(0, MAX_PORTS):
            arrayFile.write("{")
            for nFrame in xrange(0, MAX_FRAMES):
                arrayFile.write( "1 " )
                if nFrame < (MAX_FRAMES-1):
                    arrayFile.write(", ")
            arrayFile.write("}")
            if nPort < (MAX_PORTS-1):
                arrayFile.write(", ")
        if stepAnim < (MAX_ANIM_STEPS-1):
            arrayFile.write(", ")
        arrayFile.write("\n")
    return;

def isNeighborToNeighborTransducer (transducerPositionX, transducerPositionY, particulePositionX,
                                                    particulePositionY, destinationParticleX, destinationParticleY):
    if isNeighborTransducer(transducerPositionX, transducerPositionY, particulePositionX,particulePositionY) and \
            isNeighborTransducer(transducerPositionX, transducerPositionY, destinationParticleX, destinationParticleY):
        return True;
    else:
        return False;

def isNeighborToOffTransducer(transducerPositionX, transducerPositionY, particulePositionX,
                                   particulePositionY, destinationParticleX, destinationParticleY):
    if isNeighborTransducer(transducerPositionX, transducerPositionY, particulePositionX, particulePositionY) and \
            isOffTransducer(transducerPositionX, transducerPositionY, destinationParticleX, destinationParticleY):
        return True;
    else:
        return False;

def isOffToNeighborTransducer(transducerPositionX, transducerPositionY, particulePositionX,
                              particulePositionY, destinationParticleX, destinationParticleY):
    if isOffTransducer(transducerPositionX, transducerPositionY, particulePositionX, particulePositionY) and \
            isNeighborTransducer(transducerPositionX, transducerPositionY, destinationParticleX, destinationParticleY):
        return True;
    else:
        return False;

def isOffToOffTransducer(transducerPositionX, transducerPositionY, particulePositionX,
                              particulePositionY, destinationParticleX, destinationParticleY):
    if isOffTransducer(transducerPositionX, transducerPositionY, particulePositionX, particulePositionY) and \
            isOffTransducer(transducerPositionX, transducerPositionY, destinationParticleX, destinationParticleY):
        return True;
    else:
        return False;

def isParticleToNeighborTransducer(transducerPositionX, transducerPositionY, particulePositionX,
                         particulePositionY, destinationParticleX, destinationParticleY):
    if isParticleTransducer(transducerPositionX, transducerPositionY, particulePositionX, particulePositionY) and \
            isNeighborTransducer(transducerPositionX, transducerPositionY, destinationParticleX, destinationParticleY):
        return True;
    else:
        return False;

def isNeighborToParticleTransducer(transducerPositionX, transducerPositionY, particulePositionX,
                         particulePositionY, destinationParticleX, destinationParticleY):
    if isNeighborTransducer(transducerPositionX, transducerPositionY, particulePositionX, particulePositionY) and \
            isParticleTransducer(transducerPositionX, transducerPositionY, destinationParticleX, destinationParticleY):
        return True;
    else:
        return False;

def updateAnimationsFrames(x, y, s, animationState, animStep):
    # compute the index of the specific transducer
    transducerIndex = (s * (sizeArray*sizeArray)) + (y*sizeArray) + x

    transducerPort = transducersPorts[transducerIndex]
    transducerBitmask = transducersBitmask[transducerIndex]

    # get the bit values for the port
    if transducerPort not in arduinoPortValues.keys():
        portValue = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    else:
        portValue = arduinoPortValues[transducerPort]
        for cpt in xrange(0, MAX_FRAMES):
            if animationState == STATE_TRANSDUCER_NB2NB:
                portValue[cpt] = portValue[cpt] | ( transducerAnimationNeighborToNeighbor[animStep][cpt] & int (transducerBitmask,2))
            elif animationState == STATE_TRANSDUCER_NB2OFF:
                portValue[cpt] = portValue[cpt] | (transducerAnimationNeighborToOff[animStep][cpt] & int(transducerBitmask, 2))
            elif animationState == STATE_TRANSDUCER_OFF2NB:
                portValue[cpt] = portValue[cpt] | (transducerAnimationOffToNeighbor[animStep][cpt] & int(transducerBitmask, 2))
            elif animationState == STATE_TRANSDUCER_OFF2OFF:
                portValue[cpt] = portValue[cpt] | (transducerAnimationOffToOff[animStep][cpt] & int(transducerBitmask, 2))
            elif animationState == STATE_TRANSDUCER_NB2PART:
                portValue[cpt] = portValue[cpt] | (transducerAnimationNeighborToParticle[animStep][cpt] & int(transducerBitmask, 2))
            elif animationState == STATE_TRANSDUCER_PART2NB:
                portValue[cpt] = portValue[cpt] | (transducerAnimationParticleToNeighbor[animStep][cpt] & int(transducerBitmask, 2))
            # else:
                # problem

    arduinoPortValues[transducerPort] = portValue
    return

#
#

# write the start of the file (header and init code
# then writes the two arrays, one for the static positions of a particle
# and one for all the animations of a particle going from one position to another one
writeFileHeader ()
writePortArrayStart()
for particulePositionX in xrange(0, sizeArray):
    for particulePositionY in xrange(0, sizeArray):
        arrayFile.write("  // port operations for particule at x=%d y=%d\n" % (particulePositionX, particulePositionY))
        arduinoPortValues.clear()
        for transducerPositionX in xrange(0, sizeArray):
            for transducerPositionY in xrange(0, sizeArray):
                for transducerSide in xrange(0, sides):
                    if isNeighborTransducer(transducerPositionX, transducerPositionY, particulePositionX, particulePositionY):
                        updatePortFrames(transducerPositionX, transducerPositionY, transducerSide, STATE_TRANSDUCER_NB)
                    elif isParticleTransducer(transducerPositionX, transducerPositionY, particulePositionX, particulePositionY):
                        updatePortFrames(transducerPositionX, transducerPositionY, transducerSide, STATE_TRANSDUCER_PART)
                    else:
                        updatePortFrames(transducerPositionX, transducerPositionY, transducerSide, STATE_TRANSDUCER_OFF)
        writePortValues()
        if particulePositionX != (sizeArray-1) or particulePositionY != (sizeArray-1):
            arrayFile.write(",\n")
writePortArrayEnd()

writeAnimArrayStart()
for particulePositionX in xrange(0, sizeArray):
    for particulePositionY in xrange(0, sizeArray):
        # x+1
        arduinoPortValues.clear()
        destinationParticleX = particulePositionX + 1
        destinationParticleY = particulePositionY
        arrayFile.write("  // anim from (%d, %d) to (%d, %d)\n" % (particulePositionX, particulePositionY,destinationParticleX,destinationParticleY))
        if destinationValid (destinationParticleX,destinationParticleY):
            for animStep in xrange(0, MAX_ANIM_STEPS):
                arduinoPortValues.clear()
                for transducerPositionX in xrange(0, sizeArray):
                    for transducerPositionY in xrange(0, sizeArray):
                        for transducerSide in xrange(0, sides):
                            if isNeighborToNeighborTransducer(transducerPositionX, transducerPositionY, particulePositionX,
                                                    particulePositionY, destinationParticleX, destinationParticleY):
                                updateAnimationsFrames(transducerPositionX, transducerPositionY, transducerSide, STATE_TRANSDUCER_NB2NB, animStep)
                            elif isNeighborToOffTransducer(transducerPositionX, transducerPositionY, particulePositionX,
                                                    particulePositionY, destinationParticleX, destinationParticleY):
                                updateAnimationsFrames(transducerPositionX, transducerPositionY, transducerSide, STATE_TRANSDUCER_NB2OFF, animStep)
                            elif isNeighborToOffTransducer(transducerPositionX, transducerPositionY,
                                                               particulePositionX,
                                                               particulePositionY, destinationParticleX,
                                                               destinationParticleY):
                                updateAnimationsFrames(transducerPositionX, transducerPositionY, transducerSide,STATE_TRANSDUCER_OFF2NB, animStep)
                            elif isOffToOffTransducer(transducerPositionX, transducerPositionY,
                                                               particulePositionX,
                                                               particulePositionY, destinationParticleX,
                                                               destinationParticleY):
                                updateAnimationsFrames(transducerPositionX, transducerPositionY, transducerSide,STATE_TRANSDUCER_OFF2OFF, animStep)
                            elif isNeighborToParticleTransducer(transducerPositionX, transducerPositionY,
                                                               particulePositionX,
                                                               particulePositionY, destinationParticleX,
                                                               destinationParticleY):
                                updateAnimationsFrames(transducerPositionX, transducerPositionY, transducerSide,STATE_TRANSDUCER_NB2PART, animStep)
                            elif isParticleToNeighborTransducer(transducerPositionX, transducerPositionY,
                                                               particulePositionX,
                                                               particulePositionY, destinationParticleX,
                                                               destinationParticleY):
                                updateAnimationsFrames(transducerPositionX, transducerPositionY, transducerSide,STATE_TRANSDUCER_PART2NB, animStep)
                            # else:
                                # ERROR ?? invalid state
                writePortValues()
                if animStep < (MAX_ANIM_STEPS - 1):
                    arrayFile.write(", ")
                arrayFile.write("\n")

        else:
            writeNullAnimationBad()
        arrayFile.write("\n")

        # y+1
        arduinoPortValues.clear()
        destinationParticleX = particulePositionX
        destinationParticleY = particulePositionY + 1
        arrayFile.write("  // anim from (%d, %d) to (%d, %d)\n" % (particulePositionX, particulePositionY,destinationParticleX,destinationParticleY))
        if destinationValid (destinationParticleX,destinationParticleY):
            writeNullAnimationBad()
        else:
            writeNullAnimationBad()
        arrayFile.write("\n")

        # x - 1
        arduinoPortValues.clear()
        destinationParticleX = particulePositionX - 1
        destinationParticleY = particulePositionY
        arrayFile.write("  // anim from (%d, %d) to (%d, %d)\n" % (particulePositionX, particulePositionY,destinationParticleX,destinationParticleY))
        if destinationValid(destinationParticleX, destinationParticleY):
            writeNullAnimationBad()
        else:
            writeNullAnimationBad()
        arrayFile.write("\n")

        # y + 1
        arduinoPortValues.clear()
        destinationParticleX = particulePositionX - 1
        destinationParticleY = particulePositionY
        arrayFile.write("  // anim from (%d, %d) to (%d, %d)\n" % (particulePositionX, particulePositionY,destinationParticleX,destinationParticleY))
        if destinationValid(destinationParticleX, destinationParticleY):
            writeNullAnimationBad()
        else:
            writeNullAnimationBad()
        arrayFile.write("\n")

writeAnimArrayEnd()

writeSetupCode()
writeLoopCode()
#
#
#






















