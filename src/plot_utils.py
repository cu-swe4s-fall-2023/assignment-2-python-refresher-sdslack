"""Functions for plotting query results

        * plot_hist - plots a histogram of values in a file

"""

import os
import matplotlib
matplotlib.use('Agg')  # noqa
import matplotlib.pyplot as plt


def plot_hist(file_name, output_path, x_label, y_label, title):
    """Plots histogram of values in a file. Writes out as .png.

    Parameters
    ----------
    file_name : str
        Name of the file to read
    output_path : str
        Path to write output file to
    x_label : str
        Label for x-axis
    y_label : str
        Label for y-axis
    title : str
        Title for plot

    """
    data = []
    for line in open(file_name):
        data.append(int(line.rstrip()))  # assumes input has one column

    data.sort()
    fig, ax = plt.subplots()
    ax.hist(data)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    file_name_no_path = os.path.basename(file_name)
    base_file_name = os.path.splitext(file_name_no_path)[0]
    plt.savefig(output_path + base_file_name + '_hist.png', bbox_inches='tight')
