from airflow import DAG
from airflow.utils.dates import days_ago
from custom_operator.spark_k8s_operator import SparkKubernetesOperator

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}

# Define the DAG
dag = DAG(
    "spark_job_dag",
    default_args=default_args,
    description="DAG to submit Spark jobs to Kubernetes using a custom operator",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
)

# Define the Spark job task
spark_task = SparkKubernetesOperator(
    task_id="run_spark_job",
    name="example-spark-job",
    namespace="default",
    image="docker.io/library/custom-spark:v0.0.1",
    main_application="gs://matheusjerico-spark-scripts/wordcount.py",
    dag=dag,
)
