import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

hubble = pd.read_csv('hubble_data.csv')

x = hubble.distance.values.reshape(-1,1)
y = hubble.recession_velocity

lr = LinearRegression()
lr.fit(x,y)

plt.xlabel('Distance')
plt.ylabel('Velocity')
plt.title('Data from Hubble')
plt.scatter(x, y, color='black', label='Data points')
plt.plot(x, lr.predict(x), color='red', label='Fitted line', linewidth=3)
plt.grid()
plt.legend()
plt.show()
