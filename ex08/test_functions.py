x = 0

def test():
    assert x

def setup():
    global x
    x = 1

def teardown():
    global x
    x = 1

test.setup = setup
test.teardown = teardown
