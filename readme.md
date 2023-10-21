# Used Car Price Estimation: A Data-Driven Approach

![image](https://github.com/AhmedYousriSobhi/used_cars_price_estimation/assets/66730765/5d5100fe-6a7d-4afc-addd-ae7c796060ad)


## Overview

The Car Price Estimation project is a data-driven analysis aimed at accurately estimating the prices of used cars based on various critical factors, including the car's model, mileage, and manufacturing year. This analysis is integral for a company specializing in purchasing used cars, as it ensures equitable transactions and a competitive edge in the market.

## Table of Content
- [Used Car Price Estimation: A Data-Driven Approach](#used-car-price-estimation-a-data-driven-approach)
  - [Overview](#overview)
  - [Table of Content](#table-of-content)
  - [Abstract](#abstract)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
  - [Project Structure](#project-structure)
  - [Data](#data)
    - [Dataset](#dataset)
    - [Analysis](#analysis)
    - [Recommendations](#recommendations)
    - [Concolution](#concolution)
  - [License](#license)

## Abstract

The aim of this analysis report is to provide insights into the process of estimating prices for used cars in the context of Company's business model. As a company specializing in buying used cars from customers, accurately determining the appropriate price for each vehicle is crucial for ensuring fair transactions and maintaining competitive advantage in the market.

Estimating the price of a used car involves considering various factors, such as the car's model, the distance it has traveled (moved kilometers), and the year of its manufacturing. Additionally, competitor prices for similar cars play a significant role in determining the appropriate price to offer our customers. By analyzing these factors and the market dynamics, we can develop a robust pricing strategy that aligns with customer expectations and market trends.

In this analysis, we will leverage a comprehensive dataset that includes information about the car features, competitor prices, and the date at which the competitors added their prices. While the actual true price for used cars is unknown, we will estimate the appropriate price based on the given features and consider the competitor prices as a reference point. It is important to note that not all competitor prices may be logical, and we will carefully analyze and evaluate the data to ensure the reliability of our estimates.

Through this analysis, we aim to gain insights into the key factors influencing used car prices, identify patterns or trends in the market, and develop a data-driven approach for estimating prices that aligns with customer expectations and the competitive landscape. By leveraging the power of data science and statistical techniques, we can enhance our decision-making process and optimize our pricing strategy for buying used cars from customers.

The following sections of this report will delve into the details of the analysis, including data preprocessing, descriptive statistics, correlation analysis, feature importance, time series analysis, competitor price analysis, provide recommendations based on the findings, and suggested key performance indicators for the company.

## Getting Started
### Prerequisites

Before you begin, ensure you have the following prerequisites installed:
- Python (insert version)
- Jupyter Notebook (insert version)
- Required Python libraries (list them)

Installation

Follow these steps to install and set up the project:

1. Clone the repository: git clone https://github.com/AhmedYousriSobhi/used_cars_price_estimation
2. Change directory: cd used_cars_price_estimation
3. Install required libraries: pip install -r requirements.txt
4. (In case of initial setup, create required folders directory using environment script) python ./src/env/setup_env.py

## Project Structure
```bash
.
├── data                   # Dataset files
|   ├── raw
|   ├── intermid
|   ├── output
├── nb_workspace           # Jupiter notebooks
├── docs                   # Documentation files which includes analysis report
├── report                 # Reports files
|   ├── plots              # Figures files
|   ├── reports            # Reports HTML files
├── src                    # Source scripts files
|   ├── env                # Script file to create project directory environment
|   ├── model              # Exported trained models
└── README.md
```
## Data
### Dataset
The analysis utilizes a dataset containing detailed information on used cars, including their model, mileage, manufacturing year, and competitor prices. The dataset can be found data/raw directory.

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

### Analysis
![numerical_distribution](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/85f4cc1e-1e5a-4797-ae3c-df545fd6d07b)

For the insighfull insights for this project could be found inside directory: **docs/analysis_report.pdf**, feel free to take a deep look and think about what to improve and what did I miss.

### Recommendations
Based on the analysis conducted, the following recommendations are suggested:
- Regularly monitor and update pricing strategies based on the market trends and competitors prices.
- Consider the impact of specific features on pricing decisions.
- Continuously collect and analysis data on competitor prices to maintain a competitive edge.
- Further explore the relationship between pricing and other external factors.

### Concolution 
The analysis of the used car dataset has provided valuable insights into car models, transmission types, price trends, and competitor prices. These insights can assist the company in making informed decisions regarding pricing, inventory management, and understanding customer preferences. It is crucial for the company to leverage these findings to refine its strategies, maximize profitability, and establish a strong foothold in the competitive used car market.

## License
This repository is licensed under the MIT License, which means you're free to use the code here for your own learning and projects.

Thank you for visiting my project repository! Feel free to explore the data-driven approach. If you find something helpful or have questions, don't hesitate to reach out.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
