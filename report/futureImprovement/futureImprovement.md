# Future Improvement

## Missing values
In this dataset, there are not much physically missing values in each column, that's why we dropped them accordingly.

But there are values that do not make sense, which could considered as missing actually.

Like in price column, Some cars were priced with zero, which can't be true to used car price.

In this case, we could re-label them as Nans, and try to impute their values by any other method, for example: Regression imputing.

## Remove MultiCollinearity
Remove features which has high correlation coefficient between each other.

This will help reduce the redundancy in the data, improve the model interpretability, reduce overfitting, and improve the model generalization capability.

But some consideration should be included before removing the multicollinearity:

- Domain Knowledge: Consider the domain expertise and prior knowledge about the features. Features that are known to have a strong relationship with the target variable may be retained even if they are correlated with other features.

- Impact on Model Performance: Assess the impact of removing correlated features on the model's performance metrics. Removing a correlated feature may or may not improve the model's performance, and it is essential to evaluate the model's performance with and without the correlated features.

- Retaining Important Information: Highly correlated features might still contain unique information that contributes to the target variable prediction. Removing such features may result in loss of valuable information. Therefore, it's crucial to carefully evaluate the trade-off between reducing multicollinearity and retaining important information.
