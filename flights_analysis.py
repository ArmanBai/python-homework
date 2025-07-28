import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
%config InlineBackend.figure_format = 'retina'

dtype = {
    "DayOfWeek": np.uint8,
    "DayofMonth": np.uint8,
    "Month": np.uint8,
    "Cancelled": np.uint8,
    "Year": np.uint16,
    "FlightNum": np.uint16,
    "Distance": np.uint16,
    "UniqueCarrier": str,
    "CancellationCode": str,
    "Origin": str,
    "Dest": str,
    "ArrDelay": np.float32,
    "DepDelay": np.float32,
    "CarrierDelay": np.float32,
    "WeatherDelay": np.float32,
    "NASDelay": np.float32,
    "SecurityDelay": np.float32,
    "LateAircraftDelay": np.float32,
    "DepTime": np.float32,
}

flights_df = pd.read_csv("flights_2008.csv.bz2", usecols=dtype.keys(), dtype=dtype)

print(flights_df.shape)
print(flights_df.columns)

flights_df.head()

flights_df.info()

flights_df.describe()

flights_df["UniqueCarrier"].nunique()

# Количество рейсов по перевозчикам 
flights_df.groupby("UniqueCarrier").size().plot(kind="bar");

flights_df.groupby(["UniqueCarrier", "FlightNum"])["Distance"].sum().sort_values(ascending=False).iloc[:3]

flights_df.groupby(["UniqueCarrier", "FlightNum"]).agg({"Distance": [np.mean, np.sum, "count"], "Cancelled": np.sum}
).sort_values(("Distance", "sum"), ascending=False).iloc[0:3]

pd.crosstab(flights_df.Month, flights_df.DayOfWeek)

flights_df.hist("Distance", bins=20);

flights_df["Date"] = pd.to_datetime(
    flights_df.rename(columns={"DayofMonth": "Day"})[["Year", "Month", "Day"]]
)
flights_df.head()

num_flights_by_date = flights_df.groupby("Date").size()
num_flights_by_date.plot();

num_flights_by_date.rolling(window=7).mean().plot();

flights_df["DepHour"] = flights_df["DepTime"] // 100
flights_df["DepHour"].replace(to_replace=24, value=0, inplace=True)
flights_df.head()

flights_df["DepHour"].describe()

import pandas as pd

import numpy as np

dtype = {
    "DayOfWeek": np.uint8,
    "DayofMonth": np.uint8,
    "Month": np.uint8,
    "Cancelled": np.uint8,
    "Year": np.uint16,
    "FlightNum": np.uint16,
    "Distance": np.uint16,
    "UniqueCarrier": str,
    "CancellationCode": str,
    "Origin": str,
    "Dest": str,
    "ArrDelay": np.float32,
    "DepDelay": np.float32,
    "CarrierDelay": np.float32,
    "WeatherDelay": np.float32,
    "NASDelay": np.float32,
    "SecurityDelay": np.float32,
    "LateAircraftDelay": np.float32,
    "DepTime": np.float32,
}
df = pd.read_csv("flights_2008.csv.bz2", usecols=dtype.keys(), dtype=dtype)

df["DepHour"] = (df["DepTime"] // 100).astype("Int64")
df["DepHour"] = df["DepHour"].replace(24, 0)

df["Date"] = pd.to_datetime(df.rename(columns={"DayofMonth": "Day"})[["Year", "Month", "Day"]])

df.head()
import os

df = pd.read_csv("/Users/armanbaigutdinov/Arman Python/flights_2008.csv.bz2", usecols=dtype.keys(), dtype=dtype)

df = pd.read_csv("flights_2008.csv.bz2", usecols=dtype.keys(), dtype=dtype)

top_carriers = df['UniqueCarrier'].value_counts().head(10)
print(top_carriers)

not_in_top = [carrier for carrier in ['DL', 'AA', 'OO', 'EV'] if carrier not in top_carriers.index]
print("Кого нет в списке топ-10:", not_in_top)

cancellation_descriptions = {
    'A': 'Carrier',
    'B': 'Weather',
    'C': 'National Air System',
    'D': 'Security'
}

cancelled_flights = df[df['Cancelled'] == 1]

cancel_counts = cancelled_flights['CancellationCode'].value_counts()
print(cancel_counts)

cancel_counts_named = cancel_counts.rename(index=cancellation_descriptions)
print(cancel_counts_named)

import matplotlib.pyplot as plt

cancel_counts_named.plot(kind='bar')
plt.title('Распределение причин отмены рейсов')
plt.ylabel('Количество')
plt.xlabel('Причина отмены')
plt.show()

#Самая частая причина — это та, у которой будет самое большое число. Обычно это:

#Carrier (A) — если часто отменяют сами перевозчики,
#Weather (B) — если данные из зимнего периода.
#1
cancel_counts = df['Cancelled'].value_counts()
print(cancel_counts)

performed = cancel_counts[0]
cancelled = cancel_counts[1]
difference = performed - cancelled
print(f"Разница: {difference}")
#Выполнено рейсов больше, чем отменено на 6734860
#2
max_dep_delay_flight = df.loc[df['DepDelay'].idxmax()]
max_arr_delay_flight = df.loc[df['ArrDelay'].idxmax()]

print("DepDelay max — Dest:", max_dep_delay_flight['Dest'])
print("ArrDelay max — Dest:", max_arr_delay_flight['Dest'])

same_dest = max_dep_delay_flight['Dest'] == max_arr_delay_flight['Dest']
print("Одинаковый ли аэропорт назначения?", same_dest)

#3
cancelled_flights = df[df['Cancelled'] == 1]
cancelled_by_carrier = cancelled_flights['UniqueCarrier'].value_counts()
print(cancelled_by_carrier)
#4
dep_hour_counts = df['DepHour'].value_counts(normalize=True) * 100  # проценты
dep_hour_sorted = dep_hour_counts.sort_values(ascending=False)
print(dep_hour_sorted)

df = df[df['DepTime'].notna()]
df['DepHour'] = df['DepTime'].astype(int).astype(str).str.zfill(4).str[:2].astype(int)

dep_hour_counts = df['DepHour'].value_counts(normalize=True) * 100 
dep_hour_sorted = dep_hour_counts.sort_values(ascending=False)
print(dep_hour_sorted.head(5))
#5
df = df[df['DepTime'].notna()] 
df['DepHour'] = df['DepTime'].astype(int).astype(str).str.zfill(4).str[:2].astype(int)
total_by_hour = df['DepHour'].value_counts().sort_index()
cancelled_by_hour = df[df['Cancelled'] == 1]['DepHour'].value_counts().sort_index()

cancel_percent_by_hour = (cancelled_by_hour / total_by_hour * 100).fillna(0).sort_values()
print(cancel_percent_by_hour.head(10))

#6
for hour in [3, 19, 22, 4]:
    percent = cancel_percent_by_hour.get(hour, 0)
    print(f"Час {hour}: {percent:.6f}% отмен")

#7
completed_flights = df[df['Cancelled'] == 0]
completed_by_hour = completed_flights['DepHour'].value_counts().sort_values(ascending=False)
print(completed_by_hour.head(5))
#9
mq_completed = df[(df['UniqueCarrier'] == 'MQ') & (df['Cancelled'] == 0)]	
mq_hourly_distribution = mq_completed['DepHour'].value_counts().sort_values(ascending=False)
print(mq_hourly_distribution.head(10))
#8
completed = df[df['Cancelled'] == 0]
avg_dep_delay_by_hour = completed.groupby('DepHour')['DepDelay'].mean()
print(avg_dep_delay_by_hour)	

#12
df['Route'] = df['Origin'] + '-' + df['Dest']
route_counts = df['Route'].value_counts()
print(route_counts.head(10))
# 13
df['Route'] = df['Origin'] + '-' + df['Dest']
delayed_departures = df[df['DepDelay'] > 0]	
top_5_delayed_routes = delayed_departures['Route'].value_counts().head(5)
print(top_5_delayed_routes)
top_routes_flights = df[df['Route'].isin(top_5_routes_list)]
df['Route'] = df['Origin'] + '-' + df['Dest']

delayed_departures = df[df['DepDelay'] > 0]
top_5_delayed_routes = delayed_departures['Route'].value_counts().head(5)
print(top_5_delayed_routes)
top_5_routes_list = top_5_delayed_routes.index.tolist()
print(top_5_routes_list)
top_routes_flights = df[df['Route'].isin(top_5_routes_list)]
weather_delays = top_routes_flights[
    (top_routes_flights['DepDelay'] > 0) &
    (top_routes_flights['WeatherDelay'] > 0)
]
print("Рейсов задержано из-за погоды:", len(weather_delays))
#14
dep_counts = df['DepHour'].value_counts().sort_index()
print(dep_counts)
#15
df['FlightDate'] = pd.to_datetime(df[['Year', 'Month', 'DayofMonth']])
print(df.columns)

df['FlightDate'] = pd.to_datetime(df[['Year', 'Month', 'DayofMonth']])
df['FlightDate'] = pd.to_datetime(df[['Year', 'Month', 'DayofMonth']].rename(
    columns={'Year': 'year', 'Month': 'month', 'DayofMonth': 'day'}
))

df['Weekday'] = df['FlightDate'].dt.dayofweek  
df['MonthNum'] = df['FlightDate'].dt.month
weekday_counts = df['Weekday'].value_counts().sort_index()
monthly_counts = df['MonthNum'].value_counts().sort_index()
print("По дням недели:\n", weekday_counts)
print("\nПо месяцам:\n", monthly_counts)