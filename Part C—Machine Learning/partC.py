from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.regression import LinearRegression
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler


hdfs = "hdfs://andromeda.student.eecs.qmul.ac.uk"
eth_path = hdfs + "/user/mh326/data/eth.csv"

sc = SparkContext()
sql_context = SQLContext(sc)
df = sql_context.read.format('csv') \
                    .options(header='true', inferschema='true') \
                    .load(eth_path)

assembler = VectorAssembler(inputCols=['SplyCur','TxTfrCnt'],
                            outputCol='features')


output = assembler.transform(df)

final_data = output.select('features', 'PriceUSD').filter(df['PriceUSD'].isNotNull())

train_data,test_data = final_data.randomSplit([0.7,0.3])

lr = LinearRegression(labelCol='PriceUSD', maxIter=50,
                      regParam=0.3, elasticNetParam=0.5)

lr_model = lr.fit(train_data)

test_results = lr_model.evaluate(test_data)

print(test_results.rootMeanSquaredError)

print(test_results.r2)

un_data = test_data.select('features')

predictions = lr_model.transform(un_data)

predictions.show()
