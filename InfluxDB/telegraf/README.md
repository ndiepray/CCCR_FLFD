Create Secret
```
kubectl create -f secret.yaml
```
Create Config
```
kubectl create -f config.yaml
```
Create Deployment
```
kubectl create -f depolyment.yaml
```
Telegraf Service Use this if only statsd 8125 port is needed
```
kubectl expose deployment telegraf --port=8125 --target-port=8125 --protocol=UDP --type=NodePort
```
