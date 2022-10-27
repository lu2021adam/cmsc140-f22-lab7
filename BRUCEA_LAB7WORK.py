# Adam Bruce

import pandas as pd
from pathlib import Path


regionFile = Path("city_temperature.csv")

regionData = pd.read_csv(regionFile, sep = ",")

print(regionData.head())

groupedData = regionData.groupby(['Region'])

idx_max = groupedData['AvgTemperature'].idxmax()

print(idx_max)

maxTemps = regionData.loc[idx_max]

outfile = Path("city_maxtemp.csv")

maxTemps.to_csv(outfile, index = False)





