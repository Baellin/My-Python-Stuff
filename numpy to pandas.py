import numpy as np
import pandas as pd


an_array = np.array([100, 5, 20, 80])
print(an_array)

bear_family = [
    [100, 5, 20, 80],
    [50, 2.5, 10, 40],
    [110, 6, 22, 80]
]
bear_family_numpy = np.array(bear_family)
print(bear_family_numpy)

print(bear_family_numpy[2, 0])

bear_family_df = pd.DataFrame(bear_family, index=['mom', 'baby', 'dad'], columns=['leg', 'hair', 'tail', 'belly'])
print(bear_family_df)

print(bear_family_df.belly)
print(bear_family_df['belly'])

print(bear_family_df.loc['dad'])
print(bear_family_df.iloc[2])

mask = bear_family_df['belly'] == 80
print(bear_family_df[mask])

some_bears = pd.DataFrame([[105, 4, 19, 80], [100, 5, 20, 80]], columns=bear_family_df.columns)
print(some_bears)

all_bears = bear_family_df.append(some_bears)
print(all_bears)

all_bears = all_bears.drop_duplicates()
print(all_bears)

bear_family_df['sex'] = ['f', 'f', 'm']
print(bear_family_df)