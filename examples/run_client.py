import sys
sys.path.insert(0, '..')
from server.client_example import *

if __name__ == '__main__':
    app.run(debug=True, port=5001)