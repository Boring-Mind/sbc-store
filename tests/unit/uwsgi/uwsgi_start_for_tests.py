def application(environ, start_response):
    response = b'Hello World'
    headers = [('Content-Type', 'text/html')]

    start_response('200 OK', headers)
    return [response]
