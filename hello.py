from preswald import connect, get_df, query, text, table, slider, plotly
import pandas as pd
import plotly.express as px

connect()
df = get_df('weather_csv')

sql = "SELECT * FROM weather_csv WHERE Rainfall > 10"
filtered_df = query(sql, "weather_csv")

text("# 🌤️ Weather Data Analysis App")
text("This is an interactive weather data analysis app. Let's explore and analyze the weather data!\n")

text("### Filtered Data (Rainfall > 10mm):")
table(filtered_df)

threshold = slider("Max Temperature Threshold", min_val=0, max_val=50, default=30)
text(f"Current Max Temperature Threshold: {threshold}°C")

filtered_dynamic_df = df[df["MaxTemp"] > threshold]
table(filtered_dynamic_df, title="Filtered Data Based on Max Temp")

fig = px.scatter(
    df,
    x='MaxTemp',
    y='MinTemp',
    color='RainToday',
    title='Max Temperature vs Min Temperature',
    labels={'MaxTemp': 'Max Temp (°C)', 'MinTemp': 'Min Temp (°C)'},
    hover_data=['Rainfall', 'Humidity9am', 'Humidity3pm']
)

fig.update_traces(marker=dict(size=10, opacity=0.6))
fig.update_layout(template='plotly_white')

plotly(fig)

text("Data analysis is complete! 🎉")
