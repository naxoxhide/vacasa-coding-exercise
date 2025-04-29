import requests

BASE_URL = "http://127.0.0.1:5000/"

def test_addition():
    r = requests.get(BASE_URL, params={'q': '1+1'})
    assert r.text == '2'
    print("Test addition OK")

def test_count_words_letters():
    r = requests.get(BASE_URL, params={'q': 'count hello world'})
    assert r.text == '2 8 3'
    print("Test count words/letters OK")

def test_bonus1_case1():
    query = "< 53 50 17 55 58 54 50 57 38 31 >"
    expected = "75 85 103 105 95"
    r = requests.get(BASE_URL, params={'q': query})
    assert r.text == expected
    print("Test Bonus1 Case 1 OK")

def test_bonus1_case2():
    query = "< 11 17 58 32 36 39 40 14 11 35 >"
    expected = "69 51 53 67 53"
    r = requests.get(BASE_URL, params={'q': query})
    assert r.text == expected
    print("Test Bonus1 Case 2 OK")

if __name__ == "__main__":
    test_addition()
    test_count_words_letters()
    test_bonus1_case1()
    test_bonus1_case2()
    print("All tests passed!")
