

# Segmentation Districts of Istanbul

## Business Case

One of the most known fast-food company is willing to open the first restaurant in Istanbul. They want to get optimal district in Istanbul to open their first branch.They want to get a data centric solution.

You can see the dashboard app >>>>  [here](https://share.streamlit.io/ugursavci/segmentation_districts_of_istanbul/main/app.py)

<img src='https://github.com/ugursavci/Segmentation_Districts_of_Istanbul/blob/main/dashboard.png'>




### Data Collection using Beautiful Soup

- Web Scrabing from Wikipedia in order to get demographic and economic information about Districts.
- Web Scrabing from famous burger companies in Turkey in order to get total count of branches per each District.
- Foursquare APİ in order to get  total number of venues by type
- Getting latitude and longitude data using **geopy** module 

### Data Cleaning

For the Data from Wikipedia

- Dropped unnecesssary rows
- Corrected the column names 
- Cleaned data using split,replace,strip and lambda function 

For the Competitors Burger Brand

- Corrected District Name
- Text cleaning in order to get standard format for each district

### Data Analysis
- Created map using follium module in order to see each Districts visually
- Created visualization in order to see information such as  total competitors,total venues,populations,annual income by districts

### Modeling 

- Filtered data and built a K-Means algorithm to segment our data into groups.

### Creating Web App using Streamlit 

- Created dashboard  by using Streamlit and deployed it to the web server.



You can see the dashboard app [here](https://share.streamlit.io/ugursavci/segmentation_districts_of_istanbul/main/app.py)
