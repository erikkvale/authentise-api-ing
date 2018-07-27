def main():
    session = authentise_login(
        username=USERNAME,
        password=PASSWORD
    )

    # model payload/upload on current session
    payload = {
        'auto-align': False,
        'name': 'demo model'
    }
    response = session.post(
        url='https://models.authentise.com/model',
        json=payload
    )
    if _check_response(response):
        # Headers in video seem to be outdated ways of gathering urls,
        # adjusted to get from json() response and 'resources' sub dict
        unpacked_response = response.json()['resources'][0]
        model_url = unpacked_response['uri']
        upload_url = unpacked_response['upload-location']

        with open('./models/vertebra.stl', 'rb') as f:
            response = session.put(
                url=upload_url,
                data=f.read(),
                headers={
                    'Content-Type': 'application/octet-stream'
                }
            )
            if _check_response(response):
                _wait_on_status(
                    session,
                    model_url,
                    ('error', 'processed')
                )