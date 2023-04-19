import os
import datetime as dt
import polars as pl

t = dt.datetime.now()

df_brands = pl.read_csv(os.path.join(os.getcwd(), 'data', 'nikkei_listed_20230415.csv'))
df_trades = pl.read_csv(os.path.join(os.getcwd(), 'data', 'nikkei_trades_20230415test.csv'))

trades_columns = df_trades.columns
n = 2
_columns = []
for i in range(1, ((len(df_trades.columns) - 1) // 5) + 1):
    temp_cols = ["Attributes"]
    for j in range(5):
        temp_cols.append(trades_columns[n * j + i])
    _columns.append(temp_cols)
for i in range(len(_columns)):

    new_df = df_trades.select(_columns[i])
    print(new_df)
    new_df = new_df[2:]
    new_columns = new_df.columns
    new_df = new_df.select(new_columns).rename(
        {new_columns[0]: 'Date', new_columns[1]: "Close", new_columns[2]: 'High', new_columns[3]: 'Low',
         new_columns[4]: 'Open', new_columns[5]: 'Volume'})

# 事後処理
elapsed_time = dt.datetime.now() - t
minutes, seconds = divmod(elapsed_time.total_seconds(), 60)
print(f"{minutes:.0f}分{seconds:.0f}秒")
