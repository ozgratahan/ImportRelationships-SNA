IMPORT RELATIONSHIPS OF EUROPEAN COUNTRY- Social Network Analysis

Project Overview:


This project focuses on analyzing the import relationships among European countries using Social Network Analysis (SNA). The goal is to examine how countries interact with each other through imports, providing a deeper understanding of trade networks in Europe. The analysis involves calculating centrality measures for each country, visualizing the network, and deriving insights from both individual and global measures.


Data Description:


The dataset consists of import data between European countries, which was collected using Selenium for web scraping. The data is structured in the following format:


Source Country: The country exporting goods.

Target Country: The country importing goods.

Weight: The volume or value of imports between the countries.


The data was scraped from an online source that provides real-time trade information between European countries. After scraping the data, it was cleaned and preprocessed to ensure consistency and completeness.



Data Collection Process:

Web Scraping with Selenium: Selenium was used to automate the extraction of import data from web pages. The data collection process involved navigating through trade statistics web pages, locating relevant tables, and extracting the necessary information (countries and their respective import volumes).


Data Cleaning: The raw data was cleaned using Python’s Pandas library to handle missing values, remove duplicates, and ensure the dataset is ready for analysis.



Network Construction and Visualization:


Gephi for Network Visualization: After processing and cleaning the data, the import relationships were transformed into a network structure and visualized using Gephi. Gephi helped in rendering the network graph and allowed us to explore the structure and centrality measures of the trade relationships.



Analysis Focus:


Measures:


Indegree: The number of countries that import from a specific country.

Outdegree: The number of countries a specific country exports to.

Betweenness Centrality: Measures the influence of a country as an intermediary in trade relationships.

Closeness Centrality: Reflects how easily a country can reach other countries in the trade network.



Required Libraries:


pandas: For data manipulation and cleaning.

numpy: For numerical operations and handling of missing data.

selenium: For web scraping and extracting data from online sources.



Conclusion:

This project provides valuable insights into the import dynamics within Europe, offering a deeper understanding of the countries that dominate the trade network. The analysis can be used to inform policymakers, businesses, and researchers about the structure and flow of goods in the European market.
