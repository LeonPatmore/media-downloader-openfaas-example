password=RS6y45UvElmF
gateway=http://localhost:64126

include .env

generate-secrets-yml:
	echo ${AWS_ACCESS_KEY_ID}
	echo ${AWS_SECRET_ACCESS_KEY}
	export AWS_ACCESS_KEY_ID_ENCODED=`echo -n ${AWS_ACCESS_KEY_ID} | base64` && \
	export AWS_SECRET_ACCESS_KEY_ENCODED=`echo -n ${AWS_SECRET_ACCESS_KEY} | base64` && \
	cat examples/secrets-template.yml | envsubst > examples/secrets.yml

local: generate-secrets-yml
	minikube start
	kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml
	helm repo add openfaas https://openfaas.github.io/faas-netes/
	helm repo update
	helm upgrade openfaas --install openfaas/openfaas --namespace openfaas --set functionNamespace=openfaas-fn --set generateBasicAuth=true --set image_pull_policy=IfNotPresent
	kubectl apply -f examples/secrets.yml

pre-build:
	cd examples/python && ../../faas-cli template pull https://github.com/openfaas-incubator/python-flask-template
	cd examples/python && ../../faas-cli template store pull python3-http
	eval $$(minikube docker-env).

build-local: pre-build
	cd examples/python && rm -f config-local.yml
	cd examples/python && cp config.yml config-local.yml
	cd examples/python && sed -i '9s/hello-python/hello-python:$(tag)/g' config-local.yml
	cd examples/python && ../../faas-cli.exe build -f config-local.yml
	minikube image load hello-python:$(tag)

build: pre-build
	cd examples/python && ../../faas-cli.exe build --tag=sha -f config.yml
	minikube image load hello-python:latest-`git rev-parse --short HEAD`

login:
	./faas-cli.exe login --password ${password} --gateway ${gateway} 

deploy: login build
	cd examples/python && ../../faas-cli.exe deploy --tag=sha -f config.yml --gateway ${gateway}

deploy-local: login build-local 
	cd examples/python && ../../faas-cli.exe deploy -f config-local.yml --gateway ${gateway}

reset:
	rm -Rf examples/python/build

test:
	cd examples/python && pipenv install --dev
	cd examples/python && pipenv run python -m pytest handler_test.py
