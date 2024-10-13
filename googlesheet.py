import pandas as pd

gsheetid = "12drIPzH7_VSEkBxehN9-fsdYZ4Rfk351jr2GphlCMec"
sheet_name = "Purchase"

gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

df = pd.read_csv(gsheet_url)
df.to_excel("C:\\Users\\HP\\Desktop\\abcd.xlsx")
