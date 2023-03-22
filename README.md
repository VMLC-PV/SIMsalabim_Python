# PVLC codes 

## Author
Vincent M. Le Corre (Main)

## Description
All these codes are written to be used with the open-source drift-diffusion suit written by Prof. L. Jan Anton Koster from the University of Groningen. (See [GitHub repository](https://github.com/kostergroup/SIMsalabim)) They can be used to run the simulation, plot and do an analysis of the output from the simulations for both steady-state with SimSS and transient with ZimT.\
Codes can be run on Windows and Linux. However, running simulations in parallel is not possible on Windows yet. 

### Example Data
Some typical experimental data are also provided in the `Example_data` folder. This data is provided to help users get a head start when they try to reproduce their own experimental data.\
These example files represent a good starting point if a user wants to use SIMsalabim to fit their data or just simulate a typical organic or perovskite solar cell device.\
The data was taken from the following papers:\
- [Energy & Environmental Science, 2020, 13, 2134-2141 ](https://doi.org/10.1039/D0EE00714E) (Example data for an organic solar cell)
- [Solar RRL 2022, 6, 2100772 ](https://doi.org/10.1002/solr.202100772)  (Example data for a perovskite solar cell)
If you use these example data, please consider citing the corresponding papers.

## Repository Folder Structure
    .
    ├── Main                                    # Main directory, place Notebooks here to run them
        ├── Notebooks                           # Contains clean versions of the Notebooks, Notebooks need to be moved to the main directory to be used
        ├── SIMsalabim_utils                    # Contains main custom packages and functions
        ├── Simulation_program                  # Place SIMsalabim folders here
        ├── SIMsalabim                          # Place SIMsalabim folders here, Get SIMsalabim from https://github.com/kostergroup/SIMsalabim
    └── README.md

## Python packages
### Conda
To install the necessary packages, you can use [Anaconda](https://anaconda.org/).\

To install the necessary packages, run the following command in the terminal:
```bash
conda create --name simsalabim --file requirements.txt
```
To activate the environment, run the following command in the terminal:
```bash
conda activate simsalabim
```
To deactivate the environment, run the following command in the terminal:
```bash
conda deactivate
```

### Pip
To install the necessary packages, you can use pip.\
To install the necessary packages, run the following command in the terminal:
```bash
pip install -r requirements.txt
```

## Necessary installs
### SIMsalabim
All the details to install SIMsalabim are detailed in the [GitHub repository](https://github.com/kostergroup/SIMsalabim). To make sure that you are running the latest version of SIMsalabim, check regularly the repository.\
You can also run the Download_SIMsalabim.py script in the Main folder to download the latest version of SIMsalabim.\
```
python Download_SIMsalabim.py
```

### Parallel simulations
On Linux, you have the option to run the simulations in parallel. Sadly, not on windows (yet).
To be able to run simulations in parallel efficiently and with any threading or multiprocessing from python we use the `parallel` from the [GNU prallel](https://www.gnu.org/software/parallel/) project.
To install on Linux run:
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
It is also possible to use the `parmap` package to run the simulations in parallel. To switch, use the `run_multiprocess_simu` instead of `run_parallel_simu` in the `RunSimulation` function in `/SIMsalabim_utils/RunSim.py` folder. However, this does not work on Ubuntu version 22.04 but seems to work on older versions.

## Citation
Please, acknowledge the use of this work with the appropriate citation to the following paper and the repository.

M. Koopmans, V.M. Le Corre, and L.J.A. Koster, SIMsalabim: An open-source drift-diffusion simulator for semiconductor devices, J. Open Source Softw. **7**, 3727 (2022).

[The paper can be downloaded here.![DOI](https://joss.theoj.org/papers/10.21105/joss.03727/status.svg)](https://doi.org/10.21105/joss.03727)

```bibtex
@article{Koopmans2022, 
author = {Marten Koopmans and Vincent M. Le Corre and L. Jan Anton Koster}, 
title = {`SIMsalabim`: An open-source drift-diffusion simulator for semiconductor devices}, 
journal = {Journal of Open Source Software},
doi = {10.21105/joss.03727}, 
url = {https://doi.org/10.21105/joss.03727}, 
year = {2022}, volume = {7}, number = {70}, pages = {3727}, 
publisher = {The Open Journal}, 
}
```




