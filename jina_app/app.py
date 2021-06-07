import os
from jina import Executor, Flow, Document, requests


class MyExecutor(Executor):
    @requests
    def foo(self, **kwargs):
        print('!' * 100)


def init():
    f = (Flow(rest_api=True, port_expose=os.environ['JINA__PORT_EXPOSE'])
         .add(uses=MyExecutor))

    with f:
        f.block()


def search():
    pass


if __name__ == '__main__':
    init()
