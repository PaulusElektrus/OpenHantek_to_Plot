# OpenHantek to Plot

&nbsp;

### Little command line tool with GUI to build a plot out of exported .csv file(s) from [OpenHantek](http://openhantek.org/).

&nbsp;

------------

&nbsp;

## Graphical User Interface

&nbsp;

Made with [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI/tree/master)

Start the GUI with `python gui.py`

&nbsp;

![GUI](GUI.png)

&nbsp;

- Entering a file path will display the resulting plot and there is a option to save the plot.

- Entering a folder path will convert all files found and you will be asked for a path to save the plots.

&nbsp;

------------

&nbsp;

## Command Line Interface

&nbsp;

### - Usage:

  -  `python plot.py data/test.csv` --> will store the .svg plot in the same folder

  -  `python plot.py data/test.csv -d True` --> will display the plot in a window

  -  `python plot.py data/test.csv -s plots` --> will store the .svg plot in the plots/ folder

  -  `python plot.py data -s plots` --> will convert all .csv files in data/ in .svg images and store them in plots/

  - ...

&nbsp;

### - Help:

- positional arguments:
  
  FILE                  path to a .csv file or folder containing .csv files from OpenHantek

- optional arguments:
 
  -h, --help  -->          show this help message and exit

  -d DISPLAY, --display DISPLAY     -->    True displays the plot(s) in a window

  -s SAVE, --save SAVE --> specify a path to save the plot(s)

&nbsp;

------------

&nbsp;

## How to export .csv files?

&nbsp;

![Export](OpenHantekExport.png)

&nbsp;

------------

&nbsp;

## Resulting Plot for 'test.csv':

&nbsp;

![Image](test.csv.svg)

&nbsp;

------------

### by PaulusElektrus