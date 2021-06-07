dclear:
	docker stop flask-app && docker container rm flask-app

dbuild:
	cd flask_app &&\
		docker build -t flask-app:latest -f ./flask-service.dockerfile . &&\
		cd ..

run:
	docker run -p 5000:5000 flask-app

ping:
	curl http://127.0.0.1:5000/

run-kube:
	kubectl apply -f jina.yaml

minikube-run:
	minikube start --vm-driver=hyperkit &&\
		eval $(minikube docker-env) &&\
		minikube mount ./:/workdir