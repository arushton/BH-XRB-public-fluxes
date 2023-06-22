# Black Hole Observational Data Repository: GRS1915+105 & SWIFTJ1753.5-0127

This repository provides observational datasets of two intriguing black holes in our universe: GRS1915+105 and SWIFTJ1753.5-0127. Long-term observations are crucial for understanding the behavior and the physical properties of these cosmic monsters. 

## Background

**GRS1915+105** is an X-ray binary star system that features a regular star and a black hole. It's known for its variable X-ray and radio emissions and it stands out due to its extraordinary mass, making it an excellent subject for studying stellar evolution and accretion processes.

The work by [Rushton et al. (2010)](https://ui.adsabs.harvard.edu/abs/2010A%26A...524A..29R/abstract) titled "Steady jets from radiatively efficient hard states in GRS 1915+105" presents evidence of a close relationship between the radio and X-ray emission at different epochs for GRS 1915+105. The study found that both the radio and X-ray emissions decay from the start of most plateau states, with the radio emission decaying faster. These findings point towards two possible interpretations: a radiatively efficient accretion disk during the continuous outflow of a compact jet or X-ray emission in the plateau state dominated by emission from the base of the jet.

**SWIFTJ1753.5-0127** is a transient X-ray source discovered in 2005. The paper by [Rushton et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.463..628R/abstract) titled "Disc-jet quenching of the galactic black hole Swift J1753.5-0127" reports on radio and X-ray monitoring observations over a ∼10 yr period. Despite the source being relatively radio-quiet compared to similar X-ray luminosity XRBs in the hard-state, the radio and X-ray relationship scales with a power-law index close to what is expected for radiatively inefficient accretion discs. Notably, the study found significant radio-jet quenching in the XRB soft-state, showing the connection of the jet quenching to the X-ray power-law component. 

## Content Overview

The repository contains the following data files:

### GRS1915+105 Radio Data by the Ryle Telescope (RT)

- [GRS1915+105 RT 15 GHz data](https://github.com/arushton/BH-XRB-public-fluxes/blob/e88cd046924a50894283967446b3e6ecdb9197a1/BHC%20GRS1915%2B105/grs1915_rt-15GHz.dat)

Here is a representative plot of the data:

![GRS1915+105 RT 15 GHz data plot](https://github.com/arushton/BH-XRB-public-fluxes/blob/382956d93eab154c08bc1b8b023d980d4443f6d0/BHC%20GRS1915%2B105/grs1915_rt-15GHz.png)

### SWIFTJ1753.5-0127 Radio and X-ray Data

- [J1753-radio-fluxes.cvs - Radio data](https://github.com/arushton/BH-XRB-public-fluxes/blob/e88cd046924a50894283967446b3e6ecdb9197a1/BHC%20J1753/J1753-radio-fluxes.csv)

Here is a representative plot of the radio data:

![J1753-radio-fluxes plot](https://github.com/arushton/BH-XRB-public-fluxes/blob/382956d93eab154c08bc1b8b023d980d4443f6d0/BHC%20J1753/J1753-radio-fluxes.png)

Additional files related to SWIFTJ1753.5-0127:

- `SWIFTJ1753.5-0127.lc.txt`: This file contains Swift/BAT observational data.
- `XRT_J1753fits_FTEST.txt`: This file contains Swift/XRT with spectrum fitting and extracted
- `radio_data.dat`: The radio data taken from previous published data and monitoring with AMI-LA
