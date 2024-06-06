import pyuseragents

def test_random():
    print("[test] --> Testing Random")
    for _ in range(1000):
        current = pyuseragents.random()
        assert isinstance(current, str)
        assert isinstance(current.strip().replace(" ", "") != "")
