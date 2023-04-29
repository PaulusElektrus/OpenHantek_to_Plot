# OpenHantek to Plot

### Little command line program to build a plot out of exported .csv file from [OpenHantek](http://openhantek.org/).


## Usage

    `python plot.py data/test.csv`

------------

## Help

positional arguments:
  FILE                  path to a .csv file or folder containing .csv files from OpenHantek

optional arguments:
  -h, --help            show this help message and exit
  -d DISPLAY, --display DISPLAY
                        True displays the plot(s) in a window
  -s SAVE, --save SAVE  specify a path to save the plot(s)

------------

## Result

![Image](test.csv.svg)

------------

## GUI

A GUI would be a highlight for this project. In the folder flet_gui/ I played a bit with [flet](https://flet.dev/). But the results are not good at the moment and not working! I think I will try another GUI Framwork sometime...

------------

### by PaulusElektrus