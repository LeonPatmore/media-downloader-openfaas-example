include .env

generate-secrets-yml:
	echo ${AWS_ACCESS_KEY_ID}
	echo ${AWS_SECRET_ACCESS_KEY}
	export AWS_ACCESS_KEY_ID_ENCODED=`echo -n ${AWS_ACCESS_KEY_ID} | base64` && \
	export AWS_SECRET_ACCESS_KEY_ENCODED=`echo -n ${AWS_SECRET_ACCESS_KEY} | base64` && \
	cat secrets-template.yml | envsubst > secrets.yml

local: generate-secrets-yml
	minikube start
	kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml
	helm repo add openfaas https://openfaas.github.io/faas-netes/
	helm repo update
	helm upgrade openfaas --install openfaas/openfaas --namespace openfaas --set functionNamespace=openfaas-fn --set generateBasicAuth=true --set image_pull_policy=IfNotPresent
	kubectl apply -f secrets.yml

pre-build:
	cd function && ../faas-cli template pull https://github.com/openfaas-incubator/python-flask-template
	cd function && ../faas-cli template store pull python3-http
	eval $$(minikube docker-env).

build-local: pre-build
	cd function && rm -f config-local.yml
	cd function && cp config.yml config-local.yml
	cd function && sed -i '9s/hello-python/hello-python:$(tag)/g' config-local.yml
	cd function && ../faas-cli.exe build -f config-local.yml
	minikube image load hello-python:$(tag)

build: pre-build
	cd function && ../faas-cli.exe build --tag=sha -f config.yml
	minikube image load hello-python:latest-`git rev-parse --short HEAD`

login:
	./faas-cli.exe login --password ${OPENFAAS_PASSWORD} --gateway ${OPENFAAS_GATEWAY} 

deploy: login build
	cd function && ../faas-cli.exe deploy --tag=sha -f config.yml --gateway ${OPENFAAS_GATEWAY}

deploy-local: login build-local 
	cd function && ../faas-cli.exe deploy -f config-local.yml --gateway ${OPENFAAS_GATEWAY}

reset:
	rm -Rf function/build

test:
	cd function && pipenv install --dev
	cd function && pipenv run python -m pytest handler_test.py
