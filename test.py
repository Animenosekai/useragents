import useragents

def test_random():
    print("[test] --> Testing Random")
    assert isinstance(useragents.random(), str)