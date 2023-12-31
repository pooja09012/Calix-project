

Problem Statement:Create an microservice application CRUD app .Which reads from DB responds to API calls ( /api/records, /api/update, etc ). So there will be 4 API calls.


1.Create a Python microservice using Flask to implement the CRUD operations and interact with MongoDB.Use Python file K8-resources/crud-app/app.py.

2.Create a Dockerfile to package your Python application into a container using the dockerfile :K8-resources/dockerfile

3.Build the Docker image and push it to a container registry that your Kubernetes cluster can access.

4.Create a Kubernetes Deployment YAML and service yaml file to deploy your microservice K8-resources/k8-resources/crud_deployment.yaml and K8-resources/k8-resources/crud_deployment.yaml

   kubectl apply -f crud_deployment.yaml
   kubectl apply -f crud_deployment.yaml
 
5.Your microservice is now deployed in Kubernetes and accessible through the Service's IP or hostname and the exposed port (e.g., http://<service-ip>:80/api/records).  

6.Create a MongoDB Deployment , Service YAML and storage class file (K8-resources/k8-resources/mongodb.yaml , K8-resources/k8-resources/mongodb-service.yaml ,K8-resources/k8-resources/mongodb-storageclass.yaml)

  kubectl apply -f mongodb-deployment.yaml
  kubectl apply -f mongodb-service.yaml
  kubectl apply -f mongodb-service.yaml

7.In your Python application code (in app.py), update the MongoDB connection URL to point to the MongoDB service in your cluster:

client = MongoClient("mongodb://mongodb:27017/")  # Use the Kubernetes Service name

-----------------------------------------------------------------------------------------

For Helm Charts installation follow below steps:

1.Create two separate Helm charts, one for the microservice application and another for MongoDB.

   helm create microservice-app
   helm create mongodb
   
2.Edit the values.yaml files in both Helm charts to define the configurable values for your microservice application and MongoDB.

3.To install the Helm charts, first package them:

   helm package microservice-app
   helm package mongodb

4.To install the charts, use the helm install command. Deploy MongoDB first:

      helm install mongodb ./mongodb-<version>.tgz

5.Then deploy the microservice application:

      helm install microservice-app ./microservice-app-<version>.tgz

   











