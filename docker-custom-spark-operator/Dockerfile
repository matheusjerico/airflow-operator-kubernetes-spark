# Default image from Spark Operator
FROM docker.io/kubeflow/spark-operator:2.0.2

# Set env var
ENV HADOOP_CONF_DIR=/opt/hadoop/conf 

# Switch to ROOT user
USER root

# Download GCS connector JAR
ADD https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar ${SPARK_HOME}/jars/gcs-connector-hadoop3-latest.jar
RUN chmod 644 $SPARK_HOME/jars/gcs-connector-hadoop3-latest.jar

# Remove the older GCS connector JAR
RUN rm -f $SPARK_HOME/jars/gcs-connector-latest-hadoop2.jar

# Add core-site.xml with GCS configuration
COPY /conf/core-site.xml /opt/hadoop/conf/

# Add spark-defaults.conf with GCS configuration
COPY /conf/spark-defaults.conf /opt/spark/conf/spark-defaults.conf

# Add the GCS service account JSON keyfile
COPY /conf/spark-access-sa.json /opt/spark/conf/

# Switch to spark user
USER spark

# Rewrite the entrypoint
ENTRYPOINT ["/usr/bin/entrypoint.sh"]