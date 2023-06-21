# Sylndr
# Analysis Report: Estimating Prices for Used Cars

## Introduction
The aim of this analysis report is to provide insights into the process of estimating prices for used cars in the context of Sylndr's business model. As a company specializing in buying used cars from customers, accurately determining the appropriate price for each vehicle is crucial for ensuring fair transactions and maintaining competitive advantage in the market.

Estimating the price of a used car involves considering various factors, such as the car's model, the distance it has traveled (moved kilometers), and the year of its manufacturing. Additionally, competitor prices for similar cars play a significant role in determining the appropriate price to offer our customers. By analyzing these factors and the market dynamics, we can develop a robust pricing strategy that aligns with customer expectations and market trends.

In this analysis, we will leverage a comprehensive dataset that includes information about the car features, competitor prices, and the date at which the competitors added their prices. While the actual true price for used cars is unknown, we will estimate the appropriate price based on the given features and consider the competitor prices as a reference point. It is important to note that not all competitor prices may be logical, and we will carefully analyze and evaluate the data to ensure the reliability of our estimates.

Through this analysis, we aim to gain insights into the key factors influencing used car prices, identify patterns or trends in the market, and develop a data-driven approach for estimating prices that aligns with customer expectations and the competitive landscape. By leveraging the power of data science and statistical techniques, we can enhance our decision-making process and optimize our pricing strategy for buying used cars from customers.

The following sections of this report will delve into the details of the analysis, including data preprocessing, descriptive statistics, correlation analysis, feature importance, time series analysis, competitor price analysis, provide recommendations based on the findings, and suggested key performance indicators for the company.

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

## Data Preprocessing
Before conducting the analysis, several preprocessing steps were performed on the dataset. These steps included handling missing values, filtering outliers based on relevant features, and creating additional features such as car age, price moving average over last n purchases, competitor price differential, car model poplularity, and historical price change.

## Analysis Insights
1- Individual Features Analayis

![numerical_distribution](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/85f4cc1e-1e5a-4797-ae3c-df545fd6d07b)

By analysing the distribution of each of these features [model year, Kilomoters driven, price, count of extra features] by each car, It was identified the following
- There are skewness in {price, model_year, extra_features_count} features, So for price analysis, the price estimated should be between [100K - 600K] EGP.
- The central tendency of extra_features are centered around [6-18], which means most of used cars have number of extra_features ranges from [6 - 18] features.
- The company should focus on used cars with models from years [2014 - 2020], as it was analysised that The central tendency of model_year feature are centered around these years intervals.

2- Car Models Analysis: 
- We determinded the most common car models in the dataset by calculating the frequency of each model.
- This insight provides an understanding of the market's preferences and the popularity of certain car models.
- The most common model in used car is Nissan Sunny, which indicates that it is recommended to invest in this model.
![model_countplot](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/68b12fe7-60e1-44c7-83df-0509b6476bce)
Assumption that, Due to price range difference between models, That affects number of acquisition of certain model rather than other, So Juke Platinium should be the most significantly high price in all the models, so the compnay does not invest in frequently compared to other models.

3- Driven Mileage in Kilomoter analysis:
- Most of the cars we have, have driven around 0-150K.
- It is recommended that Most of sold used cars should be driven for around 0-150K.
![mileage_category_countplot](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/7bfbf4ec-9ff2-4ab3-9565-b08fd418e2a8)

4- Car extra Features analysis: 
- By comparing the most frequent used features in each car, it is recommended that the used car should have atleast these ten feaures ['abs', 'aux', 'airbags', 'powermirrors', 'powerwindows', 'airconditioning', 'powersteering', 'keyless', 'usb', 'ebd'].

5-Common car models with transmission type:
![tranmission_per_model_countplot](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/ba1c0d32-7d77-4d0c-9162-36c2331a8687)
- The car model "Sunny" has a higher number of manual transmission cars compared to other models in the dataset.
- It is important to note that the dataset contains a relatively small number of cars with manual transmission.
- This can potentially introduce some bias when estimating the price of used cars using machine learning or statistical models

6- Model manufacturing years:
- By analysisng the manufacturing year for each used car model. to have better insights which model is most common used in the market over its history.
- Model Sunny, has the highest different model years in our data, which indicates that Sunny has a long history in the market compared to others models.
- In the opposite side, model Juke Platinium has the lowest model years.
![modelyears_plot](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/295ec3d7-e614-48f0-996b-a831df5736eb)

7- Effect of transmission type in car price:
- The analysis reveals a notable price difference between cars with manual and automatic transmission types.
- Cars with manual transmission tend to have lower prices compared to cars with automatic transmission.
- This price difference can be attributed to various factors such as market demand, availability, and perceived value associated with different transmission types.
- Buyers looking for more affordable options may consider cars with manual transmission, while those seeking convenience and ease of use may opt for cars with automatic transmission.
- It is crucial for the company to account for this price disparity when estimating the value of used cars with different transmission types to ensure fair pricing and competitiveness in the market.
![price_distribution_over_transmission_type](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/32915bca-3feb-4fa9-9668-a5790936878a)

8- Price Trend and Pattern over the years:
- Analyzing the price trend and pattern over time for each car reveals interesting observations.
- Car models exhibit a generally increasing price trend over the analyzed time period. This suggests a growing demands in these models. Except for Juke Platinium model, as we don't have enough data in the dataset, so it is not visible to determined its trend.
- The price distribution in all the models suffers from fluctuations over time.
- It is important for the company to closely monitor and analyze the price trends and patterns of different car models to make informed decisions regarding pricing strategies, inventory management, and understanding customer preferences.
- By identifying these trends and patterns, the company can adapt its pricing and marketing strategies accordingly to maximize profitability and stay competitive in the market
![Price_Trend_After_Cleaning](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/9628e474-889f-462f-898a-db8382d57b4b)

9- How does the price vary based on different car features such as car model, manufacturing year, and kilometers driven?
![price_effect_per_Features](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/5283d5d0-319e-4049-89f7-c3ca169c51ac)

To understand Violin plot, there are some aspects to consider:
| Aspect | Description|
|--------|------------|
|Distribution of Data| The width of the violin plot represents the density of data points at different price level. <br/>A wider section indicates a higher concentration of data points, which a narrower section indicates a lower concentration.|
|Median| The white dot within the violin plot represents the median value of the data distribution. <br/>It provides an estimate of the central tendency of the data.|
|Interquartile Range (IQR)| The box inside the violin plot represents the interquartile range, which spans from the 25th precentile (lower quartile) to the 75th precentile (upper quartile) of the data. <br/>It provides information about the spread and variability of the data.|
|Whiskers| The thin lines extending from the box (IQR) represents the data range within a certain threshould of the IQR. <br/>They typically cover a certain percentage of the data, such as 1.5 times the IQR. <br/>Any data points outside the whiskers are considered outliers.|
|Symmetry| The shape of the violin plot can provide insights into the symmetry or skewness of the data distribution. <br/>A symmetric distribution will have similar shapes on both sides of the median, while a skewed distribution will have a longer tail on one side.|

Insights: Using Violin plot tell us the following:
- From distribution of price over car model:
    - The width of each violin indicates the density of prices for a particular price. A narrorw section in the violin plot like in [Juke, Sunny, Qashqia, Sentra], indicates a more dispersed pricing pattern. A wider section in the violin plot like in [Juke Platinium, Tiida] indicate a high concentration of sales within a specific price range.
    - The whitedot in the violin plots indicates the median price value for each car model, which give idea of typical price range. So all models  have similar range of prices, except for "Juke Platinium" has a significantly higher price.
- From distribution of price over car model:
    - The whitedot indicates that, the median price value per each model_year is following a rising trend over each new year.
- From distribution of price over car transmission type:
    - The Price in Manual transmission type used cars is concetrated in a small specific price range, relatively to Automatic transmission type, Which explains the wider & narrow width in the violin plot in both transmission types.

From All these insights, they can guide our pricing strategies, We can determine which car models command higher prices due to their perceived value, understand the range of prices that customers are willing to pay for different models, and identify any outliers in the prices.

## Recommendations
Based on the analysis conducted, the following recommendations are suggested:
- Regularly monitor and update pricing strategies based on the market trends and competitors prices.
- Consider the impact of specific features on pricing decisions.
- Continuously collect and analysis data on competitor prices to maintain a competitive edge.
- Further explore the relationship between pricing and other external factors.
  
### Most important suggested KPIs for the company to target
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

### For calculation of each KPI
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

## Conclution
In conclusion, the analysis of the used car dataset has provided valuable insights into car models, transmission types, price trends, and competitor prices. These insights can assist the company in making informed decisions regarding pricing, inventory management, and understanding customer preferences. It is crucial for the company to leverage these findings to refine its strategies, maximize profitability, and establish a strong foothold in the competitive used car market.