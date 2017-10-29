arrayFileName = './generated/moveArray.io'

arrayFile = open(arrayFileName,'w')

arrayFile.write("//\n")
arrayFile.write("// automatically generated file with array for arduino mega movement\n")
arrayFile.write("//\n")
arrayFile.write("\n")

# x dimension of array : number of ports times number of frames
nbPortsUsed = 4
nbLoopFrames = 24
nbArrayFrames = nbPortsUsed * nbLoopFrames;

# y dimension of array : 12 steps times number of movements
nbSteps = 12
nbMovements = 24
nbArraySteps = nbSteps * nbMovements

arrayFile.write("const byte[%d][%d] PROGMEM = [\n" % (nbArrayFrames, nbArraySteps) )

for stepCpt in xrange(0, nbArraySteps):
    for frameCpt in xrange(0, nbArrayFrames):
        val = stepCpt*nbArrayFrames + frameCpt
        arrayFile.write( "%d " % val )
    arrayFile.write( "\n" )
arrayFile.write( "]\n" )

