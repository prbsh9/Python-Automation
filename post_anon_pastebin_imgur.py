def post(url, headers={}, data={}, json={}, as_json=False):
    """
    Make a HTTP post request and return response
    `Required`
    :param str url:       URL of target web page
    `Optional`
    :param dict headers:  HTTP request headers
    :param dict data:     HTTP request POST data
    :param dict json:     POST data in JSON format
    :param bool as_json:  return JSON formatted output
    """
    try:
        import requests
        req = requests.post(url, headers=headers, data=data, json=json)
        output = req.content
        if as_json:
            try:
                output = req.json()
            except: pass
        return output
    except ImportError:
        import sys
        if sys.version_info[0] > 2:
            from urllib.request import urlopen,urlencode,Request
        else:
            from urllib import urlencode
            from urllib2 import urlopen,Request
        data = urlencode(data)
        req  = Request(str(url), data=data)
        for key, value in headers.items():
            req.headers[key] = value
        output = urlopen(req).read()
        if as_json:
            import json
            try:
                output = json.loads(output)
            except: pass
        return output

import time

def normalize(source):
    """
    Normalize data/text/stream
    `Required`
    :param source:   string OR readable-file
    """
    import os
    if os.path.isfile(source):
        return open(source, 'rb').read()
    elif hasattr(source, 'getvalue'):
        return source.getvalue()
    elif hasattr(source, 'read'):
        if hasattr(source, 'seek'):
            source.seek(0)
        return source.read()
    else:
        return bytes(source)

def pastebin(source, api_key):
    """
    Upload file/data to Pastebin
    `Required`
    :param str source:         data or readable file-like object
    :param str api_dev_key:    Pastebin api_dev_key
    `Optional`
    :param str api_user_key:   Pastebin api_user_key
    """
    import sys
    if sys.version_info[0] > 2:
        from urllib.parse import urlsplit,urlunsplit
    else:
        from urllib2 import urlparse
        urlsplit = urlparse.urlsplit
        urlunsplit = urlparse.urlunsplit
    if isinstance(api_key, str):
        try:
            info = {'api_option': 'paste', 'api_paste_code': normalize(source), 'api_dev_key': api_key}
            paste = post('https://pastebin.com/api/api_post.php', data=info)
            print(paste)
            parts = urlsplit(paste)
            return parts
        except Exception as e:
            print("Upload to Pastebin failed with error: {}".format(e))
    else:
        print("No Pastebin API key found")
