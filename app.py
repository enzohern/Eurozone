# Importation of Bookstores
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import pycountry


# Data Loading and Preprocessing
file_pathgp = r"C:\Users\user\Desktop\PIC_EURO\df_Public_spending.cvs"
df_Public_spending = pd.read_csv(file_pathgp)
file_pathdsp = r"C:\Users\user\Desktop\PIC_EURO\df_UNEMPLOYMENT.cvs"
df_UNEMPLOYMENT = pd.read_csv(file_pathdsp)
file_pathipc = r"C:\Users\user\Desktop\PIC_EURO\df_IPC.cvs"
df_IPC = pd.read_csv(file_pathipc)
file_pathpibp = r"C:\Users\user\Desktop\PIC_EURO\df_GDP_PC.cvs"
df_GDP_PC = pd.read_csv(file_pathpibp)
file_pathp = r"C:\Users\user\Desktop\PIC_EURO\df_Population.cvs"
df_Population = pd.read_csv(file_pathp)
file_pathtpib = r"C:\Users\user\Desktop\PIC_EURO\df_GDP_rate.cvs"
df_GDP_rate = pd.read_csv(file_pathtpib)

# Rename columns that vary (OBS_VALUE in each DataFrame) with unique names
df_Public_spending.rename(columns={'OBS_VALUE': 'Public_spending'}, inplace=True)
df_UNEMPLOYMENT.rename(columns={'OBS_VALUE': 'UNEMPLOYMENT'}, inplace=True)
df_IPC.rename(columns={'OBS_VALUE': 'IPC'}, inplace=True)
df_GDP_PC.rename(columns={'OBS_VALUE': 'GDP_PC'}, inplace=True)
df_Population.rename(columns={'OBS_VALUE': 'Population'}, inplace=True)
df_GDP_rate.rename(columns={'OBS_VALUE': 'GDP_rate'}, inplace=True)

# List of DataFrames
dfs = [df_Public_spending, df_UNEMPLOYMENT, df_IPC, df_GDP_PC, df_Population, df_GDP_rate]

# Join the merged DataFrames sequentially using 'geo' and 'TIME_PERIOD'
df_merged = dfs[0]  # with the first DataFrame
for df in dfs[1:]:
    df_merged = pd.merge(df_merged, df, on=['geo', 'TIME_PERIOD'], how='inner')  # Internal Union

# See the final result
print(df_merged)

# Assume 'geo' is the column with country names in English in your DataFrame

def get_iso_code(country):
    try:
        # Look up the country and get its ISO-3 code
        return pycountry.countries.lookup(country).alpha_3
    except LookupError:
        # If the country is not found, return None
        return None

# Apply the function to create a new column with ISO codes
df_merged['iso_code'] = df_merged['geo'].apply(get_iso_code)

# Verify the result
print(df_merged[['geo', 'iso_code']].head())

# Calculate the correlation matrix
correlation = df_merged[['Public_spending', 'UNEMPLOYMENT', 'IPC', 'GDP_PC', 'Population', 'GDP_rate']].corr()

# Streamlit App
st.title("Analysis of Eurozone Economic Indicators (2015-2023)")
st.write("This project analyses several economic indicators of the Eurozone countries between 2015 and 2023.")

# Introduction
st.header("Introduction")
st.write(""" 
    <div style="text-align: justify;">
         This project seeks to examine the economic behavior of the Eurozone member countries during the period from 2015 to 2023. The Eurozone, a region formed by developed economies that share a common currency, the euro, has experienced significant global and regional events during this time, such as financial crises, political changes, and the COVID-19 pandemic, which may have impacted the economic performance of its member states. This research aims to observe trends and correlations between various key economic indicators, employing a quantitative approach based on data visualization.

The analysis focuses on fundamental economic indicators such as the unemployment rate, public spending, gross domestic product (GDP) per capita, GDP growth rate, and the consumer price index (CPI), with the goal of understanding how these factors interact and what trends emerge over time. For instance, it aims to observe how the unemployment rate relates to public spending, or how GDP growth may be linked to inflation or unemployment. Although the study does not operate on a specific hypothesis, it will help identify patterns of economic growth and decline, and their impact on the population of Eurozone countries.

The project is aimed at a general audience interested in the region’s economy, providing an accessible and concise overview of the macroeconomic dynamics of these countries. While advanced techniques of data analysis and visualization are employed, the goal is to offer an understandable approach for anyone wishing to explore the economic trends of the Eurozone.
        </div>
         """,unsafe_allow_html=True)

# Methodology
st.header("Methodology")
st.write("""
   <div style="text-align: justify;"> 
The data analysis was conducted using a quantitative and exploratory approach, leveraging Python and Streamlit for interactive data visualization. Below is an outline of the main steps in the methodology:

Data Collection: Economic data were sourced from Eurostat, which provides reliable macroeconomic statistics for Eurozone countries.

Data Cleaning: Prior to analysis, I carried out preprocessing and data cleaning tasks, including removing missing values, normalizing column names, and handling incomplete data. Croatia was excluded from the study as it joined the Eurozone in 2023 and lacks consistent data for the entire analysis period.

Data Merging: I combined several datasets (public spending, unemployment rate, GDP per capita, CPI, GDP growth rate, and population) into a single DataFrame to facilitate the joint analysis of different indicators.

Exploratory Data Analysis (EDA): Tools like Pandas and Seaborn were used for correlation analysis and visual exploration of the data to observe the evolution of the indicators over time. A correlation matrix was computed to identify key relationships between the different economic indicators.

Data Visualization: The core of this project is the interactive presentation of the data using Streamlit and Plotly. I designed scatter plots, timelines, and interactive maps to allow users to explore trends by country and economic indicator. These visualizations enable the selection of different countries and years, allowing for visual comparisons of relationships between indicators, such as unemployment and public spending, or GDP per capita and the GDP growth rate.

Interpretation and Conclusions: By visualizing trends, I identified patterns and correlations between the economic indicators. Although the analysis is descriptive, these trends may offer insights into how factors like GDP growth or public spending influence other aspects of the economy.

This structured approach ensured a comprehensive understanding of the economic dynamics within the Eurozone during the period under review.
        </div>
         """, unsafe_allow_html=True)

# Filter a DataFrame with Eurozone countries
df_mapa_eurozona = df_merged[['geo', 'iso_code']].drop_duplicates()  # Only take single countries and their ISO codes

# Create a simple map with Plotly Express, focusing on Europe
fig_simple_map = px.choropleth(df_mapa_eurozona, 
                                locations="iso_code",  # ISO-3 Country Codes
                                hover_name="geo",  # Show country names on hover
                                title="Mapa de Referencia: Países de la Eurozona",
                                color_discrete_sequence=["#B0C4DE"],  # Simple color for countries
                                labels={'geo': 'Country'})

# Adjustments to center the map on Europe and improve the display
fig_simple_map.update_geos(
    projection_type="mercator",  # Mercator projection
    center={"lon": 10, "lat": 50},  # Focused on Europe
    projection_scale=4.5,  # Zoom scale
    showcoastlines=True, coastlinecolor="black",  # Show the coasts
    showland=True, landcolor="#E5E5E5",  # Light color for the earth
    showocean=True, oceancolor="#ADD8E6",  # Color of the ocean
    showframe=False,  # Hide map frame
    showcountries=True, countrycolor="darkgray"  # Colors for countries
)

# Adjust map size
fig_simple_map.update_layout(
    width=1000,  # Figure width
    height=600,  # Figure height
    title={
        'text': "Reference Map: Eurozone Countries",  # Title
        'y':0.95,  # Vertical position (closer to 1 is higher)
        'x':0.5,   # Horizontal position (0.5 is centered)
        'xanchor': 'center',  # Anchor text horizontally
        'yanchor': 'top',     # Anchor text vertically
        'font': {'size': 24}  # Title font size
    }
)

# Show map in Streamlit
st.plotly_chart(fig_simple_map)

# Mostrar el heatmap de correlaciones
st.header("Correlation between Economic Indicators")
fig, ax = plt.subplots(figsize=(10, 6))  # Set the size of the figure
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Header: Trends by Country
st.header("Trends in Economic Indicators by Country")

# Select a country
selected_country = st.selectbox("Select a country", df_merged['geo'].unique())

# Filter the DataFrame by the selected country
df_pais = df_merged[df_merged['geo'] == selected_country]

# Column selection (economic indicator)
selected_indicator = st.selectbox("Select the economic indicator", 
                                      ['Public_spending', 'UNEMPLOYMENT', 'IPC', 'GDP_PC', 'Population', 'GDP_rate'])

# Gráfico de línea para el indicador seleccionado
fig = px.line(df_pais, 
              x='TIME_PERIOD', 
              y=selected_indicator, 
              title=f"Evolution of {selected_indicator.replace('_', ' ').title()} in {selected_country}",
              labels={'TIME_PERIOD': 'Year', selected_indicator: selected_indicator.replace('_', ' ').title()})

# Show the graph in Streamlit
st.plotly_chart(fig)


# Get the unique years available in the DataFrame
anios_unicos = sorted(df_merged['TIME_PERIOD'].unique())

# Create buttons to select the year
st.write("Select a year to filter the data:")
selected_year = st.radio("Available years", anios_unicos, key='selected_year')

# Filter data by selected year
df_year = df_merged[df_merged['TIME_PERIOD'] == selected_year]

# Scatter plot for the selected year
st.title(f"Relationship between Unemployment and Public Spending in {selected_year}")
fig = px.scatter(df_year, 
                 x='UNEMPLOYMENT', 
                 y='Public_spending',  # Asegúrate de usar la columna correcta
                 color='geo', 
                 size='Population', 
                 hover_name='geo', 
                 title=f'Relationship between Unemployment and Public Spending in {selected_year}',
                 labels={'UNEMPLOYMENT': 'Unemployment Rate (%)', 'Public_spending': 'Public Spending (%)', 'geo': 'Country'})

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig)

st.title(f"Relationship between GDP per capita and GDP growth rate in {selected_year}")
fig = px.scatter(df_year, 
                 x='GDP_PC', 
                 y='GDP_rate', 
                 color='geo', 
                 size='Population', 
                 hover_name='geo', 
                 title=f'Relationship between GDP per capita and GDP growth rate in {selected_year}',
                 labels={'GDP_PC': 'GDP per capita (Euro)', 'GDP_rate': 'GDP growth rate (%)', 'geo': 'Country'})
st.plotly_chart(fig)

st.title(f"Relationship between GDP growth and the Consumer Price Index in {selected_year}")
fig = px.scatter(df_year, 
                 x='GDP_rate', 
                 y='IPC', 
                 color='geo', 
                 size='Population', 
                 hover_name='geo', 
                 title=f'Relationship between GDP growth and the Consumer Price Index in {selected_year}',
                 labels={'GDP_rate': 'GDP growth Rate (%)', 'IPC': 'Consumer Price Index (%)', 'geo': 'Country'})
st.plotly_chart(fig)

# Comparison between countries
st.header("Comparison of Indicators between Countries")

# Selection of several countries
selected_countries = st.multiselect("Select countries to compare", df_merged['geo'].unique())

# Selecting the economic indicator to compare
comparison_indicator = st.selectbox("Select the economic indicator to compare", 
                                     ['Public_spending', 'UNEMPLOYMENT', 'IPC', 'GDP_PC', 'Population', 'GDP_rate'])

# Check if there are selected countries
if selected_countries:
    # Filter data by selected countries
    df_comparison = df_merged[df_merged['geo'].isin(selected_countries)]
    
    # Comparison chart of the selected indicator between the selected countries
    fig_comparison = px.line(df_comparison, 
                             x='TIME_PERIOD', 
                             y=comparison_indicator, 
                             color='geo', 
                             title=f"Comparison of {comparison_indicator.replace('_', ' ').title()} between countries",
                             labels={comparison_indicator: comparison_indicator.replace('_', ' ').title(), 'geo':'Country', 'TIME_PERIOD':'Year'})
    
    # Show the graph in Streamlit
    st.plotly_chart(fig_comparison)

# Conclusion
st.header("Conclusions of the Analysis")
st.write("""
    <div style="text-align: justify;">
    This analysis has provided an overview of the economic activity of Eurozone countries between 2015 and 2023, exploring the relationship between key indicators such as the unemployment rate, public spending, GDP per capita, and inflation. Throughout this period, the Eurozone experienced various economic fluctuations influenced by global and regional factors, including the COVID-19 pandemic and other crises.

One of the most notable findings was the correlation between unemployment and public spending, which varied significantly between nations. Additionally, we observed that GDP growth showed notable links with other indices, such as the consumer price index (CPI), reflecting how economic progress can influence inflation.

However, this analysis has some limitations, such as the omission of Croatia due to its late entry into the Eurozone in 2023 and the scarcity of detailed data for certain indicators. Despite these constraints, the results offer a solid foundation for policymakers to better understand the dynamics of the region.

In the future, it would be interesting to expand this analysis to include other economic or social factors, as well as to explore how recent events, such as the energy crisis in Europe, may affect the Eurozone's economic indicators. The addition of more up-to-date data would also enable a more current analysis of trends in this region.
        </div>
         """, unsafe_allow_html=True)
