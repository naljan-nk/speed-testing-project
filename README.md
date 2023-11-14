# speed-testing-project
# Description

# This project is designed to measure network performance by providing a server hosted on Google Cloud and a JavaScript client that calls APIs to the server. The server has three main routes: `default`, `download`, and `upload`. The JavaScript client interacts with these routes to measure network speed, including ping, download speed, and upload speed.

# Server (server.py)

# The server, implemented in `server.py`, is hosted on Google Cloud and serves as the backend for the project. It offers the following routes:

# 1. Default Route
#   - Purpose: Measure ping
#   - Description: This route is used to measure the ping response time from the server. It's a basic test to check the responsiveness of the network connection.

# 2. Download Route
#   - Purpose: Measure download speed
#   - Description: The download route is used for clients to measure the download speed. It sends a randomly generated 20 MB file to the client, which calculates the time it takes to download the file. This provides a measure of download speed.

# 3. Upload Route
#   - Purpose: Measure upload speed
#   - Description: The upload route expects a 20 MB file from the client and is used to measure the upload speed. When the server is first run, a 20 MB file is generated for this purpose. The client uploads the file, and the time taken for the upload is recorded, giving us the upload speed.

### JavaScript File (script.js)

# The client-side component of the project is implemented in `script.js`. It interacts with the server using APIs and provides three primary functions:

# 1. Ping Server
#   - Description: The `pingServer` function calls the default server route and measures the time it takes for the server to respond. This provides information about the server's ping response time.

# 2. Download File
#   - Description: The `downloadFile` function calls the download route and expects a 20 MB file. It calculates the time it takes to download the file, providing information about download speed.

# 3. Upload File
#   - Description: The `uploadFile` function generates a random 20 MB file and calculates the time it takes to upload the file. This gives us information about the upload speed of the network connection.

### index.html File

# The `index.html` file is the main webpage of the project. It serves as the user interface for interacting with the server and using the JavaScript functions mentioned above. This is where users can initiate the network speed measurements.
