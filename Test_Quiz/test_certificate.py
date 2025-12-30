from certificate import generate_certificate as c

def test_certificate():

    assert c("Ali", 10, 5) is False

    assert c("mmad", 70, 7) is True

    assert c("", 10, 5) is False

