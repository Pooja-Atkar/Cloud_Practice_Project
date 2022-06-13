import os
from google.cloud import bigquery

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"D:\Google Cloud Data\radiant-saga-351413-457e57ce1bc8.json"

    obj_client = bigquery.Client()

    schema = [
        bigquery.SchemaField(name="dept_id",field_type="INTEGER"),
        bigquery.SchemaField("dept_name","string"),
        bigquery.SchemaField("address","RECORD",mode="REPEATED",
                             fields=[
                                 bigquery.SchemaField("city", "string"),
                                 bigquery.SchemaField("state", "string")

                             ])
    ]
    table = bigquery.Table("radiant-saga-351413.bwt_practice_learning.dept_tb",schema)
    print("table object created :{}".format(table))

    table.clustering_fields = ["dept_id"]

    table = obj_client.create_table(table)
    print("successfully created table:{}".format(table.table_id))
