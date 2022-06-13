import os
from google.cloud import bigquery

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"D:\Google Cloud Data\radiant-saga-351413-457e57ce1bc8.json"

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"

load_conf = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("dept_id", "INTEGER"),
        bigquery.SchemaField("dept_name", "STRING"),
        bigquery.SchemaField("department_date","DATE"),
    ],

    # time_partitioning = bigquery.TimePartitioning(
    #     type_=bigquery.TimePartitioningType.YEAR,
    #     field="department_date")

    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows = 1
)
uri = "gs://bwt_practice_learning/input_data/department.csv"

load_job = client.load_table_from_uri(uri,
                                      "radiant-saga-351413.bwt_practice_learning.department",
                                      location="US",
                                      job_config=load_conf,
                                      job_id_prefix="loadcsv")
    #uri, "bwt_session_dataset.chkmate", job_config=job_config
  # Make an API request.

load_job.result()  # Waits for the job to complete.

table = client.get_table("bwt_practice_learning.department")  # Make an API request.
print("Loaded:{},no of record loaded:{}".format("bwt_practice_learning.department",table.num_rows))