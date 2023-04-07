import requests

username = 'martinvv'
token = '755e1ff9b98bac35c7094e8d0ad47bbfcb674e85'
domain_name = 'martinvv.pythonanywhere.com'

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