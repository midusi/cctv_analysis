
import sys
sys.path.insert(0, '..')
from server.app import *

if __name__ == '__main__':
    app.run(debug=True)