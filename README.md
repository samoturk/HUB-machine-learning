# HUB-machine-learning
HUB (Heidelberg Unseminars in Bioinformatics) about machine learning  

This repository contains example notebooks/workflows for [HUB](http://www.hub-hub.de/wordpress/?tribe_events=hub25-machine-learning) machine learning event.  

### KNIME workflows
In order to use KNIME workflows you just need to install [KNIME analytics platform](https://www.knime.org/downloads/overview) (no additional KNIME packages are needed).  
To load the data in select "File Reader" -> "Configure..." -> "Browse..." and open a `csv` file with data. Now you also have to click on "class" column and change type to "String".

### Jupyter notebooks
In order to use jupyter notebooks you need Python 3.x with numpy, pandas, matplotlib, scikit-learn and seaborn. All except seaborn are included in the default [Anaconda Python distribution](https://www.continuum.io/downloads) installation.

### Presentation
Folder `pdf` contains a sort presentation about validation of binary classifiers.

### Data sets
Folder `data` contains two data sets **Pima Indians Diabetes Database** and **Breast cancer Wisconsin**. First one is used in the example workflows/notebooks and the second is for group activity. More information about individual data sets can be found in `info` files. `csv` files are processed so that they can be imidiately used in ML software. Target variable is always *class* column, first column is sample index and the rest are features.
