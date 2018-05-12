# What is the Leviator ?

The Leviator is a device made of two arrays of ultrasonic transducers, able to levitate and to control the movements of small objects such as styrofoam beads in 3 dimensions mid-air, using acoustic levitation. 

The levitation is possible thanks to standing wave created by the transducers of the device. Levitating objects are trapped in pressure nodes of those standing waves, surrounded by antinodes, which are going to apply forces on the object, making it levitate. The movements are made by modulating the phase of emission of the transducers. 

This project was awarded a first prize at the XXVth Olypimpiades de Physique, a national physics contest in France.

## How it works

The levitation is possible thanks to standing wave created by the transducers of the device. Levitating objects are trapped in pressure nodes of those standing waves, surrounded by antinodes, which are going to apply forces on the object, making it levitate. The movements are made by modulating the phase of emission of the transducers. 

To see our device work and to have a more precise explication of the movement method, click on the following image to watch a video of our Youtube channel :
<p align="center">
<a href="http://www.youtube.com/watch?feature=player_embedded&v=FV5mTikOukU
" target="_blank"><img src="http://img.youtube.com/vi/FV5mTikOukU/0.jpg" 
alt="The Leviator, levitation and control of movements using ultrsound" width="480" height="350" border="10" /></a>
</p>



## Want to build a Leviator ?

The 3D parts are available on this page in the STL folder. Many electronic parts are also necessary (list to be provided soon).

Assemble all the parts (Full instructions should soon be available on Instructables). The Fritzing schematic is available in the SCHEMA folder. It will show you the electronic schematic of the Leviator device.

Run the python 'generateMegaCode16x16new.py' program. This will generate a 'moveArray16x16.io' file in the 'generated' folder. Compile using your Arduino IDE and flash on the Arduino MEGA card.


## Future improvements

<p align="left">
  <img src="https://raw.githubusercontent.com/ttraverdy/Leviator-Project/master/IMAGES/Chart%20of%20the%20movement%20success%20percentage%20at%20different%20movement%20speeds.png" width="450"/> 
</p>
The actual maximum reliable movement speed is 10.5cm per second for 1 to 5 beads. 100% success rate movement speeds are 0.5cm to 1.5cm/s speeds and speeds from 4.1 to 5.4 cm per second. If more beads are put in a node, the success rate decreases.


We are planning to make a new Leviator, smaller and modular. 3D pieces of the protoype are available in the STL folder. Here is a photo of the actual prototype of the new Leviator. 
<p align="right">
  <img src="https://github.com/ttraverdy/Leviator-Project/blob/master/IMAGES/P1172850.jpg" width="450"/> 
</p>
The new version will be smaller using 10mm diameter transducers and will be modular. Multiple Leviators will be able to be chained to increase the space in which beads will be able to be moved into.

We successfully made a first prototype of the transducer part of the Leviator. We are now working on the miniaturization of power supply of the device. We are actually testing different prototypes such as L293D or TC4427A MOSFET. 
We made different PCB circuits using CNC milling machines or by chemical way using iron perchloride.

## Credits and similar projects

Many thanks to Professor [Takayuki Hoshi](http://hoshistar81.jp/) from the University of Tokyo [Pixie Dust Technologies](http://pixiedusttech.com/) and to Mr. [Asier Marzo](https://www.researchgate.net/profile/Asier_Marzo) from the Bristol University [BigLev/TinyLev and Acoustic Tractor Beam projects](http://www.instructables.com/member/Asier%20Marzo/)




