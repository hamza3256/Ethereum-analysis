from mrjob.job import MRJob
import time
import re

class partA(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        try:
            if (len(fields) == 7):
                time_epoch = int(fields[6])
                date = time.strftime("%Y-%m",time.gmtime(time_epoch))
                yield (date, 1)
        except:
            pass

    def combiner(self, date, counts):
        yield (date, sum(counts))

    def reducer(self, date, counts):
        yield (date, sum(counts))

if __name__ == '__main__':
    partA.run()
