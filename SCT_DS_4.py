import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

data = pd.read_csv("traffic_accidents.csv")

data.dropna(inplace=True)

data['accident_datetime'] = pd.to_datetime(data['accident_datetime'])

data['hour_of_day'] = data['accident_datetime'].dt.hour
data['day_of_week'] = data['accident_datetime'].dt.day_name()
data['month'] = data['accident_datetime'].dt.month_name()

plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='hour_of_day', bins=24, kde=True)
plt.title('Accident Frequency by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='day_of_week', data=data, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Accident Frequency by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='month', data=data, order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.title('Accident Frequency by Month')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['longitude'], data['latitude']))
gdf.plot(figsize=(10, 8))
plt.title('Accident Hotspots')
plt.show()

correlation_matrix = data[['weather_condition', 'road_condition', 'accident_severity']].corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()