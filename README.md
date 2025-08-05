# 2-Tier Application with Network Restrictions on Kubernetes

This repository contains a basic 2-tier application (frontend and backend) running on Kubernetes. The frontend service interacts with the backend service. The project includes Kubernetes configuration files for deploying the services and applying network policies to restrict access between pods.

## Prerequisites

Before setting up the project, ensure the following tools are installed on your machine:

- **EC2**: Launch t2.large Ubuntu 22.04 instance
- **Minikube**: For running the local Kubernetes cluster.
- **kubectl**: Command-line tool for interacting with Kubernetes.
- **Docker**: For building and running the container images.
- **Other Depedencies**: curl wget apt-transport-https ca-certificates git socat conntrack
 
### Install Minikube
If you don't have Minikube installed, follow the [official installation guide](https://minikube.sigs.k8s.io/docs/).

### Install kubectl
Follow the instructions to install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

### Install Docker
Ensure Docker is installed and running. Follow the installation guide [here](https://docs.docker.com/get-docker/).

## Setup Instructions

### 1. Start Minikube
Start a Minikube cluster with the necessary configuration:

minikube start --driver=docker --kubernetes-version=stable

### 2. Build Docker Images
Build the Docker images for the frontend and backend services.

Backend Image:

Navigate to the backend folder and build the image:

docker build -t backend .

Frontend Image:

Navigate to the frontend folder and build the image:

docker build -t frontend .

### 3. Push Docker Images to Docker Hub

If you want to push the images to Docker Hub, log in to your Docker account and push the images:

docker login  
docker tag backend your-dockerhub-username/backend  
docker tag frontend your-dockerhub-username/frontend  

docker push your-dockerhub-username/backend  
docker push your-dockerhub-username/frontend  

### 4. Apply Kubernetes Manifests

Apply the Kubernetes configuration files to deploy the backend and frontend services along with a network policy to restrict access.

kubectl apply -f backend-deployment.yaml  
kubectl apply -f frontend-deployment.yaml  
kubectl apply -f backend-service.yaml  
kubectl apply -f frontend-service.yaml  
kubectl apply -f network-policy.yaml  

### 5. Verify the Deployment
Check the status of the pods and services:
 
kubectl get pods  
kubectl get svc  
Make sure the services are running, and the network policy has been applied correctly.  

### 6. Access the Frontend
To access the frontend service, use the Minikube service command:  
 
minikube service frontend-service --url

This will open the frontend application in your browser.  

Network Policy: The network policy applied ensures that the frontend can only communicate with the backend service and no other services within the Kubernetes cluster.  
The frontend can access the backend service on port 5000. No external access is allowed to the backend from other services or pods in the cluster.

### 7. Test Communication
You can test if the network policy is applied correctly by attempting to access the backend service from the frontend pod:  
 
kubectl exec -it <frontend-pod-name> -- curl http://backend-service:5000  

If the network policy is applied correctly, access should be allowed from the frontend to the backend but restricted from other sources.  

### 8. Cleanup
To delete the resources and stop Minikube:

kubectl delete -f backend-deployment.yaml
kubectl delete -f frontend-deployment.yaml
kubectl delete -f backend-service.yaml
kubectl delete -f frontend-service.yaml
kubectl delete -f network-policy.yaml

minikube stop
