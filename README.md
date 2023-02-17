# prefect-capstone
Prefect project to incorperate Bluesky workflows

## Simple Example of Run Engine
To run a simple example, first make a venv, paste the tiled client config in a findable place,
then spin up the docker containers. 

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdir -p ./venv/etc/tiled/profiles
cp docker/tiled_client_config.yml ./venv/etc/tiled/profiles
cd docker
docker-compose up
```

Then all that is left is to run
```bash
python simple_sim.py
```
Which will create a run engine and some kafka topics, subscribe the run engine to tiled insert and kafka publisher, then run a simple plan. 
This will put documents on Kafka to be subscribed to, and `BlueskyRuns` into mongo to be fetched with tiled. 






