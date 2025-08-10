#!/usr/bin/env python3

import sys
import os

print("=== Environment Diagnostics ===")
print(f"Python interpreter: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"JAVA_HOME: {os.environ.get('JAVA_HOME', 'Not set')}")

# Test Java version
import subprocess
try:
    result = subprocess.run(['java', '-version'], capture_output=True, text=True)
    print(f"Java version: {result.stderr.split()[2] if result.stderr else 'Unknown'}")
except:
    print("Java: Not found or error")

print("\n=== PySpark Test ===")
try:
    import pyspark
    print(f"✅ PySpark version: {pyspark.__version__}")
    
    from pyspark.sql import SparkSession
    print("✅ PySpark import successful")
    
    # Create SparkSession with more conservative settings
    spark = (
        SparkSession.builder
        .appName("MAST30034 Jupyter Test")
        .config("spark.sql.repl.eagerEval.enabled", True) 
        .config("spark.sql.parquet.cacheMetadata", "true")
        .config("spark.sql.session.timeZone", "Etc/UTC")
        .config("spark.driver.memory", "2g")  # Limit memory usage
        .config("spark.driver.maxResultSize", "1g")
        .getOrCreate()
    )
    
    print("✅ SparkSession created successfully")
    
    # Test basic operation
    df = spark.range(5)
    df.show()
    print("✅ Basic Spark operations working")
    
    spark.stop()
    print("✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc() 