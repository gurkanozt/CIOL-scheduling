# CIOL-scheduling
## Overview
In this repository, it is focused on extracting priority rules (PR) for dynamic multi-objective flexible job shop scheduling problems using gene expression programming (GEP). This repository enables you for  testing your PR's. You can find the paper this [link](https://www.tandfonline.com/doi/abs/10.1080/00207543.2018.1543964).
## Initial Setup
This project was developed using Python2.
I highly recommend using Anaconda for Python environment management. It will help you install Shapely, which I've had some problems installing with pip. You do not need extra libraries not contained by Anaconda. 
## Extracting new PR's using GEP
When you run the ```genetikAlgoritma.py``` new rules automatically are generated according to given parameters. This script calls the ```main.py``` containing both ```schedulingProblem.py``` generating the problem and ``` createSolution.py``` that is the simulation scripts.
