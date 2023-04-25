import pandas as pd
import matplotlib.pyplot as plt
import argparse

def plot(file, **kwargs):

    df = pd.read_csv(file, delimiter=';')
    print (df)
    
    for label in df.columns:
        df[label] = df[label].replace(',','.',regex=True)
        df[label] = df[label].astype(float)

    x_1 = df.iloc[:, 0]

    y_1 = df.iloc[:, 1]
    y_2 = df.iloc[:, 2]

    plt.plot(x_1, y_1)
    plt.plot(x_1, y_2)
    
    if path:
        plt.savefig(path, format='svg', dpi=1200)
        return()
    
    #plt.gca().set_xticks([0,0.01,0.02])
    #plt.gca().set_yticks([0,2.5,5])
    if window == True:
        plt.show()

    #plt.clf()


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
                        prog='OpenHantek to Plot',
                        description='Converts .csv files from OpenHantek to a plot',
                        epilog='by PaulusElektrus')
    parser.add_argument("-s", "--source", required=True, help="path to .csv file from OpenHantek", type=str)
    parser.add_argument("-w", "--window", required=False, default=True, help="show the plot in a window?", type=bool)
    parser.add_argument("-p", "--path", required=False, help="or path for exporting the file to .svg", type=str)
    args = parser.parse_args()

    file = args.source
    window = args.window
    path = args.path

    plot(file, window = window, path = path)