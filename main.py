import socketserver
import http.server

server = socketserver.TCPServer(('0.0.0.0', 5),

http.server.SimpleHTTPRequestHandler)
print('[OK] Running on Port 5')
print("[ERROR] gave 404 bad ur?")
print("[CONNECTION] Timed Out")
server.serve_forever()
