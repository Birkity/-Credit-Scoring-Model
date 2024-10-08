Credit Scoring System using Transaction Data

This project focuses on building a credit scoring system by analyzing transaction data from various customers. 
The goal is to classify users as high-risk or low-risk based on their transaction behavior. We leverage aggregate 
features derived from the transaction data to build a customer-level profile, identifying patterns that distinguish 
between high and low-risk users. The data includes customer transaction details, such as transaction amounts, dates,
and categories, allowing us to perform a detailed analysis of user behavior.

The project begins with feature engineering, which involves aggregating key transactional features like the total transaction
amount, average transaction amount, and frequency of transactions per customer. We also extract useful date and time components,
such as transaction hour, day, month, and year. These features enable us to explore customer behavior patterns, particularly in terms of how frequently
customers transact and how recently they engaged in transactions. The main aim is to construct a set of robust features that serve as the foundation for risk classification.

To prepare the data for model building, we apply various techniques to handle missing values, encode categorical variables, and scale numerical features. The pipeline includes 
one-hot encoding for categorical features, normalization/standardization for numerical features, and methods to handle missing data. Additionally, we calculate correlations between 
features and perform multicollinearity checks using the Variance Inflation Factor (VIF) to ensure that the data is suitable for model training and prediction.

