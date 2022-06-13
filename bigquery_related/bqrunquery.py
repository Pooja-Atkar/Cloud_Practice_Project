import os
from google.cloud import bigquery

if __name__ == '__main__':

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"D:\Google Cloud Data\radiant-saga-351413-457e57ce1bc8.json"

    bqclient = bigquery.Client()

    query = """with data_input as
            (
              select 11 as id,
              ["Music","News"] as category,
              b"ghhhj" as byteval
            )
            select * from `radiant-saga-351413.bwt_practice_learning.student_tb` t inner join data_input t1 on t.stud_id=t1.id;
            """
    query_job = bqclient.query(query)
    for row in query_job:
        print(row)