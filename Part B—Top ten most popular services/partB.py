import pyspark

def transactions_clean(line):
    try:
        fields = line.split(',')
        if len(fields) != 7:
            return False
        int(fields[3])
        return True
    except:
        pass


def contracts_clean(line):
    try:
        fields = line.split(',')
        if len(fields) != 5:
            return False
        return True
    except:
        pass

sc = pyspark.SparkContext()

transactions = sc.textFile('/data/ethereum/transactions')
contracts = sc.textFile('/data/ethereum/contracts')

transaction_filter = transactions.filter(transactions_clean)
transaction_mapper = transaction_filter.map(lambda n: (str(n.split(',')[2]), long(n.split(',')[3]) ))

contract_filter  = contracts.filter(contracts_clean)
contract_mapper = contract_filter.map(lambda a: (a.split(',')[0],1))

transaction_reducer = transaction_mapper.reduceByKey(lambda a,b: a + b)

join = transaction_reducer.join(contract_mapper).map(lambda a: (a[0], a[1][0]))

top_ten = join.takeOrdered(10,key = lambda a: -a[1])

for top in top_ten:
    print("{}: {}".format(top[0], top[1]))
