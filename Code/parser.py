import sys

def parse_request(file_path):
    try:
        with open(file_path, 'r') as f:
            request = f.read()

        lines = request.splitlines()

        # Parse the request method, path, and version
        method, path, version = lines[0].split(' ')
        

        # Make sure that the version is valid
        if version not in ['HTTP/1.0', 'HTTP/1.1', 'HTTP/2']:
            return '400 BAD REQUEST\r\n\r\n'
        
        # Make sure that the method is valid
        valid_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'CONNECT']
        if method not in valid_methods:
            return '400 BAD REQUEST\r\n\r\n'

        # Parse the headers of the request
        headers = {}
        for line in lines[1:]:
            if line == '':
                break
            key, value = line.split(': ')
            headers[key] = value

        # Parse the body of the request
        body = None
        if lines[-1] != '':
            body = lines[-1]

        # Condition if request made is valid
        return f"200 OK - {method} \r\n\r\n"

    except Exception as e:
        # If there occurs any exception
        return '500 INTERNAL SERVER ERROR\r\n\r\n'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 parser.py <PATH OF THE FILE>')
        sys.exit(1)

    file_path = sys.argv[1]
    response = parse_request(file_path)
    print(response)
