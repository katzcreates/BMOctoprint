# BMOctoprint: The DIY Octoprint Server Shaped like BMO from Adventure Time!

So you followed along with my [BMOctoprint](https://katzcreates.com/portfolio/bmoctoprint) project and want to try your hand at making your own? Well, congratulations! You're in the right place and you are in for a treat because BMOctoprint is the sweetest, cutest, loveliest Octoprint server there ever was. 

All of the files you need to recreate my version of BMOctoprint can be found here in this repository. However, if you wish to make alterations to make BMO your own, you are encouraged to do so! You can even create forks of this repository to add your own code or altered 3D printing files. I would love to see what other versions of BMO people can make with what I have started, so please share your results if you end out taking a different approach!

### The full, detailed build instructions will be coming soon!

## Getting Started

This is a rather involved build with a fair bit of expenditure involved with a handful of parts being needed! Below are the components/necessary materials that I used to create BMOctoprint and therefore will work perfectly with the case/code as provided. If you wish to use different components then feel free, but alterations may be necessary to make everything fit!

### Electronics (links are not affiliate links and UK specific)
- A Raspberry Pi 4 (I used a 8GB model which worked great and I recommend it. A smaller model may be fine as well or may run a bit slower.)
   - (If you are going to be running Octoprint then a Pi 4 is a requirement as older models struggle to run it and I have not tested this setup with a Pi Zero.)
- [7 inch Raspberry Pi Touchscreen](https://shop.pimoroni.com/products/raspberry-pi-7-touchscreen-display-with-frame?variant=2677960835082)
   - (This is super easy to use, fits the case perfectly and allows the Pi to mount right to the back of it. It is also quite expensive and there are probably cheaper options that can work with adjustments.)
- [Adafruit I2S Speaker Bonnet](https://shop.pimoroni.com/products/adafruit-i2s-3w-stereo-speaker-bonnet-for-raspberry-pi-mini-kit?variant=34945052618)
- Two (2) [3 inch Speakers](https://shop.pimoroni.com/products/3-speaker-4-3w?variant=380549926)
- Three (3) [12mm Tactile Switches](https://shop.pimoroni.com/products/tactile-switches?variant=372242669)
- Four (4) [6mm Tactile Switches](https://shop.pimoroni.com/products/tactile-switches?variant=372242667)
- One (1) USB-C Panel Mount (capable of power delivery, this is important!!)
- Four (4) [USB-A Panel Mounts (2 Left Angle and 2 Right Angle)](https://www.ebay.co.uk/itm/232860372185)
- Seven (7) 10K resistors

### Additional Components/Materials
- One (1) KG of [Teal PETG filament](https://eu.polymaker.com/product/polylite-petg/?aff=44) (affiliate link)
   - (Total printed weight will depend on your print settings, but 1KG should see you through)
- 50g Black PETG filament
- Small amounts of Yellow, Red, Green and Blue PLA
- 3mm Flexible Armature Wire
- Eight (8) M4x6 screws (cap head preferred for all screws)
- Four (4) M3x4 screws
- Eight (8) M3x8 screws
- Eight (8) M3x16 screws
- Two (2) 8x3mm Neodymium Magnets (optional)

<br/>

### Pi Software Setup

To run all of the current code and software for BMOctoprint, you will need to use the **Buster OS** build of Raspbian. 
> The current build (Bullseye) will not work as OMXPlayer is not compatible with it. 

I recommend downloading and using the [Raspberry Pi Installer tool](https://www.raspberrypi.com/software/) to get this set up. 

#### Required Installs
- OMXPlayer ([Documentation](https://github.com/popcornmix/omxplayer))
- [OMXPlayer-Wrapper](https://pypi.org/project/omxplayer-wrapper/) ([Documentation](https://python-omxplayer-wrapper.readthedocs.io/en/latest/#))
- [Xscreensaver](https://www.jwz.org/xscreensaver/) ([Documentation](https://linux.die.net/man/1/xscreensaver-command))
- [Feh](https://feh.finalrewind.org/) ([Documentation](https://man.finalrewind.org/1/feh/))
- [Octoprint](https://octoprint.org/) (NOT Octopi!) ([Install Instructions](https://community.octoprint.org/t/setting-up-octoprint-on-a-raspberry-pi-running-raspberry-pi-os-debian/2337))

<br/>
<br/>
<br/>


Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
