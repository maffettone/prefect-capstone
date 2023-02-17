from bluesky.plans import count
from bluesky.run_engine import RunEngine
from bluesky_kafka import Publisher
from bluesky_kafka.utils import create_topics, delete_topics
from ophyd.sim import det1, det2
from tiled.client import from_profile

bootstrap_servers = "127.0.0.1:9092"
broker_config = {
    "acks": 1,
    "enable.idempotence": False,
    "request.timeout.ms": 1000,
    "bootstrap.servers": "127.0.0.1:9092",
}


if __name__ == "__main__":
    RE = RunEngine({})
    cat = from_profile("testing_sandbox")
    create_topics(topics_to_create=["bluesky.documents"], bootstrap_servers=bootstrap_servers)
    publisher = Publisher(
        topic="bluesky.documents", bootstrap_servers=bootstrap_servers, producer_config=broker_config, key="key"
    )
    RE.subscribe(publisher)

    dets = [det1, det2]
    RE(count(dets))
    run = cat[-1]
    print(run.primary.data["det2"].read())

    delete_topics(
        bootstrap_servers=bootstrap_servers,
        topics_to_delete=[
            "bluesky.documents",
        ],
    )
