import os
from google.cloud import bigquery

if __name__ == '__main__':

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"D:\Google Cloud Data\radiant-saga-351413-457e57ce1bc8.json"

    obj = bigquery.Client()

    # obj.create_dataset()

    dataset = obj.dataset(dataset_id="bwt_student_dataset",project="radiant-saga-351413")
    print(dataset)
    dataset.location = "US"
    final_op = obj.create_dataset(dataset=dataset)
    print("Successfully created : project_id:{}, dataset:{}".format(obj.project,dataset.dataset_id))