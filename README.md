# PVLC codes 

## Author
Vincent M. Le Corre (Main)

## Description
All these codes are written to be used with the open-source drift-diffusion suit written by Prof. L. Jan Anton Koster from University of Groningen. (See [GitHub repository](https://github.com/kostergroup/SIMsalabim)) They can be used to run the simulation, plot and do analysis of the output from the simulations for both steady-state with SimSS and transient with ZimT.\
Codes can be ran on Windows and Linux. However, the running simulations in parallel is not possible on Windows yet. 



## Repository Folder Structure
    .
    ├── Main                                    # Main directory, place Notebooks here to run them
        ├── Dev_files                           # Directory for development files
        ├── Notebooks                           # Contains clean versions of the Notebooks, Notebooks need to be moved to the main directory to be used
        ├── SIMsalabim_utils                    # Contains main custom packages and functions
        ├── Simulation_program                  # Place SIMsalabim folders here
        ├── SIMsalabim                          # Place SIMsalabim folders here, Get SIMsalabim from https://github.com/kostergroup/SIMsalabim
    └── README.md

## Necessary installs
### SIMsalabim
All the details to install SIMsalabim are detailed in the [GitHub repository](https://github.com/kostergroup/SIMsalabim). To make sure that you are running the latest version of SIMsalabim, check regularly the repository.

### Parallel simulations
On Linux, you have the option to run the simulations in parallel. Sadly, not on windows (yet).
To be able to run simulations in parallel efficiently and with any threading or multiprocessing from python we use the `parallel` from the [GNU prallel](https://www.gnu.org/software/parallel/) project.
To install on linux run:
```
sudo apt update
sudo apt install parallel
```
You can also use [Anaconda](https://anaconda.org/):
```
conda install -c conda-forge parallel
```
To test is the installation worked by using by running the following command in the terminal:
```
parallel --help
```
It is also possible to use the `parmap` package to run the simualtions in parallel. To switch, use the `run_multiprocess_simu` instead of `run_parallel_simu` in the `RunSimulation` function in `/VLC_units/Simulation/RunSim.py` folder. However, this does not work on Ubuntu version 22.04 but seems to work on older versions.
