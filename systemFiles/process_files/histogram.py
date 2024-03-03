# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:34:02 2023

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_data(url, rows):
    if rows not in (10001, 20001):
        print('unexpected data dimension')
    
    # rows is 10001 for simulation with incremental timsteps of 10, else 20002
    df = pd.read_csv(url)
    
    # use system_total_waiting_time as key to locate performance metric
    waiting_time_row = df["system_total_waiting_time"]
    waiting_time = waiting_time_row.head(rows)
    
    return waiting_time
    
    
def histogram(waiting_time):    
    plt.hist(waiting_time, edgecolor="black")
    
    plt.title('Total Waiting Time between Timesteps')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    
    plt.show()
    pass


def compare(df_list, bins, labels):
    plt.hist(df_list, bins, histtype ='bar', stacked = False, label = labels)
    
    plt.title('Total Waiting Time between Timesteps')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.legend(prop={'size' : 10})
    
    plt.show()
    pass
    


if __name__ == "__main__":
    ###
    # urls
    ###
    # df_standard_normal_norltl = get_data('../result/standard/normal/norltl_normal_result.csv', 20001)
    # df_standard_normal_rltl = get_data('../result/standard/normal/rltl_normal_result.csv', 20001)
    # df_standard_normal_notl = get_data('../result/standard/normal/notl_normal_result.csv', 20001)
    
    # df_standard_dense_norltl = get_data('../result/standard/dense/norltl_dense_result.csv', 20001)
    # df_standard_dense_rltl = get_data('../result/standard/dense/rltl_dense_result.csv', 20001)
    # df_standard_dense_notl = get_data('../result/standard/dense/notl_dense_result.csv', 10001)
    
    # df_standard_biased_norltl = get_data('../result/standard/biased/norltl_biased_result.csv', 20001)
    # df_standard_biased_rltl = get_data('../result/standard/biased/rltl_biased_result.csv', 20001)
    # df_standard_biased_notl = get_data('../result/standard/biased/notl_biased_result.csv', 20001)
    
    # # real life inspired environment, use 100001 as columns
    # df_subang_normal_norltl = get_data('../result/subang/normal/norltl_normal_result.csv', 10001)
    # df_subang_normal_rltl = get_data('../result/subang/normal/rltl_normal_result.csv', 10001)
    # df_subang_normal_notl = get_data('../result/subang/normal/notl_normal_result.csv', 10001)
    
    # df_subang_dense_norltl = get_data('../result/subang/dense/norltl_dense_result.csv', 10001)
    # df_subang_dense_rltl = get_data('../result/subang/dense/rltl_dense_result.csv', 10001)
    # df_subang_dense_notl = get_data('../result/subang/dense/notl_dense_result.csv', 10001)
    
    data_0 = get_data('../result/subang/dense/norltl_dense_result.csv', 10001)
    data_1 = get_data('../result/subang/dense/rltl_dense_result.csv', 10001)
    
    df_list = [data_0, data_1]
    
    labels_0 = ('fixed', 'RL', 'None')
    labels_1 = ('fixed', 'RL')
    
    # histogram(data_0)
    compare(df_list, 30, labels_1)
    
    