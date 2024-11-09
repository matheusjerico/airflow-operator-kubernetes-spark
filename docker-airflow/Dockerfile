# Base Airflow image
FROM apache/airflow:2.9.3

# Install the Kubernetes Python package
RUN pip install kubernetes

# Copy the custom operator and DAG files into the Airflow container
COPY ./custom_operator/ /${AIRFLOW_HOME}/plugins/custom_operator/
COPY ./dag/ /${AIRFLOW_HOME}/dags/