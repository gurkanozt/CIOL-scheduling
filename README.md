# CIOL-scheduling
## Overview
In this repository, it is focused on extracting priority rules (PR) for dynamic multi-objective flexible job shop scheduling problems using gene expression programming (GEP). This repository enables you for  testing your PR's. You can find the paper this [link](https://www.tandfonline.com/doi/abs/10.1080/00207543.2018.1543964).
## Initial Setup
This project was developed using Python2.
I highly recommend using Anaconda for Python environment management. It will help you install Shapely, which I've had some problems installing with pip. You do not need extra libraries not contained by Anaconda. 
## Extracting new PR's using GEP
When you run the ```genetikAlgoritma.py``` new rules automatically are generated according to given parameters. This script calls the ```main.py``` containing both ```schedulingProblem.py``` generating the problem and ``` createSolution.py``` that is the simulation scripts. After finish the scripts ```sumofresult.txt``` file is created. This file contains all information about GEP steps and at the bottom of this file you can find the extracted PR's. 
## Testing PR's
If you have your PR's you can test them by running ```dispatchingRules.py``` script. Before running this script you should add your rules on this file. You must seclect variables ,you use in your rules, in our GEP terminal sets(you can find it in the paper page 8).  
When you run the script, ```main.py``` is called same as Extracting new PR's using GEP. After finish the script ```result.txt```and  ```sumofresult.txt``` files are created. The first file records the all result for the all PR's for the each sub problem while the second file saves the same result for the  ().
