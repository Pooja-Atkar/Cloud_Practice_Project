import os
from google.cloud import bigquery

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"D:\Google Cloud Data\radiant-saga-351413-457e57ce1bc8.json"

    obj_client = bigquery.Client()

    schema = [
        bigquery.SchemaField(name="stud_id",field_type="INTEGER"),
        bigquery.SchemaField("stud_name","string"),
        bigquery.SchemaField(name="gender", field_type="string"),
        bigquery.SchemaField(name="admission_date", field_type="DATE")
    ]
    table = bigquery.Table("radiant-saga-351413.bwt_practice_learning.student_tb",schema)
    print("table object created :{}".format(table))
    table.time_partitioning = bigquery.TimePartitioning(field="admission_date")

    table = obj_client.create_table(table)
    print("successfully created table:{}".format(table.table_id))
