# Rasa Getting Started 

## Feature

* Out of Box Chatroom integrated with Rasa
* Chinese Rasa Pipeline to build Chatbot
* ...

BotBay 刚刚出生，需要大家的共同努力才能够快速成长 ~~

## Quick Start

* clone the repo

```shell
git clone https://github.com/BOOOOTBAY/rasa-getting-started
```

* install dependency packages

```shell
pip install -r requirements.txt
```

* trian

```shell
rasa train

# or 

make train
```

* run the bot & ChatRoom

```shell
rasa run --port 5003 --credentials credentials.yml \
  --cors "*" --debug --endpoints endpoints.yml --enable-api

# or

make run
```

## Copyright & License

- Code & Docs © 2021 BOOOOTBAY <https://github.com/BOOOOTBAY>
- Code released under the Apache-2.0 License
- Docs released under Creative Commons
