# e-z.host API Python Wrapper

This is a Python wrapper for the e-z.host API, allowing for easy use of the file uploading, link shortening, and pasting services.

## Installation

This library can be installed via pip:

```bash
pip install ez-api
```

## Usage
Here are some examples of how to use the library:

```python
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
```
For more detailed documentation, see the [official e-z.host API documentation.](https://e-z.host/docs/api)

# License
This library is released under the MIT License. See LICENSE for more information.

