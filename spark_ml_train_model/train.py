# A simple extension for Jupyter Notebook and Jupyter Lab to beautify Python code automatically using Black.
#%load_ext nb_black
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T

spark = SparkSession.builder.getOrCreate()