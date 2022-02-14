import os
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), '../')
)

import app.main

if __name__ == '__main__':
    app.main.hello()
    app.main.test()
