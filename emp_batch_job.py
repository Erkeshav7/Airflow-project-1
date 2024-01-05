from pyspark.sql import SparkSession

def process_data():
    spark = SparkSession.builder.appName("GCPDataprocJob").getOrCreate()

    # Define your GCS bucket and paths
    bucket = "landing-zone-gds-noob2"
    emp_data_path = f"gs://{bucket}/employee.csv"
    dept_data_path = f"gs://{bucket}/department.csv"
    output_path = f"gs://{bucket}/joined_output"

    # Read datasets
    employee = spark.read.csv(emp_data_path, header=True, inferSchema=True)
    department = spark.read.csv(dept_data_path, header=True, inferSchema=True)

    # Filter employee data
    filtered_employee = employee.filter(employee.salary > 50000) # Adjust the salary threshold as needed

    # Join datasets
    joined_data = filtered_employee.join(department, "dept_id", "inner")

    # Write output
    joined_data.write.csv(output_path, header=True)

    spark.stop()

if __name__ == "__main__":
    process_data()