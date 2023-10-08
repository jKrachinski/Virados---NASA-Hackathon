import http.server
import socketserver

# Specify the port you want to use
PORT = 3000

# Navigate to the directory containing your WebGL build (replace 'webgl_build' with your actual directory)
DIRECTORY = "C://Users//jpcar//Desktop//templates_html_css//hackaton"

# Create a custom request handler to allow CORS (Cross-Origin Resource Sharing)
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Start the server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()