password=RS6y45UvElmF
gateway=http://localhost:64126

local:
	minikube start
	kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml
	helm repo add openfaas https://openfaas.github.io/faas-netes/
	helm repo update
	helm upgrade openfaas --install openfaas/openfaas --namespace openfaas --set functionNamespace=openfaas-fn --set generateBasicAuth=true

build:
	eval $$(minikube docker-env). 
	./faas-cli.exe build --tag=sha -f examples/python/config.yml

login:
	./faas-cli.exe login --password ${password} --gateway ${gateway} 

deploy: login build
	./faas-cli.exe deploy --tag=sha -f examples/python/config.yml --gateway ${gateway}
	sleep 5s
	kubectl patch deployment -n openfaas-fn hello-python --type=json -p='[{"op":"replace","path":"/spec/template/spec/containers/0/imagePullPolicy","value":"IfNotPresent"}]'
