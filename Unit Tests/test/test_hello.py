from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Adnan") == "hello, Adnan"

# in the terminal type:
# > pytest test <- folder name
# to test the whole folder, an empty file have to create
# __init__.py