Big data processing

Implemented a set of Map/Reduce and Spark jobs that process the given input and generates the data for the following:

TIME ANALYSIS:

Created a bar plot showing the number of transactions occurring every month between the start and end of the dataset.

TOP TEN MOST POPULAR SERVICES:

Showing top 10 smart contracts by total Ether received. MRJob based approach.

JOB 1 - INITIAL AGGREGATION:

Shows which services are the most popular. I aggregated all transactions to see how much each address within the user space has been involved in. 

JOB 2 - JOINING TRANSACTIONS/CONTRACTS AND FILTERING:

After obtaining this aggregate of the transactions, I performed a repartition join between this aggregate and contracts. The join was performed at the to_address field from the output of Job 1 with the address field of contracts

Secondly, in the reducer, if the address for a given aggregate from Job 1 was not present within contracts this was filtered out as it is a user address and not a smart contract.

JOB 3 - TOP TEN:

Finally, aggregated filtered addresses and sorted these via a top ten reducer.

PART C. DATA EXPLORATION:

Price Forecasting: Using a dataset online for the price of Ethereum from its inception until now, I utilised a Spark mllib to build a price forecasting model trained on the 
