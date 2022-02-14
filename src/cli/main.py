import os
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), '../')
)

import app.main

app.main.hello()
