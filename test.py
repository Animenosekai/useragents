import pyuseragents

def test_random():
    print("[test] --> Testing Random")
    assert isinstance(pyuseragents.random(), str)