import pandas as pd
import numpy as np

np.random.seed(42)

num_rows=1000

data={
    'camera':np.random.randint(8,201,size=num_rows),
    'age':np.random.randint(0,4,size=num_rows),
    'ram':np.random.choice([4,6,8,12,16],size=num_rows),
    'cpu_score':np.random.randint(40,101,size=num_rows),
    'slot_sd':np.random.randint(0,2,size=num_rows),
    'sims':np.random.choice([1,2],size=num_rows),
    'price':np.random.randint(8000,70001,size=num_rows),

}

df=pd.DataFrame(data)

df.to_csv("smartphone_data.csv",index=False)

print(df.head())