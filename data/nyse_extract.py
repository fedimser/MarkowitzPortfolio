# This script extracts NYSE (New York Stock Exchange) prices
# Author: fedimser

from data_extraction import extract_data

with open('nyse_symbols.txt') as f:
    nyse_symbols = [line.split()[0] for line in f.readlines()][1:]
 
    
extract_data(nyse_symbols[::50], dataset_name='nyse_each_50')
#extract_data(nyse_symbols[::10], dataset_name='nyse_each_10')
#extract_data(nyse_symbols, dataset_name='nyse')
