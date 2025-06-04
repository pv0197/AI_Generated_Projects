import streamlit as st
import pandas as pd
import plotly.express as px

# IPL data (winners and runner-ups from 2008 to 2025)
data = [
    {"Year": 2008, "Winner": "Rajasthan Royals", "Runner-up": "Chennai Super Kings"},
    {"Year": 2009, "Winner": "Deccan Chargers", "Runner-up": "Royal Challengers Bangalore"},
    {"Year": 2010, "Winner": "Chennai Super Kings", "Runner-up": "Mumbai Indians"},
    {"Year": 2011, "Winner": "Chennai Super Kings", "Runner-up": "Royal Challengers Bangalore"},
    {"Year": 2012, "Winner": "Kolkata Knight Riders", "Runner-up": "Chennai Super Kings"},
    {"Year": 2013, "Winner": "Mumbai Indians", "Runner-up": "Chennai Super Kings"},
    {"Year": 2014, "Winner": "Kolkata Knight Riders", "Runner-up": "Kings XI Punjab"},
    {"Year": 2015, "Winner": "Mumbai Indians", "Runner-up": "Chennai Super Kings"},
    {"Year": 2016, "Winner": "Sunrisers Hyderabad", "Runner-up": "Royal Challengers Bangalore"},
    {"Year": 2017, "Winner": "Mumbai Indians", "Runner-up": "Rising Pune Supergiant"},
    {"Year": 2018, "Winner": "Chennai Super Kings", "Runner-up": "Sunrisers Hyderabad"},
    {"Year": 2019, "Winner": "Mumbai Indians", "Runner-up": "Chennai Super Kings"},
    {"Year": 2020, "Winner": "Mumbai Indians", "Runner-up": "Delhi Capitals"},
    {"Year": 2021, "Winner": "Chennai Super Kings", "Runner-up": "Kolkata Knight Riders"},
    {"Year": 2022, "Winner": "Gujarat Titans", "Runner-up": "Rajasthan Royals"},
    {"Year": 2023, "Winner": "Chennai Super Kings", "Runner-up": "Mumbai Indians"},
    {"Year": 2024, "Winner": "Gujarat Titans", "Runner-up": "Lucknow Super Giants"},
    {"Year": 2025, "Winner": "Royal Challengers Bangalore", "Runner-up": "Punjab Kings"},
]

# Create DataFrame
df = pd.DataFrame(data)

st.title("IPL Winners & Runner-ups Dashboard")

# Sidebar - filter by year (show all years sorted)
years = sorted(df["Year"].unique())
selected_year = st.sidebar.selectbox("Select Year", ["All"] + [str(y) for y in years])

# Filter dataframe based on selection
if selected_year == "All":
    filtered_df = df
else:
    filtered_df = df[df["Year"] == int(selected_year)]

st.subheader(f"IPL Results ({selected_year})")
st.table(filtered_df)

# Bar chart: Total titles by each team (Winner count)
title_counts = df["Winner"].value_counts().reset_index()
title_counts.columns = ["Team", "Titles"]

fig = px.bar(title_counts, x="Team", y="Titles", title="Total IPL Titles by Team", text="Titles")
fig.update_traces(textposition='outside')
fig.update_layout(yaxis=dict(dtick=1))
st.plotly_chart(fig, use_container_width=True)
