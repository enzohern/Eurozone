This project seeks to examine the economic behavior of the Eurozone member countries during the period from 2015 to 2023. The Eurozone, a region formed by developed economies that share a common currency, the euro, has experienced significant global and regional events during this time, such as financial crises, political changes, and the COVID-19 pandemic, which may have impacted the economic performance of its member states. This research aims to observe trends and correlations between various key economic indicators, employing a quantitative approach based on data visualization.

The analysis focuses on fundamental economic indicators such as the unemployment rate, public spending, gross domestic product (GDP) per capita, GDP growth rate, and the consumer price index (CPI), with the goal of understanding how these factors interact and what trends emerge over time. For instance, it aims to observe how the unemployment rate relates to public spending, or how GDP growth may be linked to inflation or unemployment. Although the study does not operate on a specific hypothesis, it will help identify patterns of economic growth and decline, and their impact on the population of Eurozone countries.

The project is aimed at a general audience interested in the region’s economy, providing an accessible and concise overview of the macroeconomic dynamics of these countries. While advanced techniques of data analysis and visualization are employed, the goal is to offer an understandable approach for anyone wishing to explore the economic trends of the Eurozone.

Methodology

The data analysis was conducted using a quantitative and exploratory approach, leveraging Python and Streamlit for interactive data visualization. Below is an outline of the main steps in the methodology:

Data Collection: Economic data were sourced from Eurostat, which provides reliable macroeconomic statistics for Eurozone countries.

Data Cleaning: Prior to analysis, I carried out preprocessing and data cleaning tasks, including removing missing values, normalizing column names, and handling incomplete data. Croatia was excluded from the study as it joined the Eurozone in 2023 and lacks consistent data for the entire analysis period.

Data Merging: I combined several datasets (public spending, unemployment rate, GDP per capita, CPI, GDP growth rate, and population) into a single DataFrame to facilitate the joint analysis of different indicators.

Exploratory Data Analysis (EDA): Tools like Pandas and Seaborn were used for correlation analysis and visual exploration of the data to observe the evolution of the indicators over time. A correlation matrix was computed to identify key relationships between the different economic indicators.

Data Visualization: The core of this project is the interactive presentation of the data using Streamlit and Plotly. I designed scatter plots, timelines, and interactive maps to allow users to explore trends by country and economic indicator. These visualizations enable the selection of different countries and years, allowing for visual comparisons of relationships between indicators, such as unemployment and public spending, or GDP per capita and the GDP growth rate.

Interpretation and Conclusions: By visualizing trends, I identified patterns and correlations between the economic indicators. Although the analysis is descriptive, these trends may offer insights into how factors like GDP growth or public spending influence other aspects of the economy.

This structured approach ensured a comprehensive understanding of the economic dynamics within the Eurozone during the period under review.