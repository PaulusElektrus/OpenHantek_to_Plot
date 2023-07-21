#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import argparse, os, glob
from matplotlib.ticker import FormatStrFormatter


def plot(file, show, save_path, pyGui=False):

    df = pd.read_csv(file, delimiter=";", decimal=",", thousands=".")
    df = df.astype(float)

    if "f / Hz" in df.columns and (df["t / s"] == 0).all():
        fig, ax2 = plt.subplots(1)
    elif "t / s" and "f / Hz" in df.columns:
        fig, (ax1, ax2) = plt.subplots(2)
    else:
        fig, ax1 = plt.subplots(1)

    if (df["t / s"] == 0).all():
        print("No time data found")
        pass
    elif "t / s" in df.columns:
        x_t = df["t / s"]
        x_t = x_t * 1000
        if "CH1 / V" in df.columns:
            y_V1 = df["CH1 / V"]
            ax1.plot(x_t, y_V1, label="CH1")
        if "CH2 / V" in df.columns:
            y_V2 = df["CH2 / V"]
            ax1.plot(x_t, y_V2, label="CH2")
        if "MATH / V" in df.columns:
            y_VMATH = df["MATH / V"]
            ax1.plot(x_t, y_VMATH, label="MATH")
        ax1.set_xlabel("Zeit [ms]")
        ax1.set_ylabel("Spannung [V]")
        decimal_places = 1
        ax1.yaxis.set_major_formatter(FormatStrFormatter(f'%.{decimal_places}f'))
        ax1.legend()
    else:
        print("No time data found")

    if "f / Hz" in df.columns:
        x_f = df["f / Hz"]
        x_f = x_f / 1000
        if "SP1 / dB" in df.columns:
            y_f1 = df["SP1 / dB"]
            ax2.plot(x_f, y_f1, label="SP1")
            ind = x_lim_finder(df, "SP1 / dB")
        if "SP2 / dB" in df.columns:
            y_f2 = df["SP2 / dB"]
            ax2.plot(x_f, y_f2, label="SP2")
            ind = x_lim_finder(df, "SP2 / dB")
        if "SPM / dB" in df.columns:
            y_fmixed = df["SPM / dB"]
            ax2.plot(x_f, y_fmixed, label="SPM")
            ind = x_lim_finder(df, "SPM / dB")
        if ind != None:
            x_lim = x_f[ind]
            ax2.set_xlim(0, x_lim)
        ax2.set_xlabel("Frequenz [kHz]")
        ax2.set_ylabel("Amplitude [dB]")
        ax2.legend()
    else:
        print("No frequency data found")

    plt.tight_layout()

    if pyGui:
        return plt.gcf()

    if save_path:
        head, tail = os.path.split(file)
        plt.savefig(save_path + "/" + tail + ".svg", format="svg", dpi=1200)
    else:
        plt.savefig(file + ".svg", format="svg", dpi=1200)

    if show:
        plt.show()


def x_lim_finder(df, column):
    is_60 = 0
    for ind, column in enumerate(df[column]):
        if column == -60 or column == float("nan"):
            is_60 += 1
            # 211 because then 10 kHz is minimal reached
            if is_60 == 211:
                return ind
        else:
            is_60 = 0
    return None


def open_csv(path, show, save_path, pyGui=False):
    if os.path.isfile(path):
        print("File found")
        if pyGui:
            return plot(path, show, save_path, True)
        else:
            plot(path, show, save_path)

    elif os.path.isdir(path):
        print("Directory found")
        for filepath in glob.glob(os.path.join(path, "*.csv")):
            if pyGui:
                return plot(path, show, save_path, True)
            else:
                plot(filepath, show, save_path)

    elif os.path.exists(path):
        print("Path does not exist")
        return ()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="OpenHantek to Plot",
        description="Converts .csv files from OpenHantek to a .svg plot.",
        epilog="by PaulusElektrus",
    )
    parser.add_argument(
        "open",
        metavar="FILE",
        help="path to a .csv file or folder containing .csv files from OpenHantek",
        type=str,
    )
    parser.add_argument(
        "-d",
        "--display",
        required=False,
        default=False,
        help="True displays the plot(s) in a window",
        type=bool,
    ),
    parser.add_argument(
        "-s",
        "--save",
        required=False,
        default=None,
        help="specify a path to save the plot(s)",
        type=str,
    )

    args = parser.parse_args()

    file = args.open
    show = args.display
    save_path = args.save

    open_csv(file, show, save_path)
