# -*- coding:  euc-kr -*-
import pandas as pd
import json
import os

base_dir = os.path.dirname( os.path.abspath( __file__ ) ) +"/files/"
file_cupang  = base_dir+"result.xlsx"
file_res2  = base_dir+"res2.xlsx"
file_res3  = base_dir+"res3.xlsx"



res1 = pd.read_excel(file_cupang,sheet_name='cupang')
res2 = pd.read_excel(file_res2,sheet_name='Sheet1')

print(res1)
print(res2)


res3 = pd.merge(res1,res2, how ='left', on ='productId')


res3.to_excel(file_res3,sheet_name='cupang',engine='xlsxwriter')

print (res3)
