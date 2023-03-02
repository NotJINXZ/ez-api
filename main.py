import requests

# FILE

def upload_file(api_key, file_path, domain=None, randomdomain=False, invisibleurl=False, emojiurl=False, amongusurl=False, customurl=False):
    url = 'https://api.e-z.host/files'
    headers = {'key': api_key}
    data = {'file': open(file_path, 'rb')}
    if domain is not None:
        data['domain'] = domain
    if randomdomain:
        data['randomdomain'] = randomdomain
    if invisibleurl:
        data['invisibleurl'] = invisibleurl
    if emojiurl:
        data['EmojiURL'] = emojiurl
    if amongusurl:
        data['amongusUrl'] = amongusurl
    if customurl:
        data['customurl'] = customurl

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()['url']
    elif response.status_code == 401:
        raise ValueError('Invalid API Key')
    elif response.status_code == 400:
        raise ValueError('Provide a file to upload')
    else:
        raise ValueError(f'Upload failed with status code {response.status_code}')

def delete_file(deletion_key):
    url = f'https://api.e-z.host/files/delete?key={deletion_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return True
    elif response.status_code == 401:
        raise ValueError('Invalid Deletion Key')
    else:
        raise ValueError(f'Deletion failed with status code {response.status_code}')

# LINK SHORTENER

def shorten_url(api_key, url, domain=None, longurl=False):
    url = 'https://api.e-z.host/shortener'
    headers = {'key': api_key}
    data = {'url': url}
    if domain is not None:
        data['domain'] = domain
    if longurl:
        data['longurl'] = longurl

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()['url']
    elif response.status_code == 400:
        if 'IP Logger detected' in response.text:
            raise ValueError('IP Logger detected')
        elif 'Domain "i.e-z.host" can\'t be used for shorteners' in response.text:
            raise ValueError('Domain "i.e-z.host" can\'t be used for shorteners')
        else:
            raise ValueError('Unknown error')
    elif response.status_code == 401:
        raise ValueError('Invalid URL')
    else:
        raise ValueError(f'Shortening failed with status code {response.status_code}')

def delete_shortened_url(api_key, deletion_key):
    url = 'https://api.e-z.host/shortener/delete'
    headers = {'key': api_key}
    params = {'key': deletion_key}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        raise ValueError(f'Deletion failed with status code {response.status_code}')

# PASTES

def create_text_paste(api_key, paste_text, paste_language, paste_title, paste_description, domain=None, random_domain=False, invisible_url=False, emoji_url=False, amongus_url=False, custom_url=False):
    url = 'https://api.e-z.host/paste'
    headers = {'key': api_key}
    data = {
        'text': paste_text,
        'language': paste_language,
        'title': paste_title,
        'description': paste_description,
        'domain': domain,
        'randomdomain': random_domain,
        'invisibleurl': invisible_url,
        'EmojiURL': emoji_url,
        'amongusUrl': amongus_url,
        'customurl': custom_url
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        raise ValueError('Domain "i-.e-z.host" can\'t be used for pastes')
    elif response.status_code == 401:
        raise ValueError('Invalid API key')
    else:
        raise ValueError(f'Paste creation failed with status code {response.status_code}')

def create_file_paste(api_key, file_path, domain=None, random_domain=False, invisible_url=False, emoji_url=False, amongus_url=False, custom_url=False):
    url = 'https://api.e-z.host/paste/file'
    headers = {'key': api_key}
    files = {'file': open(file_path, 'rb')}
    data = {
        'domain': domain,
        'randomdomain': random_domain,
        'invisibleurl': invisible_url,
        'EmojiURL': emoji_url,
        'amongusUrl': amongus_url,
        'customurl': custom_url
    }

    response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        raise ValueError('Domain "i-.e-z.host" can\'t be used for pastes')
    elif response.status_code == 401:
        raise ValueError('Invalid API key')
    else:
        raise ValueError(f'Paste creation failed with status code {response.status_code}')

def edit_paste(api_key, paste_id, new_text):
    url = 'https://api.e-z.host/paste/edit'
    headers = {'key': api_key}
    data = {'id': paste_id, 'text': new_text}

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        raise ValueError('Invalid API key')
    elif response.status_code == 404:
        raise ValueError('Invalid paste ID')
    else:
        raise ValueError(f'Paste edit failed with status code {response.status_code}')

def delete_paste(deletion_key):
    url = 'https://api.e-z.host/paste/delete'
    params = {'key': deletion_key}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return 'Paste successfully deleted'
    elif response.status_code == 404:
        raise ValueError('Invalid deletion key')
    else:
        raise ValueError(f'Paste deletion failed with status code {response.status_code}')