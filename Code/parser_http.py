import sys

def parse_request(request_data):
    try:
        lines = request_data.splitlines()

        method, path, version = lines[0].split(' ')

        #If the methods are not as stated as in guidelines, I choose 'HEAD' and 'CONNECT' as the additional methods
        if method not in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'CONNECT']:
            return 400,

        #If the versions are not valid
        if version not in ['HTTP/1.0', 'HTTP/1.1', 'HTTP/2']:
            return 400,

        #Parse the headers of the request
        headers = {}
        for line in lines[1:]:
            if line == '':
                break
            key, value = line.split(': ')
            headers[key] = value

        body = None
        if len(lines) > 2 and lines[-1] != '':
            body = lines[-1]

        return method, path, headers, body

    #If there are any exceptions
    except Exception as e:
        print(f"Exception: {e}")
        return 500,

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python parser-http.py <PATH OF THE FILE>')
        sys.exit(1)

    file_path = sys.argv[1]
    response = parse_request(file_path)
    print(response)
