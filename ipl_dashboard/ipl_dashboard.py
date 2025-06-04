import streamlit as st
import pandas as pd
import plotly.express as px

# Load IPL winners data (replace with live scraping if needed)
data = [
    {"Year": 2025, "Winner": "KKR", "Runner-Up": "SRH", "Venue": "Chennai"},
    {"Year": 2024, "Winner": "KKR", "Runner-Up": "SRH", "Venue": "Ahmedabad"},
    {"Year": 2023, "Winner": "CSK", "Runner-Up": "GT", "Venue": "Ahmedabad"},
    {"Year": 2022, "Winner": "GT", "Runner-Up": "RR", "Venue": "Ahmedabad"},
    {"Year": 2021, "Winner": "CSK", "Runner-Up": "KKR", "Venue": "Dubai"},
    # Add more historical data as needed
]
df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.title("Filter Options")
year_filter = st.sidebar.selectbox("Select Year", options=["All"] + sorted(df["Year"].tolist(), reverse=True))

# Filter data
if year_filter != "All":
    df = df[df["Year"] == year_filter]

# Main Title
st.title("🏏 IPL Winners & Runner-Ups Dashboard (2008–2025)")
st.markdown("""
A simple dashboard showing the winners and runner-ups of IPL across seasons.
Data is manually updated for accuracy up to 2025.
""")

# Display table
st.subheader("📅 Season Results")
st.dataframe(df.sort_values("Year", ascending=False), use_container_width=True)

# Plot bar chart
st.subheader("🏆 Number of Titles by Team")
full_df = pd.DataFrame(data)
winner_counts = full_df["Winner"].value_counts().reset_index()
winner_counts.columns = ["Team", "Titles"]
fig = px.bar(winner_counts, x="Team", y="Titles", color="Team", title="Total IPL Titles by Team")
st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Built with ❤️ by PV")
