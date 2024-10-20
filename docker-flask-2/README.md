

# 快速开始
```bash
ansible-galaxy install -r requirements.yml
ansible-playbook -i inventory.yml provisioning/main.yml
```


# 启动&构建整个架构
```bash
docker compose up --build
docker compose build
```

# K3s
```bash
export KUBECONFIG=$(pwd)/config.yaml

cd /home/cxh/ansible-for-devops/docker-flask-2/my-k3s-app/
kubectl apply -f nginx-configmap.yml
kubectl apply -f redis-deployment.yml
kubectl apply -f redis-service.yml
kubectl apply -f webapp-deployment.yml
kubectl apply -f webapp-service.yml
kubectl apply -f nginx-deployment.yml
kubectl apply -f nginx-service.yml

kubectl get pods

kubectl port-forward svc/nginx 8080:80
```


# Test(local)
```bash
kubectl port-forward svc/nginx 8080:8080

curl http://119.28.140.139:8080
```


