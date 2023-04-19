import os
import datetime as dt
import pandas as pd
import edit

t = dt.datetime.now()

df_brands = pd.read_csv(os.path.join(os.getcwd(), 'data', 'nikkei_listed_20230415.csv'))
df_trades = pd.read_csv(os.path.join(os.getcwd(), 'data', 'nikkei_trades_20230415test.csv'))

df_date = df_trades['Attributes']
rolling_list = [i + 2 for i in range(100)]

new_columns = df_trades.iloc[0].tolist()
df_trades.columns = new_columns
for i in range(1, ((len(new_columns) - 1) // 5) + 1):
    extracted_df = pd.concat([df_date, df_trades[new_columns[i]]], axis=1)
    extracted_df = extracted_df.drop([0, 1])
    extracted_df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
    extracted_df = extracted_df.astype({'Close': float, 'High': float, 'Open': float, 'Low': float, 'Volume': float})
    extracted_df['brand'] = new_columns[i]
    _df = edit.add_ma(extracted_df, rolling_list)
    print(_df)



# 事後処理
elapsed_time = dt.datetime.now() - t
minutes, seconds = divmod(elapsed_time.total_seconds(), 60)
print(f"{minutes:.0f}分{seconds:.0f}秒")
