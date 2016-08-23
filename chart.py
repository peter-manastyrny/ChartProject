#imports

import numpy as np
import matplotlib.pyplot as plt

LS_LEGEND = ['Tasks', 'Defects', 'Total']


def read_input_file(input_file):
    '''
    Read csv file and prepare an array of values for plot
    @input_file: name of input csv file
    '''

    #read data from file into array, skipping the first line
    file_data = np.genfromtxt(input_file, delimiter=',', skip_header= 1)

    return file_data


def get_release_labels(file_data):
    '''
    Return release versions from the input file as flat array
    (first column of the input file)
    @file_data: input array with data from .csv file
    '''

    ls_release_labels = file_data[:, 0]

    return ls_release_labels


def build_chart (chart_data, ls_xlabels, ls_legend):
    '''
    Builds chart based on input data and saves it into pdf
    file as well as displays it
    @chart_data: 2-dimensional array of input values
    @ls_xlabels: labels for x-axis
    @ls_legend: legend
    '''

    plt.clf()
    plt.plot(ls_xlabels, chart_data)
    plt.yticks(np.arange(0, np.amax(chart_data) + 10,10))
    plt.legend(LS_LEGEND)
    plt.xlabel('Releases')
    plt.ylabel('Number of tickets')
    plt.show()
    plt.savefig('output_chart.pdf', format='pdf')


def main():
    '''
    Main Function
    '''

    #Read data from csv file
    file_data = read_input_file('input.csv')

    #Get a list of release labels from 1st column of csv file
    ls_release_numbers = get_release_labels(file_data)

    #prepare list of labels for the chart legend
    ls_legend = ['Tasks', 'Defects', 'Total']

    #Get array of values to build the chart
    chart_input_data = file_data[:, 1:]

    #invoke chart build function with prepared parameters
    build_chart(chart_input_data, ls_release_numbers, ls_legend)


if __name__ == '__main__':
    main()