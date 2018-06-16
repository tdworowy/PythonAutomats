import requests


def test_roobal():
    """Test roobal page."""
    response = requests.get("http://robertmarek.pl")
    while 1:
        print(response)
        if "500" in response:
            break


if __name__ == "__main__":
    test_roobal()
