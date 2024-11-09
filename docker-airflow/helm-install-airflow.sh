#!/bin/bash

helm upgrade --install airflow apache-airflow/airflow \
--namespace airflow \
--create-namespace \
--set images.airflow.repository=docker.io/library/custom-airflow \
--set images.airflow.tag=v0.0.3 \
--set images.airflow.pullPolicy=Never 

