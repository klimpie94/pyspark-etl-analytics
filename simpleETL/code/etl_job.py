from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, LongType, TimestampType, ShortType, DateType
from os import environ

def main():
    spark = initialize_Spark()

    df_test = loadDFWithoutSchema(spark)

    df_test.show(5)

    df = loadDFWithSchema(spark)

    df.show(2)



def initialize_Spark():

    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("IloveCars") \
        .getOrCreate()

    return spark

def loadDFWithoutSchema(spark):

    df = spark.read.format("csv").option("header", "true").load(environ["HOME"] + "/Downloads/autos.csv")

    return df

def loadDFWithSchema(spark):

    schema = StructType([
        StructField("dateCrawled", TimestampType(), True),
        StructField("name", StringType(), True),
        StructField("seller", StringType(), False),
        StructField("offerType", StringType(), True),
        StructField("price", LongType(), True),
        StructField("abtest", StringType(), True),
        StructField("vehicleType", StringType(), True),
        StructField("yearOfRegistration", StringType(), True),
        StructField("gearbox", StringType(), True),
        StructField("powerPS", ShortType(), True),
        StructField("model", StringType(), True),
        StructField("kilometer", LongType(), True),
        StructField("monthOfRegistration", StringType(), True),
        StructField("fuelType", StringType(), True),
        StructField("brand", StringType(), True),
        StructField("notRepairedDamage", StringType(), True),
        StructField("dateCreated", DateType(), True),
        StructField("nrOfPictures", ShortType(), True),
        StructField("postalCode", StringType(), True),
        StructField("lastSeen", TimestampType(), True)
    ])

    df = spark \
        .read \
        .format("csv") \
        .schema(schema)         \
        .option("header", "true") \
        .load(environ["HOME"] + "/Downloads/autos.csv")

    return df

if __name__ == '__main__':
    main()