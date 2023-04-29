#!/usr/bin/env python

import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib, plot

sg.theme("Dark Blue 3")


def GetFile():
    form_rows = [
        [sg.Text("Enter .csv file from OpenHantek")],
        [sg.Text("File: ", size=(15, 1)), sg.InputText(key="-file1-"), sg.FileBrowse()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window("Choose File", form_rows)
    event, values = window.read()
    window.close()
    return event, values


def main():

    button, values = GetFile()
    path = values["-file1-"]

    if any((button != "Submit", path == "")):
        sg.popup_error("Operation cancelled!")
        return

    matplotlib.use("TkAgg")
    fig = plot.open_csv(path, False, None, True)

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
        return figure_canvas_agg

    layout = [
        [sg.Canvas(key="-CANVAS-")],
        [
            sg.Text("Save File: ", size=(15, 1)),
            sg.InputText(key="-folder1-"),
            sg.FolderBrowse(),
        ],
        [sg.Submit(), sg.Button("Close")],
    ]

    window = sg.Window(
        "OpenHantek to Plot",
        layout,
        finalize=True,
        element_justification="center",
        font="Helvetica 18",
    )

    fig_canvas_agg = draw_figure(window["-CANVAS-"].TKCanvas, fig)

    event, values = window.read()

    window.close()

    save_path = values["-folder1-"]

    if any((button != "Submit", path == "", save_path == "")):
        sg.popup_error("Operation cancelled!")
        return

    plot.open_csv(path, False, save_path, False)


if __name__ == "__main__":
    main()
