import pandas as pd
import fix_yahoo_finance as yf

def extract_data(symbols, dataset_name='data'):
    end_train = '2015-01-01'
    start_train = '2007-01-01'
    end_test = '2016-01-01'
    start_test = '2015-01-01'
    
    def get_px_train(symbol):
        return yf.download(symbol, start=start_train, end=end_train)['Adj Close']
    
    def get_px_test(symbol):
        return yf.download(symbol, start=start_test, end=end_test)['Adj Close']
    
    loaded_train = dict()
    loaded_test = dict()
    ok_symbols = set()
    
    ctr = 0
    total = len(symbols)
    
    for symbol in symbols:
        try:
            loaded_train[symbol] = get_px_train(symbol)
            loaded_test[symbol]  = get_px_test(symbol)
            ok_symbols.add(symbol)
        except:
            pass
        
        ctr += 1
        if symbol in ok_symbols:
            print("Loaded %s. %d of %d done." % (symbol, ctr, total))
        else:
            print("Failed %s. %d of %d done." % (symbol, ctr, total))        
    print("All done.")
    
    data_train = pd.DataFrame({sym:loaded_train[sym] for sym in ok_symbols})
    data_test = pd.DataFrame({sym:loaded_test[sym] for sym in ok_symbols})
    
    data_train.dropna(axis = 1, how='any', inplace=True)
    data_test = data_test[list(data_train)]
    
    data_train.to_csv("./%s_train.csv" % dataset_name)
    data_test.to_csv("./%s_test.csv" % dataset_name)

if __name__ == "__main__":
    symbols = ['BAC','GE','MU','F','AMD','BRCD',\
           'AAPL','T','WFC','RAD','WFT','CMCSA','CHK','BABA','TEVA',\
           'MSFT','VALE','VZ','INTC','CSCO','SIRI','JPM','FHN']
    extract_data(symbols)