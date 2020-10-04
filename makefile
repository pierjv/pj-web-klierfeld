SHELL=/bin/sh


source:
	source     ~/envs/Klierfeld/bin/activate
run:
	virtualenv --python python3 \
    	~/envs/Klierfeld	
	pip install -r requirements.txt
	python main.py

gce:
	gcloud app create
	gcloud app deploy app.yaml \
		--project pj-web-klierfeld
gcd:
	gcloud app deploy app.yaml \
		--project pj-web-klierfeld