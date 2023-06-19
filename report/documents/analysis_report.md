# Sylndr
# Analysis Report: Estimating Prices for Used Cars

## Introduction
The aim of this analysis report is to provide insights into the process of estimating prices for used cars in the context of Sylndr's business model. As a company specializing in buying used cars from customers, accurately determining the appropriate price for each vehicle is crucial for ensuring fair transactions and maintaining competitive advantage in the market.

Estimating the price of a used car involves considering various factors, such as the car's model, the distance it has traveled (moved kilometers), and the year of its manufacturing. Additionally, competitor prices for similar cars play a significant role in determining the appropriate price to offer our customers. By analyzing these factors and the market dynamics, we can develop a robust pricing strategy that aligns with customer expectations and market trends.

In this analysis, we will leverage a comprehensive dataset that includes information about the car features, competitor prices, and the date at which the competitors added their prices. While the actual true price for used cars is unknown, we will estimate the appropriate price based on the given features and consider the competitor prices as a reference point. It is important to note that not all competitor prices may be logical, and we will carefully analyze and evaluate the data to ensure the reliability of our estimates.

Through this analysis, we aim to gain insights into the key factors influencing used car prices, identify patterns or trends in the market, and develop a data-driven approach for estimating prices that aligns with customer expectations and the competitive landscape. By leveraging the power of data science and statistical techniques, we can enhance our decision-making process and optimize our pricing strategy for buying used cars from customers.

The following sections of this report will delve into the details of the analysis, including data preprocessing, descriptive statistics, correlation analysis, feature importance, time series analysis, competitor price analysis, market segmentation, and provide recommendations based on the findings.

## Data Overview
The analysis is based on given dataset that contains information relevant to estimating the prices of used cars.

The dataset includes the following columns:
| Column | Description|
|--------|------------|
| Car Manufacturing Company | The manufacturing company for the used car. Indicates the brand of the car. The only given data are for used cars from Nissan.|
| Car Model | The specific model of the used car. In this dataset, there are 6 unique types of used cars models manufactured by Nissan {Juke', 'Juke Platinium', 'Qashqai', 'Sentra', 'Sunny', 'Tiida'}|
| Car Manufacturing Year | The Manufacturing year of each car model. Indicates the age of the vehicle, which is a significant factor in determining its value.|
| Moved Kilometers | The distance in kilometers that each car has traveled. This column reflects the wear, tear, and overall condition of the vehicle.|
| Car Transmission Type | The transmission type of car which is either manual or automatic.|
| Car Extra Features | Additional features or characteristics of the car that may influence its price. Examples include the presence of advanced technology, safety features, or unique modifications.|
|Competitor Price| The price set by competitors for similar used cars. Serves as a reference and comparison for estimating the appropriate price for each car.|
|Priced_at|The date on which the competitor price was added. Allows analysis of trends and patterns in competitor prices over time.|

## Most important KPIs
|KPI| Description|
|---|------------|
|Acqusition Cost| Measures the average cost incurred by the company to acquire each used car. <br/>This includes factors such as the purchase price from the seller, any associated fees, and transportation cost. <br/>Sylndr should aim to keep the acquisition cost as low as possible to maximize profitability.| 
|Profitability| Main kpi the company should aim to maximize the profit margin on each acquaired car. <br/>This could be achieved by accurately estimating the appropriate buying price based on the car's features, condition, market demands, and competitor prices.|
|Quality of Inventory| Can be measured by evaluating the condition of the cars, their maintenance history, and the presence of any significant issues or damages. <br/>Maintaining a high-quality inventory helps attract customers and ensures better resale opportunities. <br/>In this dataset, extra_features column could be considered as quality of inventory.|
|Turnaround Time| Referes to the duration between acquiring a used car and selling it. <br/>A shorter turnaround time allows the company to quickly recoup their investment and maximize cash flow. <br/>Calculation by dividing the total number of cars sold within a specific period by the average number of cars in inventory during that period.|
|Inventory Turnover|Measures how quickly the company buys and sells used cars. <br/>A higher inventory turnover indicates efficient operations and a better utilization of resources. <br/>It can be calculated by dividing the total number of cars sold within a specific period by the average number of cars in inventory during that period|
|Market Demands| Monitoring the market demands is essential for determining the types of used cars that are high in demand. <br/>Analyzing customer preferences and market trends can guide the company in focusing on popular car models, features, and price ranges, which can result in faster sales and higher profits.|
|Market Share| Monitoring the company's market share in the used car buying market is important to assess its competitive position. <br/>Increasing market share indicates that the company is successfully attracting sellers and outperforming competitors.|
|Customer Satisfaction| Although the company focuses on buying used cars, maintaining good relationships with sellers is crucial. <br/>Positive customer experiences can lead to word-of-mouth referrals and a larger pool of potential sellers. <br/>Gathering feedback from sellers can provide insights into their satisfaction level and identify areas for improvement.|

|KPI| Calculation Method|
|---|-------------------|
|Acquisition Cost| Calculate the total cost incurred to acquire used cars (purchase price, fees, transportation costs, etc.). <br/>Divide the total acquisition cost by the number of cars acquired to get the average acquisition cost per car.|
|Profitability| Calculate the profit for each sold car by subtracting the acquisition cost from the selling price. <br/>Calculate the profit margin by dividing the total profit by the total revenue (sum of selling prices). <br/>Alternatively, calculate the return on investment (ROI) by dividing the total profit by the total investment.|
|Quality of inventory| Establish criteria for evaluating the quality of the acquired inventory (e.g., condition, maintenance history, damages). <br/>Assess each car against the defined criteria and assign a quality score or label. <br/>Calculate the percentage or ratio of high-quality cars in the inventory.|
|Turnaround Time| Track the acquisition date and the sale date for each car. <br/>Calculate the time difference (in days or any other unit) between acquisition and sale for each car. <br/>Calculate the average turnaround time by averaging the time differences across all sold cars.|
|Inventory Turnover| Track the number of used cars sold within a specific period (e.g., monthly, quarterly, annually). <br/>Calculate the average number of cars in inventory during that period. <br/>Divide the number of cars sold by the average inventory count to calculate the inventory turnover ratio.|
|Market Demands| Analyze market trends and customer preferences through market research, surveys, or monitoring industry reports. <br/>Identify popular car models, features, and price ranges based on market demand indicators.|
|Market Share| Collect market data on the total number of used cars sold in the market or within a specific region. <br/>Determine the number of used cars acquired by the company within the same market or region. <br/>Calculate the company's market share by dividing the number of cars acquired by the total market sales and multiplying by 100 for a percentage value.|
|Customer Satisfaction| Gather feedback from sellers after the transaction, either through surveys or direct communication. <br/>Design a satisfaction rating scale (e.g., 1 to 5) or collect qualitative feedback to assess seller satisfaction. <br/>Calculate the average satisfaction rating or percentage of satisfied sellers based on the collected feedback.|

