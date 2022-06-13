# First create a dataset on google cloud.
# then create a table on that dataset.
# Create a bucket on the google cloud.
# load or upload your csv or Json file in the bucket.
# then write a following code to load your file data on the table.
# you can used pycharm(python code or SDK command) to load your file data into the table.

import os
from google.cloud import bigquery

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"D:\Google Cloud Data\radiant-saga-351413-457e57ce1bc8.json"

    obj_client = bigquery.Client()

    load_conf = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("fname","STRING"),
            bigquery.SchemaField("lname", "STRING"),
            bigquery.SchemaField("age", "INTEGER"),
            bigquery.SchemaField("dob", "DATE")
        ],
        source_format = bigquery.SourceFormat.CSV,skip_leading_rows = 1
    )

    uri = "gs://bucket_client_pycharm/input_data/emp.csv"

    load_job = obj_client.load_table_from_uri(uri,
                                              "radiant-saga-351413.bwt_session_dataset.emp_data",
                                              location="US",
                                              job_config=load_conf
                                              )

    load_job.result()
    table = obj_client.get_table("radiant-saga-351413.bwt_session_dataset.emp_data")

    print("Loaded:{},no of record loaded:{}".format("bwt_session_dataset.emp_data", table.num_rows))