# Databricks notebook source
from pyspark.sql.functions import sum, col, when

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the Data

# COMMAND ----------

dbutils.fs.mount (
    source = "wasbs://raw-data@crmsalespipelinesc.blob.core.windows.net",
    mount_point = "/mnt/raw-data",
    extra_configs = {
        "fs.azure.account.key.crmsalespipelinesc.blob.core.windows.net": dbutils.secrets.get(scope = "databricksScope", key = "secretkv")
    
    }
)

# COMMAND ----------

dbutils.fs.mount (
    source = "wasbs://transformed-data@crmsalespipelinesc.blob.core.windows.net",
    mount_point = "/mnt/transformed-data",
    extra_configs = {
        "fs.azure.account.key.crmsalespipelinesc.blob.core.windows.net": dbutils.secrets.get(scope = "databricksScope", key = "secretkv")
    
    }
)

# COMMAND ----------

dbutils.fs.ls("/mnt/raw-data")

# COMMAND ----------

dbutils.fs.ls("/mnt/transformed-data")

# COMMAND ----------

accounts_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/raw-data/accounts.csv")
data_dictionary_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/raw-data/data_dictionary.csv")
products_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/raw-data/products.csv")
sales_pipeline_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/raw-data/sales_pipeline.csv")
sales_teams_df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/mnt/raw-data/sales_teams.csv")

# COMMAND ----------

accounts_df.show(2)

# COMMAND ----------

print(accounts_df.columns)
print(data_dictionary_df.columns)
print(products_df.columns)
print(sales_pipeline_df.columns)
print(sales_teams_df.columns)

# COMMAND ----------

# MAGIC %md
# MAGIC ### DataSet Cleaning

# COMMAND ----------

accounts_df = accounts_df.withColumnRenamed("subsidiary_of", "parent_company")
data_dictionary_df = data_dictionary_df.withColumnRenamed("Table", "table").withColumnRenamed("Field", "field").withColumnRenamed("Description", "description")

# COMMAND ----------

accounts_df.show(2)

# COMMAND ----------

data_dictionary_df.show(2)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Null Values 

# COMMAND ----------

null_counts_accounts_df = accounts_df.select([sum(when(col(column).isNull(), 1).otherwise(0)).alias(column) for column in accounts_df.columns])
null_counts_data_dictionary_df = data_dictionary_df.select([sum(when(col(column).isNull(), 1).otherwise(0)).alias(column) for column in data_dictionary_df.columns])
null_counts_products_df = products_df.select([sum(when(col(column).isNull(), 1).otherwise(0)).alias(column) for column in products_df.columns])
null_counts_sales_pipeline_df = sales_pipeline_df.select([sum(when(col(column).isNull(), 1).otherwise(0)).alias(column) for column in sales_pipeline_df.columns])
null_counts_sales_teams_df = sales_teams_df.select([sum(when(col(column).isNull(), 1).otherwise(0)).alias(column) for column in sales_teams_df.columns])

display(null_counts_accounts_df)
display(null_counts_data_dictionary_df)
display(null_counts_products_df)
display(null_counts_sales_pipeline_df)
display(null_counts_sales_teams_df)

# COMMAND ----------

sales_pipeline_df.display()

# COMMAND ----------

accounts_df = accounts_df.fillna({
    "parent_company" : "Independent"
})

sales_pipeline_df = sales_pipeline_df.fillna({
    "account": "Unknown"
})


# COMMAND ----------

null_counts_accounts_df = accounts_df.select([sum(when(col(column).isNull(), 1).otherwise(0)).alias(column) for column in accounts_df.columns])

null_counts_accounts_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Transformed Data

# COMMAND ----------

accounts_df.write.option("header", "true").csv("/mnt/transformed-data/accounts")
data_dictionary_df.write.option("header", "true").csv("/mnt/transformed-data/data_dictionary")
products_df.write.option("header", "true").csv("/mnt/transformed-data/products")
sales_pipeline_df.write.option("header", "true").csv("/mnt/transformed-data/sales_pipeline")
sales_teams_df.write.option("header", "true").csv("/mnt/transformed-data/sales_teams")