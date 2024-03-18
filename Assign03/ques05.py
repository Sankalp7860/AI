import pandas as pd
import time

data5 = {'TimeStamp': ['2023-08-01 08:50:00', '2024-01-11 12:45:00', '2024-02-01 18:23:00']}
time_df = pd.DataFrame(data5)
time_df['TimeStamp'] = pd.to_datetime(time_df['TimeStamp'])
time_df['Hour'] = time_df['TimeStamp'].dt.hour

print(time_df)
