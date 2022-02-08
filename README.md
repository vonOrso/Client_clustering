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
- Average income: 42527.09;
- Family size: 3-4 persons;
- Preferred shopping place: Website and store;
- Average spent: 127.89;
- Average number of items purchased: 6.8;
- Participation in campaigns: Low;
- Note: The company does not provide the goods necessary for this group, it consists of families with children, and the main product of the company is wine. This group is not the target audience and can only be attracted by expanding the range of products, which can only be considered in the very long term.
##### Group 2
- Average income: 76820.05;
- Family size: 1-2 persons;
- Preferred shopping place: Website, catalog and store;
- Average spent: 1407.60;
- Average number of items purchased: 19.37;
- Participation in campaigns: High, use of discounts is very low;
- Note: This group is the main clients of the company and the main target of promotional campaigns. This group rarely visits the website, it may be worth considering new approaches to keeping the audience on the site (simplification of functionality, updating recommender systems, etc.).
##### Group 3
- Average income: 30069.88;
- Family size: 2-3 persons;
- Preferred shopping place: Website and store;
- Average spent: 	101.85;
- Average number of items purchased: 5.9;
- Participation in campaigns: Low;
- Note: This is the youngest group, over time, clients from this group will flow into groups 1 and 4.
##### Group 4
- Average income: 59994.39;
- Family size: 2-3 persons;
- Preferred shopping place: Website and store;
- Average spent: 	831.56;
- Average number of items purchased: 18.35;
- Participation in campaigns: moderate, high interest in discounts;
- Note:This audience is very similar to group 2, but buys cheaper goods and has one child in the family. Often participates in promotional campaigns and has an interest in discounted products.
### Visualizations
The algorithm split the data into 4 almost identical clusters. Now we need to evaluate our groups.
![download](https://user-images.githubusercontent.com/43719238/152992430-8f79c3a1-67c5-4d78-9211-a36402404623.png)

The dependence of money spent in the store on income clearly shows the division of customers into clusters. The graph shows the usual relationship between these indicators, but group 1 is of some interest. The income of this group is higher than that of group 3, but the average amount of purchased goods is approximately equal. This group should be given more attention, most likely the company does not provide the goods necessary for this group or promotional companies do not take this group into account.
![download](https://user-images.githubusercontent.com/43719238/152992646-1caf8cc0-ce8d-4705-9382-d9b403e902e7.png)

The dependence of the number of purchases on their price indicates the difference between groups 2 and 4. Group 2 buys more expensive goods.
![download](https://user-images.githubusercontent.com/43719238/152992737-6ae00b33-7dda-4224-bfd5-785a15ff881a.png)
![download](https://user-images.githubusercontent.com/43719238/152992773-41415dac-2c8b-4769-94be-a2e9b546e566.png)

Returning to group 1, we can assume that the company provides few products for families with children, so you can consider options for expanding the range to attract this group.
![download](https://user-images.githubusercontent.com/43719238/152993093-8ff04673-0faa-4590-a147-8b5eea00f8a9.png)

The most traded commodity is wine. The distribution of clusters for all products is approximately the same, but you can pay attention to meat products. The main consumer of these products is the group with the highest income. Most likely, the price of meat products is higher than in other stores.
![download](https://user-images.githubusercontent.com/43719238/152993127-8cab7653-ba4e-44b0-8585-fb13d72f2001.png)

The group with the highest income (Group 2) shows the greatest interest in campaigns. Most likely, these campaigns are created with an eye on these customers.
![download](https://user-images.githubusercontent.com/43719238/152993188-0109f6a0-3056-4c7f-9e9e-591ee6f99c3d.png)

I think we can conclude that the last campaign was the most successful and attracted a record number of customers. It seems to me that campaigns should focus not only on group 2, but also on group 4. This group is distinguished by lower income, having one child in the family and interest in discounts, but it is just as loyal as group 2.
![download](https://user-images.githubusercontent.com/43719238/152993226-80022fc6-2ea0-4342-b264-1d7b14026670.png)

### Conclusions
The KMeans algorithm did a good job and divided the clients into groups. Each group has its own characteristics (private increase from its income) and preference when buying the company's products. These client groups can also be divided into subgroups by age, number of children, and included for a detailed study of clients.
