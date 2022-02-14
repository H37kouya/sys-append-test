import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
)

import app.usecase.quantum.random_qubit as random_qubit

def hello():
    print('hello')


def test():
    print(random_qubit.create(7))