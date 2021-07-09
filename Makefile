train-nlu:
	rasa train nlu
train:
	rasa train

shell:
	rasa shell

actions: 
	rasa run actions

run:
	rasa run --port 5003 --credentials credentials.yml \
       --cors "*" --debug --endpoints endpoints.yml --enable-api
