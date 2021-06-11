build-flask:
	cd flask_app &&\
	docker build -t flask-app:latest -f ./flask-service.dockerfile . &&\
	cd ..

build-jina:
	cd jina_app &&\
	docker build -t jina-app:latest -f ./jina.dockerfile . &&\
	cd ..

run-kube:
	kubectl apply -f deployment.yaml

minikube-run:
	minikube start --vm-driver=hyperkit &&\
	minikube mount ./:/workdir

