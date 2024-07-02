**Run the App:**
1. docker build -t image-name:tag .
2. kubectl apply -f deployments.yaml 
3. kubectl apply -f service.yaml
4. kubectl port-forward deployment/flask-app 5005:500
