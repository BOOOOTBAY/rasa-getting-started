train-nlu:
	rasa train nlu
train:
	rasa train

shell:
	rasa shell

.PYHONY: actions
actions: 
	rasa run actions --port 5056

run:
	rasa run --port 5008 --credentials credentials.yml \
       --cors "*" --debug --endpoints endpoints.yml --enable-api

validate:
	rasa data validate