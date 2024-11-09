from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from kubernetes import client, config
import logging

class SparkKubernetesOperator(BaseOperator):
    """
    Custom Airflow operator to submit a Spark job to Kubernetes
    by creating a SparkApplication manifest using the Kubernetes API.

    Attributes:
        name (str): Name of the SparkApplication resource.
        namespace (str): Kubernetes namespace for the SparkApplication.
        image (str): Docker image to use for the Spark job.
        main_application (str): The main application for the PySpark job.
        arguments (list, optional): List of arguments for the Spark job.
    """

    @apply_defaults
    def __init__(
        self,
        name,
        namespace,
        image,
        main_application,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.name = name
        self.namespace = namespace
        self.image = image
        self.main_application = main_application

    def execute(self, context):
        """
        Executes the Spark job by creating a SparkApplication resource
        on the Kubernetes cluster.

        Args:
            context (dict): Airflow context dictionary.

        Raises:
            Exception: If there's an error in creating the SparkApplication.
        """
        # Load in-cluster Kubernetes configuration
        logging.info("Loading cluster configuration")
        config.load_incluster_config()

        # Define the Kubernetes API client for custom objects
        logging.info("Creating Kubernetes API client")
        api_instance = client.CustomObjectsApi()

        # Define the SparkApplication manifest
        spark_application = {
            "apiVersion": "sparkoperator.k8s.io/v1beta2",
            "kind": "SparkApplication",
            "metadata": {"name": self.name, "namespace": self.namespace},
            "spec": {
                "type": "Python",
                "pythonVersion": "3",
                "mode": "cluster",
                "image": self.image,
                "imagePullPolicy": "Never",
                "mainApplicationFile": self.main_application,
                "sparkVersion": "3.5.3",
                "driver": {
                    "cores": 1,
                    "memory": "512m",
                    "serviceAccount": "spark-operator-spark",
                },
                "executor": {
                    "cores": 1,
                    "instances": 2,
                    "memory": "512m",
                },
            },
        }

        # Submit the SparkApplication resource to Kubernetes
        try:
            api_instance.create_namespaced_custom_object(
                group="sparkoperator.k8s.io",
                version="v1beta2",
                namespace=self.namespace,
                plural="sparkapplications",
                body=spark_application,
            )
            self.log.info(
                "Successfully submitted SparkApplication: %s", self.name
            )
            return True
        except Exception as e:
            self.log.error("Failed to create SparkApplication: %s", str(e))
            raise
