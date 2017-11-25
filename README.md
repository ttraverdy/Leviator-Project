# Leviator-Project

An Arduino project to levitate small objects and control their movements in mid-air

## Objectives

The Leviator is a 3D printed device that uses ultrasonic transducers to levitate and control in mid air movements of a particle (polystyren microballs) in 3D (limited to 2D for now).


## How it works

Download and print the 3D parts in the STL folder. Many electronic parts are also necessary (list to be provided soon).

Assemble all the parts (Full instructions should soon be available on Instructables). The Fritzing schematic is available in the SCHEMA folder. It will show you the electronic schematic of the Leviator device.

Run the python 'generateMegaCode16x16new.py' program. This will generate a 'moveArray16x16.io' file in the 'generated' folder. Compile using your Arduino IDE and flash on the Arduino MEGA card.

## Leviator in action

Here is the link of the youtube channel of the project : 

<a href="http://www.youtube.com/watch?feature=player_embedded&v=reaBH0q8Cks
" target="_blank"><img src="http://img.youtube.com/vi/reaBH0q8Cks/0.jpg" 
alt="The Leviator, levitation and control of movements using ultrsound" width="240" height="180" border="10" /></a>

(click on the image to see our device work)

The actual 100% successful movement speed is 5mm/s, 10mm/s and 15mm/s for 1 bead. If more beads are put in a node, success rate decrease. 

## Credits and similar projects

Many thanks to Professor Takayuki Hoshi from the University of Tokyo (PixieDust project) and to Mr. Asier Marzo from the Bristol University (BigLev/TinyLev and LeviPath projects)












