Web Server Project by Sai Appala Rahul Itha

This repository, created for GitHub Classroom, showcases the Web Server Project developed by Sai Appala Rahul Itha.

Welcome Message
Greetings! I am Sai Appala Rahul Itha. It's my pleasure to introduce you to my Web Server Project.

HTTP Parser Testing Instructions

    Initial Setup:
        Clone the repository. In the root directory, you'll find the file parser.py.
        Execute the parser using the command: $ python3 parser.py

    Testing Different HTTP Methods:
        GET Request: $ python3 parser.py test-get.txt
        POST Request: $ python3 parser.py test-post.txt
        HEAD Request: $ python3 parser.py test-head.txt
        DELETE Request: $ python3 parser.py test-delete.txt
        PUT Request: $ python3 parser.py test-put.txt
        CONNECT Request: $ python3 parser.py test-connect.txt

Running the Server.py

    GET Request Implementation:
        Start the server: $ python3 server.py 127.0.0.1 8080
        Access via browser: http://127.0.0.1:8080/get.php

    POST Request Implementation:
        Start the server: $ python3 server.py 127.0.0.1 8080
        Access via browser: http://127.0.0.1:8080/post.php
        Send a POST request using curl: $ curl -X POST -d "name=Rahul&age=32" http://127.0.0.1:8080/post.php

For testing methods other than GET and POST, use corresponding .txt files as these requests cannot be tested directly through a PHP interface.

Ansible Implementation Instructions

    Configuration:
        Update hosts.ini with the IP address of your target server.
        Modify myplaybook.yaml and python_server.service.j2 with appropriate SRC and DEST file locations.

    Execution:
        Run the playbook: $ ansible-playbook -i hosts.ini myplaybook.yaml
        Verify successful deployment on the target system's IP address.
        On the remote or testing system, check active connections: $ sudo netstat -tuln | grep 8080
        Test connectivity: $ sudo nc -zv [Remote System IP] [Port]

This documentation ensures clear guidance for deploying and testing the web server, demonstrating professionalism and attention to detail in system configuration and deployment.
