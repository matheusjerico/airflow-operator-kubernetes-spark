# Cloud-Native Data Engineering with Apache Spark, Kubernetes, GCS, and Airflow

This repository contains code and resources for setting up an end-to-end data engineering pipeline using **Apache Spark on Kubernetes**, **Google Cloud Storage (GCS)**, and **Apache Airflow**. This setup enables scalable, automated data workflows in a cloud-native environment, suitable for large-scale data processing and orchestration tasks.

This project is based on the article: ["Cloud-Native Data Engineering: Orchestrating Spark on Kubernetes with Airflow and GCS Integration"](https://medium.com/@matheusjerico/advanced-spark-on-kubernetes-integrating-gcs-and-orchestrating-with-airflow-using-custom-airflow-2e8b50710b6a).

Follow the article for a detailed explanation of the setup and how to run the example Spark job. Everything you need to run the example is provided in this article.

---

## Project Structure
```
.
├── docker-airflow
│   ├── custom_operator
│   │   └── spark_k8s_operator.py
│   ├── dag
│   │   └── spark_job_dag.py
│   ├── Dockerfile
│   ├── helm-install-airflow.sh
│   └── rbac
│       ├── cluster-role-binding.yaml
│       └── cluster-role.yaml
├── docker-custom-spark
│   ├── conf
│   │   ├── core-site.xml
│   │   ├── spark-access-sa.json
│   │   └── spark-defaults.conf
│   └── Dockerfile
├── docker-custom-spark-operator
│   ├── conf
│   │   ├── core-site.xml
│   │   ├── spark-access-sa.json
│   │   └── spark-defaults.conf
│   ├── Dockerfile
│   └── helm-install-spark-operator.sh
└── example
    ├── wordcount.py
    └── wordcount-spark.yaml
```

# Cloud-Native Data Engineering with Apache Spark, Kubernetes, GCS, and Airflow

This repository contains code and resources for setting up an end-to-end data engineering pipeline using **Apache Spark on Kubernetes**, **Google Cloud Storage (GCS)**, and **Apache Airflow**. This setup enables scalable, automated data workflows in a cloud-native environment, suitable for large-scale data processing and orchestration tasks.

# LICENSE
MIT License

# AUTHOR
Matheus Jerico  
https://www.linkedin.com/in/matheusjerico/

# ACKNOWLEDGEMENTS
This project is based on the article: ["Cloud-Native Data Engineering: Orchestrating Spark on Kubernetes with Airflow and GCS Integration"](https://medium.com/@matheusjerico/advanced-spark-on-kubernetes-integrating-gcs-and-orchestrating-with-airflow-using-custom-airflow-2e8b50710b6a).
