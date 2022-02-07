# Client clustering
### Introduction
Hello everyone, this is a small client clustering project. KMeans was used as the clustering algorithm. The result of the work was the division of clients into 4 main groups. These groups have their own preferences in the company's products and places of purchase. More details below.
##### The project consists of three files:

  - marketing_campaign.csv - Dataset;
  - Marketing campaign.ipynb - The main notebook that contains all the clustering steps;
  - sup_defs.py - A file with auxiliary functions for plotting (I think it is better to keep a large amount of monotonous code in a separate file).

### What we have?
Dataset from Kaggle: Customer Personality Analysis (https://www.kaggle.com/imakash3011/customer-personality-analysis)
##### Problem Statement
Customer Personality Analysis is a detailed analysis of a company’s ideal customers. It helps a business to better understand its customers and makes it easier for them to modify products according to the specific needs, behaviors and concerns of different types of customers.

Customer personality analysis helps a business to modify its product based on its target customers from different types of customer segments. For example, instead of spending money to market a new product to every customer in the company’s database, a company can analyze which customer segment is most likely to buy the product and then market the product only on that particular segment.

<details>
  <summary>Attributes</summary>
  
  ##### People

- ID: Customer's unique identifier
- Year_Birth: Customer's birth year
- Education: Customer's education level
- Marital_Status: Customer's marital status
- Income: Customer's yearly household income
- Kidhome: Number of children in customer's household
- Teenhome: Number of teenagers in customer's household
- Dt_Customer: Date of customer's enrollment with the company
- Recency: Number of days since customer's last purchase
- Complain: 1 if the customer complained in the last 2 years, 0 otherwise

##### Products

- MntWines: Amount spent on wine in last 2 years
- MntFruits: Amount spent on fruits in last 2 years
- MntMeatProducts: Amount spent on meat in last 2 years
- MntFishProducts: Amount spent on fish in last 2 years
- MntSweetProducts: Amount spent on sweets in last 2 years
- MntGoldProds: Amount spent on gold in last 2 years

##### Promotion

- NumDealsPurchases: Number of purchases made with a discount
- AcceptedCmp1: 1 if customer accepted the offer in the 1st campaign, 0 otherwise
- AcceptedCmp2: 1 if customer accepted the offer in the 2nd campaign, 0 otherwise
- AcceptedCmp3: 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
- AcceptedCmp4: 1 if customer accepted the offer in the 4th campaign, 0 otherwise
- AcceptedCmp5: 1 if customer accepted the offer in the 5th campaign, 0 otherwise
- Response: 1 if customer accepted the offer in the last campaign, 0 otherwise

##### Place

- NumWebPurchases: Number of purchases made through the company’s website
- NumCatalogPurchases: Number of purchases made using a catalogue
- NumStorePurchases: Number of purchases made directly in stores
- NumWebVisitsMonth: Number of visits to company’s website in the last month
</details>

### Clustering algorithm
- First, I checked the data for gaps. In this case, the dataset had 24 gaps in the income line, it was easiest to remove them, since this will have little effect on the result.
- Having information about the birthday, you can calculate the age of the client (in general, this column is only relatively useful, we do not know at what point in time the dataframe was created).
- The number of days during which the client uses the services of the company is also calculated.
- Good indicators will also be the number of goods purchased and the amount that was spent on them. These indicators will allow you to calculate the average price of the product and reduce the number of columns.
- StandardScaler will be used for data processing, so the 'Marital_Status' and 'Education' columns have been simplified and numeric.
- Abnormal values were found and removed using the plot-matrix.
- The correlation matrix allows to track indicators that affect each other, there a lot of them, so need to apply the dimensionality reduction algorithm (PCA).
- Transform data with StandardScaler().
- Let's transform the data using PCA. 80% of the dataset information will be enough.
- Using the Elbow Method, we determine the recommended number of clusters. It turns out 4 groups of clients.
- Using KMeans(), we divide clients into 4 groups.
### Client groups
##### Group 1
- Average income: 42527.09.
- Family size: 3-4 persons.
- Preferred shopping place: Website and store.
- Average spent: 127.89
- Average number of items purchased: 6.8
- Participation in campaigns: Weak
- 
