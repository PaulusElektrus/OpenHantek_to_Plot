import pandas as pd
import matplotlib.pyplot as plt
import argparse


def plot(file, **kwargs):

    df = pd.read_csv(file, delimiter=";", decimal=",", thousands=".")
    df = df.astype(float)

    if "f / Hz" in df.columns and (df["t / s"] == 0).all():
        fig, ax2 = plt.subplots(1)
    elif "t / s" and "f / Hz" in df.columns:
        fig, (ax1, ax2) = plt.subplots(2)
    else:
        fig, ax1 = plt.subplots(1)

    if (df["t / s"] == 0).all():
        pass
    elif "t / s" in df.columns:
        x_t = df["t / s"]
        x_t = x_t * 1000
        if "CH1 / V" in df.columns:
            y_V1 = df["CH1 / V"]
            ax1.plot(x_t, y_V1)
        if "CH2 / V" in df.columns:
            y_V2 = df["CH2 / V"]
            ax1.plot(x_t, y_V2)
        if "MATH / V" in df.columns:
            y_VMATH = df["MATH / V"]
            ax1.plot(x_t, y_VMATH)
        ax1.set_xlabel("Zeit [ms]")
        ax1.set_ylabel("Spannung [V]")
    else:
        print("No time data found")

    if "f / Hz" in df.columns:
        x_f = df["f / Hz"]
        x_f = x_f / 1000
        if "SP1 / dB" in df.columns:
            y_f1 = df["SP1 / dB"]
            ax2.plot(x_f, y_f1)
        if "SP2 / dB" in df.columns:
            y_f2 = df["SP2 / dB"]
            ax2.plot(x_f, y_f2)
        if "SPM / dB" in df.columns:
            y_fmixed = df["SPM / dB"]
            ax2.plot(x_f, y_fmixed)
        ax2.set_xlim(0, 20)
        ax2.set_xlabel("Frequenz [kHz]")
        ax2.set_ylabel("Amplitude [dB]")
    else:
        print("No frequency data found")

    plt.tight_layout()

    if path:
        plt.savefig(path, format="svg", dpi=1200)
        plt.clf()
        return ()

    if window == True:
        plt.show()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="OpenHantek to Plot",
        description="Converts .csv files from OpenHantek to a plot",
        epilog="by PaulusElektrus",
    )
    parser.add_argument(
        "-o",
        "--open",
        required=True,
        help="path to .csv file from OpenHantek",
        type=str,
    )
    parser.add_argument(
        "-w",
        "--window",
        required=False,
        default=True,
        help="show the plot in a window?",
        type=bool,
    )
    parser.add_argument(
        "-s",
        "--save",
        required=False,
        help="or path for exporting the file to .svg",
        type=str,
    )
    args = parser.parse_args()

    file = args.source
    window = args.window
    path = args.path

    plot(file, window=window, path=path)
