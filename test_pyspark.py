#!/usr/bin/env python3

import sys
print(f"Python interpreter: {sys.executable}")

try:
    from pyspark.sql import SparkSession
    print("✅ PySpark import successful")
    
    # Create SparkSession
    spark = (
        SparkSession.builder
        .appName("MAST30034 Test")
        .config("spark.sql.repl.eagerEval.enabled", True) 
        .config("spark.sql.parquet.cacheMetadata", "true")
        .config("spark.sql.session.timeZone", "Etc/UTC")
        .getOrCreate()
    )
    
    print("✅ SparkSession created successfully")
    
    # Test basic operation
    df = spark.range(10)
    count = df.count()
    print(f"✅ Basic Spark operation successful - count: {count}")
    
    spark.stop()
    print("✅ All tests passed! PySpark is working correctly.")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc() 