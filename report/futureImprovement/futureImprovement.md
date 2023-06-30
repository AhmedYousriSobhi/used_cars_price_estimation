# Future Improvement

## Missing values
In this dataset, there are not much physically missing values in each column, that's why we dropped them accordingly.

But there are values that do not make sense, which could considered as missing actually.

Like in price column, Some cars were priced with zero, which can't be true to used car price.

In this case, we could re-label them as Nans, and try to impute their values by any other method, for example: Regression imputing.