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
	cd examples/python && ../../faas-cli.exe build --tag=sha -f config.yml

login:
	./faas-cli.exe login --password ${password} --gateway ${gateway} 

deploy: login build
	cd examples/python && ../../faas-cli.exe deploy --tag=sha -f config.yml --gateway ${gateway}
	sleep 5s
	kubectl patch deployment -n openfaas-fn hello-python --type=json -p='[{"op":"replace","path":"/spec/template/spec/containers/0/imagePullPolicy","value":"IfNotPresent"}]'

reset:
	rm -Rf examples/python/build
