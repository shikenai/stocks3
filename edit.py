def add_ma(df, rolling_list):
    for i in rolling_list:
        df[f'Close_{str(i)}ma'] = df["Close"].rolling(i).mean()
    return df