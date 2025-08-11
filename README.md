This script demonstrates how to send a POST and GET request to an API endpoint using requests in Python.
It reads the API endpoint from a configuration file (configurations.ini), constructs a JSON payload, sends it to the server, and prints the response.

Features:
Reads API endpoint from configurations.ini

Sends a POST request with a JSON payload

Handles and prints API responses

Modular payload creation (separate payload.py file)

  ├── API_Post_Request.py   # Main script to send POST request
  ├── payload.py            # Contains payload creation function
utilities/
  ├── configurations.ini    # Stores API endpoint and settings

[requests.read](https://requests.readthedocs.io/en/latest/)  
