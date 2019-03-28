import pandas as pd

class ResourceManager:

    csv_cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

    def read_from_csv(self, path='', converters=None):
        return pd.read_csv(path, converters=converters).rename(columns={
            #TODO refactor this and use csv_cols with some lowercase function

                'Date': 'date',
                'Open': 'open',
                'High': 'high',
                'Low': 'low',
                'Close': 'close',
                'Volume': 'volume'
            }).drop('Adj Close', axis=1)
