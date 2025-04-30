import requests
from  fake_useragent import UserAgent
import pandas as pd
import csv
# coding: utf-8
# web crawler example 001
# url https://xueqiu.com/hq/detail?market=CN&first_name=0&second_name=0&type=sh_sz
## actual url=https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page=1&size=30&order=desc&order_by=percent&market=CN&type=sh_sz

ua=UserAgent().random # get random user agent
headers={'User-Agent':ua} # set user agent of header

cookies={'cookie':'xq_a_token=9773bacc11404cb5ac8b0847c564eda3730e6b61; xqat=9773bacc11404cb5ac8b0847c564eda3730e6b61; xq_r_token=caf75c71460c20a680e6e3c455cadcca5c1be14a; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc0NzM1NzE4MywiY3RtIjoxNzQ1OTQ3NTU1Mzk1LCJjaWQiOiJkOWQwbjRBWnVwIn0.f-XL06MJC2XGJBo6bktPDRIhHMFoMI8ZKgPqedfSqigQzhjAWE-SRONv92xeTtxjVLtAff9y3YDJ7tX8o5aTC7AvXxbAQewvxTelUOWFucF5Fe4u3g3r4J4g8rvdtYuwaKTdo-20CyfwU1W4_4ZD_P52hu1ruLW7_oEY48l86zw4gTYyiRcDx7_gl8gyiSM3HlASMjwNIAQpwjozc0TMKf4HXDklLgBoODDnf9yPuWRDONHx8yHqm5hnge9LV6BQMoZb5gz4Euj8A3vrEdcu3GMlNohZiAmFd-OuIMVmQijQwC48Gj7XMz7859a-_c_mX9r9qaOFgWcnq3WGN4YCXg; cookiesu=241745947565046; u=241745947565046; device_id=5bdc7ea2c87eea18558ae5840e2b12ce; ssxmod_itna=YqjxyD2QD=it7uD4qbDBQ8G8jRK0QDXDUqAQD2DIqGQGcD8OD0pO6ciewP6IPdAPYiiD5tDlhiTAbDCMPGfDQaYKDGxyhf8e9DgDqN0c7iaXadqhjrDuG7h2RA5wIQ+i3xCPGn7UziYd4xGGD0oDt4DIDAYDDxDWDYoIDGUbDG=D7hroLnb5xi3DbOTDmTXWD1WD0feK=mWoDDtDiTNDKdp5L4DltMjKenhrxGYZY6ekvC6hP+rDjdPD/bwAL+27pISfnCBpP3WwQeGye5Gujjao6aI5glRiES=K4gfx4CD9FuGxn7hPffxHh5=04dB4Lgz8Gq8GDY04=GY9g3bQeDAoSh2LjDVe+2Otn6oIjtDP+HGDBGRBe4ZaD6Cx0WmCjwzlwzmex9DYUGZEhVGGfYD; ssxmod_itna2=YqjxyD2QD=it7uD4qbDBQ8G8jRK0QDXDUqAQD2DIqGQGcD8OD0pO6ciewP6IPdAPYiiDHYD=P4DQhWRjgRpY0EwvNGYnDZgTxD'} # set cookies of header, it is dict type
file=open('stock_data.csv',mode='a',encoding='utf-8',newline='')
csv_write=csv.DictWriter(file,fieldnames=['symbol','name','current','percent','volume'])
csv_write.writeheader()
## open file and write header

for page in range(1,100):
    url='https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page={0}&size=30&order=desc&order_by=percent&market=CN&type=sh_sz'.format(page)
    resopnse=requests.get(url,headers=headers,cookies=cookies)
    print(resopnse)
    json_data=resopnse.json()
    print(json_data)
    data_list=json_data['data']['list'] # get data list
    print(data_list)
    for data in data_list:
    # print(data['symbol'],data['name'],data['current'],data['percent'],data['volume'])
        data_dict={
            'symbol':data['symbol'],
            'name':data['name'],
            'current':data['current'],
            'percent':data['percent'],
            'volume':data['volume']


        } # create a dict for each data
        print(data_dict)
        csv_write.writerow(data_dict)
        # write data to csv file
    print('write data to csv file page={}'.format(page))
file.close()



