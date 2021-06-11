import os

from jina import Flow
from jina.parsers.helloworld import set_hw_multimodal_parser


def search():
    f = Flow.load_config('flow-search.yml')

    with f:
        f.block()


if __name__ == '__main__':
    args = set_hw_multimodal_parser().parse_args()
    args.workdir = os.environ['HW_WORKDIR']

    search()
