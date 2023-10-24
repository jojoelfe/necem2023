from pathlib import Path
import mdocfile
import pandas as pd

from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter, HourLocator
mdoc_files = Path('/data/elferich/CryoTEM/Johannes_20231006/Johannes_20231006').glob('*/*/frames/*.mdoc')

time_list = []

for mdoc in mdoc_files:
    data = mdocfile.read(mdoc)
    time = pd.to_datetime(data["DateTime"],format='%d-%b-%Y  %H:%M:%S')
    time_list.append(time.iloc[0])

time_list = pd.Series(time_list)
time_list = time_list.sort_values()


# Create Dataframe with times and accumulate number of collected micrtographs
time_list = time_list.to_frame()
time_list['num_micrographs'] = range(1,len(time_list)+1)

time_list.plot(x=0,y=1)

# Hide legend
plt.gca().get_legend().remove()
plt.gca().xaxis.set_major_locator(HourLocator(byhour=range(0, 24, 6)))
plt.gca().xaxis.set_major_formatter(DateFormatter('%a %H:%M'))
plt.xlabel('Time')
plt.ylabel('# Micrographs')




plt.show()

