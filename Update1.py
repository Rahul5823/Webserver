import sys

def parse_request(request_str):
    try:
        # Split the request into lines
        lines = request_str.split('\r\n')

        # Ensure the request is not empty
        if not lines:
            return "400 BAD REQUEST"

        # Parse the first part of the request to find the method type
        first = lines[0].split(' ')
        if len(first) != 3:
            return "400 BAD REQUEST"
        
        method, path, protocol = first

        # Check if method is GET or POST
        # More methods will be added later on in the project
        if method not in ['GET', 'POST']:
            return "400 BAD REQUEST"

        # Check if the request is valid or not based on the requirements mentioned

        return "200 OK"
    
    except Exception as e:
        return "500 INTERNAL SERVER ERROR"

def main():
    if len(sys.argv) != 2:
        print("Invalid arguments Usage: python Update1.py <PATH TO 'request.txt'>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            http_request = file.read()
            response = parse_request(http_request)
            print(response)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
