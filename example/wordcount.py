# wordcount.py

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Sample data for counting words
data = ["Hello world", "Hello Kubernetes", "Hello Spark on GCS"]

# Create an RDD and perform the word count
rdd = spark.sparkContext.parallelize(data)
counts = rdd.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b)

# Show the result
counts.collect()
for (word, count) in counts.collect():
    print(f"{word}: {count}")

spark.stop()