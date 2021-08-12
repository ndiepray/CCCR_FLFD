Create Grafana Secret
```
kubectl create secret generic grafana-creds \
--from-literal=GF_SECURITY_ADMIN_USER=admin \
--from-literal=GF_SECURITY_ADMIN_PASSWORD=admin1234
```
Create Grafana Deployment
```
kubectl create -f deployment.yaml
```
Expose Deployment
```
kubectl expose deployment grafana --type=LoadBalancer --port=3000 --target-port=3000 --protocol=TCP
```
