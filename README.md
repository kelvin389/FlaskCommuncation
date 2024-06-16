# FlaskCommuncation
 
Examples of using Flask and JQuery to create a control panel webpage that interacts with a python applcation. A basic version using GET and POST requests is included, as well as a version using socketio to seamlessly exchange information without polling or redirecting the page with requests.

Creates a counter that counts up from 0 with a web page that is able to start/stop the counter. Utilizes multithreading to ensure the counter incrementing does not block the users inputs to start/stop.

The page created by these applications can be found at http://127.0.0.1:5000

## Basic
The webpage uses POST requests to the app to start and stop the loop. GET requests are used to retrieve the number from the application, polling once every second to keep the counter up to date.

## Socket
The page emits to tell the app to start/stop counting, with the app hooking to these emits. Similarly, the app emits when the counter increments with the page hooking to this emit and updating the text the user sees.