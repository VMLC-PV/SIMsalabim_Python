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
        ├── bayesim                             # Directory with the modified Bayesim package from https://github.com/PV-Lab/bayesim
        ├── imeet                               # Directory with the imeet python package
        ├── Notebooks                           # Contains clean versions of the Notebooks, Notebooks need to be moved to the main directory to be used
        ├── VLC_units                           # Contains main custom packages and functions
        ├── Simulation_program                  # Place SIMsalabim folders here
            ├── SIMsalabim                      # Contains simulation program folders from https://github.com/kostergroup/SIMsalabim
        ├── Dev_files                           # Code currently in development
    └── README.md

## Necessary installs
### SIMsalabim
All the details to install SIMsalabim are detailed in the [GitHub repository](https://github.com/kostergroup/SIMsalabim). To make sure that you are running the latest version of SIMsalabim, check regularly the repository.

### Bayesim
The Bayesim package in the repository is a modified version of the original package from [Bayesim GitHub repository](https://github.com/PV-Lab/bayesim). All the details to install bayesim or to get some tutorials are detailed on the [Bayesim website](https://pv-lab.github.io/bayesim/_build/html/index.html#).
Note that none of the method related to the baysian inference and subdivision were modified from the original package.\
The modifications are:
- updated the export function for .h5 files to make it compatible with newer python versions.
- added a new function to calculate the physical hyperparameters.
- modified the code to interface properly with the output from [SIMsalabim](https://github.com/kostergroup/SIMsalabim).

If bayesim is used, one should cite the following [paper](https://doi.org/10.1016/j.cpc.2019.01.022):\
R. Kurchin, G. Romano, and T. Buonassisi, “Bayesim: A tool for adaptive grid model fitting with Bayesian inference", Comput. Phys. Commun., vol. 239, pp. 161–165, 2019. 

### Parallel simulations
On Linux, you have the option to run the simulations in parrallel. Sadly, not on windows (yet).
To be able to run simulations in parrallel efficiently and with any threading or multiprocessing from python we use the `parallel` from the [GNU prallel](https://www.gnu.org/software/parallel/) project.
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
