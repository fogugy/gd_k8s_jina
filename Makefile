clear-flask:
	docker image rm flask-app

clear-jina:
	docker image rm jina-app

build-flask:
	cd flask_app &&\
	docker build -t flask-app:latest -f ./flask-service.dockerfile . &&\
	cd ..

build-jina:
	cd jina_app &&\
	docker build -t jina-app:latest -f ./jina.dockerfile . &&\
	cd ..

run:
	docker run -p 5000:5000 flask-app

ping:
	curl http://127.0.0.1:5000/

run-kube:
	kubectl apply -f jina.yaml

minikube-run:
	minikube start --vm-driver=hyperkit &&\
	minikube mount ./:/workdir


# 	minikube start --vm-driver=hyperkit &&\
#	minikube start --driver=docker &&\