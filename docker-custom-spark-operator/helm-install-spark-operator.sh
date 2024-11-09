#!/bin/bash

helm install spark-operator spark-operator/spark-operator \
--namespace spark-operator \
--create-namespace \
--set image.registry=docker.io \
--set image.repository=library/custom-spark-operator \
--set image.tag=v0.0.1 \
--set image.pullPolicy=Never