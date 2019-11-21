# this program reads an excel sheet and put the information on to a calendar

import numpy
import panda as pd
from panda import ExcelWriter
from panda import ExcelFile

df = pd.read_excel('ERCDeskEvents.xls', sheetname='Sheet1')

print("Column headings:")
print(df.columns)

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

df = pd.DataFrame({'a':[1,3,5,7,4,5,6,4,7,8,9],
                   'b':[3,5,6,2,4,6,7,8,7,8,9]})

writer = ExcelWriter('Pandas-Example2.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()
