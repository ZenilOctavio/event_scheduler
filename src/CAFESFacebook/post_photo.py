import requests

def post_photo(page_id: str, page_token: str, photo_bytes: bytes, message: str):
    url = f'https://graph.facebook.com/{page_id}/photos'
    response = requests.post(url,
                            files={'file': ('image.png', photo_bytes)},
                            data={
                                'access_token': page_token,
                                'message': message
                            })
    return response.json()['id']

def create_post_with_photo(page_id: str, page_token: str, message: str, photo_id: int):
    url = f'https://graph.facebook.com/{page_id}/photos'
    response = requests.post(url,
                         data={'message': message,
                               'attached_media[0]': f'{{"media_fbid":"{photo_id}"}}',
                               'access_token': page_token})
    return response.json()['id']