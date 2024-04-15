from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def get_pairs(df_products, df_categories):
    df_joined = df_products.join(df_categories, df_products["product_id"] == df_categories["product_id"], "left_outer")

    df_result = df_joined.select("product_name", "category_name")

    product_category_pairs = df_result.collect()

    products_without_category = df_joined.filter(col("category_name").isNull()).select(
        "product_name").distinct().collect()

    return product_category_pairs, products_without_category


if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("ProductCategoryPairs") \
        .getOrCreate()

    products_data = [("product1", 1), ("product2", 2), ("product3", None)]
    categories_data = [(1, "category1"), (2, "category2")]

    df_products = spark.createDataFrame(products_data, ["product_name", "product_id"])
    df_categories = spark.createDataFrame(categories_data, ["category_id", "category_name"]).withColumnRenamed(
        "category_id", "product_id")

    pairs, products_without_category = get_pairs(df_products, df_categories)

    print("Пары продукт-категория:")
    for pair in pairs:
        print(pair)

    print("\nПродукты без категорий:")
    for product in products_without_category:
        print(product)

    spark.stop()