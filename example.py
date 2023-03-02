import ez_api

# Upload a file
api_key = 'your-api-key-here'
file_path = '/path/to/file.txt'
url = ez_api.upload_file(api_key, file_path)

# Shorten a URL
api_key = 'your-api-key-here'
url = 'https://google.com'
short_url = ez_api.shorten_url(api_key, url)

# Create a text paste
api_key = 'your-api-key-here'
paste_text = 'This is some example paste text.'
paste_language = 'plaintext'
paste_title = 'Example Paste'
paste_description = 'This is an example paste created with the e-z.host API Python wrapper.'
paste = ez_api.create_text_paste(api_key, paste_text, paste_language, paste_title, paste_description)