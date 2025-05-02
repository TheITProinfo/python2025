
import pandas as pd
import csv
from pyecharts import options as opts
from pyecharts.charts import Bar

data_df=pd.read_csv('stock_data.csv')
df=data_df.dropna()
df1=df[['symbol','amount']]
df2=df1.iloc[:20]
print(df2['symbol'].values)
print(df2['amount'].values)

c=(
    Bar()
    .add_xaxis(list(df2['symbol']))
    .add_yaxis("Stock amount", list(df2['amount']))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Stock amount Chart"),
        datazoom_opts=opts.DataZoomOpts(),
        
        )
        .render("data.html")
)

print("generate virtualize data is done!!")