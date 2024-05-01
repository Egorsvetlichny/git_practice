import requests


def get_random_fact():
    url = 'https://api.api-ninjas.com/v1/facts'
    api_key = 'hwGJJJGeN0g5OtcrrxjHqA==INEiXnDJbMj5rieu'
    response = requests.get(url, headers={'X-Api-Key': api_key})

    if response.status_code == 200:
        return response.json()[0]['fact']
    else:
        raise requests.exceptions.HTTPError(
            f"Error {response.status_code} - {response.json()['message']}")


def get_len_of_fact():
    return len(get_random_fact())


if __name__ == '__main__':
    print(get_random_fact())
    print(get_len_of_fact())
