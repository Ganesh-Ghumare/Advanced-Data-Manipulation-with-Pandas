CUSTOMER SALES ANALYSIS REPORT
Project Overview
The objective of this project is to analyze customer purchasing patterns and overall sales
performance using real business data. The analysis focuses on identifying top customers,
understanding sales trends, detecting seasonal patterns, evaluating customer retention, and
analyzing product-wise and region-wise performance. The final outcome includes actionable
insights, visual dashboards, pivot-based summaries, and business recommendations.
Datasets Used
Two datasets were used in this project: 1. customer_data.csv – Contains customer information
such as customer ID, name, region, and join date. 2. sales_data.csv – Contains transactional sales
records including order ID, customer ID, product, order date, and revenue.
Data Preparation
Data loading and cleaning steps included handling missing values, removing duplicates, converting
date columns to datetime format, extracting year, month, and day components, standardizing text
fields, merging customer and sales datasets, and creating calculated revenue measures.
Key Performance Indicators
The following KPIs were calculated in the analysis: • Total Revenue • Total Customers • Total
Orders • Average Order Value • Repeat Customer Rate • Top Performing Region
Customer Analysis
Customers were segmented into high value, medium value, and low value groups based on total
revenue contribution. Top customers were identified and lifetime value was calculated to
understand long term contribution to business performance.
Sales Pattern Analysis
Monthly revenue trends were examined to identify seasonal variations and peak demand periods.
Best selling products were analyzed, along with region wise sales distribution to compare
geographic performance.
Advanced Analysis
Cross selling patterns were explored to identify products frequently purchased together. Pivot
tables were used to summarize performance by product, region, and month. Multiple aggregation
functions such as sum, mean, max, and count were applied.
Dashboard and Visualizations
A sales dashboard consisting of bar charts, line charts, and pie charts was developed to visually
communicate business trends and findings effectively.
Insights and Recommendations
Key insights revealed that a small group of high value customers contributes a major share of total
revenue, some regions outperform others, and strong seasonal demand exists during specific
months. Recommended business actions include loyalty programs, targeted marketing, product
bundling, stock optimization during peak seasons, and focused strategies for under performing
regions.
Conclusion
This project successfully demonstrates the use of data analysis techniques for real world business
decision making. Using pandas, merging, grouping, aggregation, pivoting, and visualization
methods provided meaningful insights into customer behavior and sales performance.
