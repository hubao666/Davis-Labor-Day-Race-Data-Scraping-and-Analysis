## Topic
This project uses web-scraping collect the data and analyzes data from the Davis Labor Day Running Races to explore factors affecting running endurance, focusing on age, gender, race distance, and the impact of the COVID-19 pandemic.

## Methodology
Using Python's BeautifulSoup and requests libraries, race data (names, ages, finish times, gender, race type, and year) were scraped from the official website. Data was processed with pandas and visualized using plotly.express. The analysis examined speed and pace differences by age and gender, as well as pre- and post-pandemic performance.

## Tools
- Web Scraping: BeautifulSoup, requests
- Data Processing: pandas
- Visualization: plotly.express
- Storage: CSV format

## Results
- __Age Group Performance__: The fastest runners are typically in the 10-19 age group, showing the highest average speed and lowest average pace. On the other hand, those aged 90+ have the slowest average speed and the highest pace.

- __Gender Differences__: Across both the 5k and 10k distances, males tend to have faster speeds and better paces compared to females within the same age group. However, the gap in performance varies by age, with the largest differences typically seen in older age groups.

- __Impact of COVID__: After COVID, the < 10 and 80-89 age groups became faster, improving both speed and pace. However, the 10-19 and 30-39 age groups slowed down, showing a decrease in speed and an increase in pace. This suggests different age groups experienced varying impacts on their fitness due to pandemic-related changes.

## Note on Data Collection:
- This project originally included two functions to scrape age and time data from official race websites. However, due to recent changes in the structure of these data tables, these functions are currently not working.

- For now, you can still use the notebook by loading data from the previously scraped and saved files for analysis.

- In the future, I may update these functions to accommodate the new table structure and restore the scraping functionality.

