from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import mimetypes, os

class UTF8Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        ctype = self.headers.get('Content-Type')
        super().end_headers()
    def guess_type(self, path):
        ctype = super().guess_type(path)
        if ctype and ctype.startswith('text/'):
            if 'charset=' not in ctype:
                ctype += '; charset=utf-8'
        return ctype

if __name__=='__main__':
    os.chdir(os.path.dirname(__file__) + '/..')
    port = int(os.environ.get('PORT','5500'))
    with ThreadingHTTPServer(('', port), UTF8Handler) as httpd:
        print(f'Serving on http://localhost:{port} (UTF-8)')
        httpd.serve_forever()
