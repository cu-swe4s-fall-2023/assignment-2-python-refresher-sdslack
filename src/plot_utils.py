"""Functions for plotting query results

        * plot_hist - plots a histogram of values in a file

"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_hist(file_name, x_label, y_label, title):
    """Plots histogram of values in a file. Writes out as .png.

    Parameters
    ----------
    file_name : str
        Name of the file to read
    x_label : str
        Label for x-axis
    y_label : str
        Label for y-axis
    title : str
        Title for plot

    """
    data = []
    for line in open(file_name):
        data.append(line.rstrip())  # assumes input has one column
 
    fig, ax = plt.subplots()
    ax.hist(data)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    base_file_name = os.path.splitext(file_name)[0]
    plt.savefig(base_file_name + '_hist.png', bbox_inches='tight')