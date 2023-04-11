import requests
import os
from dotenv import load_dotenv


def reload_script():
    """
    For website hosting purposes only.
    Reloads website hosting when new data becomes available.
    """
    load_dotenv()
    username = os.getenv('PA_USERNAME')
    token = os.getenv('PA_TOKEN')
    domain_name = os.getenv('PA_DOMAIN')

    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
            username=username, domain_name=domain_name
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )
    if response.status_code == 200:
        print('reloaded OK')
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

if __name__ == '__main__':
    reload_script()