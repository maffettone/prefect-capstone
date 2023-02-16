from bluesky.plans import count
from bluesky.run_engine import RunEngine
from ophyd.sim import det1, det2
from tiled.client import from_profile

if __name__ == "__main__":
    RE = RunEngine({})
    cat = from_profile("testing_sandbox")
    dets = [det1, det2]
    RE(count(dets))
    run = cat[-1]
    print(run.primary.data["det2"].read())
