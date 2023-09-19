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








