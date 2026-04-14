"""
Tiny local server that appends client email submissions from quote.html
to client_emails.csv in this folder.

Run:  python email_server.py
Then open quote.html in a browser and submit the form.
"""
import csv
import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

CSV_PATH = Path(__file__).parent / "client_emails.csv"
HEADERS = ["Timestamp", "Email", "Scope", "Total"]
HOST, PORT = "127.0.0.1", 8000


def ensure_csv():
    if not CSV_PATH.exists() or CSV_PATH.stat().st_size == 0:
        with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(HEADERS)


class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path != "/save":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        try:
            data = json.loads(self.rfile.read(length).decode("utf-8"))
        except Exception:
            self.send_response(400)
            self._cors()
            self.end_headers()
            self.wfile.write(b'{"ok":false,"error":"bad json"}')
            return

        row = [
            data.get("timestamp") or datetime.now().isoformat(timespec="seconds"),
            data.get("email", ""),
            data.get("scope", ""),
            data.get("total", ""),
        ]
        ensure_csv()
        with CSV_PATH.open("a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(row)
        print(f"[saved] {row}", flush=True)

        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def log_message(self, format, *args):
        return  # silence default access logs; we print our own


if __name__ == "__main__":
    ensure_csv()
    print(f"Email server running at http://{HOST}:{PORT}")
    print(f"Saving to: {CSV_PATH}")
    print("Press Ctrl+C to stop.\n")
    try:
        HTTPServer((HOST, PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
