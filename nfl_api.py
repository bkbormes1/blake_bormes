#!/usr/bin/env python
import json
import requests
from kafka import KafkaProducer
from flask import Flask

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    producer.send(topic, json.dumps(event).encode())

@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"

@app.route("/get_game_data")
def get_game_data():
    my_headers = {'Ocp-Apim-Subscription-Key' : 'c1a67aa2c0454422923a280f26415860'}
    game_update = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/ScoresByDate/2021-OCT-31', headers=my_headers)
    log_to_kafka('games', game_update.json())
    return "Game Update!\n"