local:
	minikube start
	kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml
	helm repo add openfaas https://openfaas.github.io/faas-netes/
	helm repo update
	helm upgrade openfaas --install openfaas/openfaas --namespace openfaas --set functionNamespace=openfaas-fn --set generateBasicAuth=true

build:
	./faas-cli.exe build -f examples/python/config.yml 
