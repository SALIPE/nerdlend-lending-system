## inside each microservice project
name-microservice/
|_ name_app/
||_ views.py
||_ ...
|_ name_microservice/
||_ settings.py
||_ ...
|_ rabbit-mq/
||_ __init__.py
||_ publisher.py
||_ consumer.py

## How to use consumer
from rabbitmq.consumer import Consumer, default_callback

<!-- implement your own callback or use default -->
<!-- tip: use a switch case inside your callback to handle different messages -->

consumer = Consumer("microservice_queue", default_callback)
consumer.start()

## How to use publisher
from rabbitmq.publisher import Publisher

publisher = Publisher()
publisher.send_message("microservice_name", {"Hello": "World"})

## How to config rabbit-mq exchange and queues
https://drive.google.com/file/d/1A1a8tR8_Wuxkp8ZHphe8raKdhJ7FrGHz/view?usp=sharing

## GitHub of minimum Rabbit MQ model
https://github.com/vnszero/rabbitmq-model