from numb3rs import  validate

def test_number1():
    assert validate("22.12.3.4")==True
    assert validate("1234.3.45.6")==False
    assert validate("3.275.4.50")==False
    assert validate("23.45.232.1")==True
    assert validate("23.4.53.453")==False

def test_number2():
    assert validate("hello.hi.32.5")==False
    assert validate("hello 3.4.5.6 is IPv4")==False
    assert validate("2.3.4.5.6")==False
    assert validate("12.3.")==False
    