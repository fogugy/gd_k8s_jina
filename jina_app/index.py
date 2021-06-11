import os

from jina import Flow
from jina.types.document.generators import from_csv
from jina.parsers.helloworld import set_hw_multimodal_parser


def index(args):
    f = Flow.load_config('flow-index.yml')

    with f, open(f'{args.workdir}/people-img/meta.csv', newline='') as fp:
        f.index(inputs=from_csv(fp), request_size=10)


if __name__ == '__main__':
    args = set_hw_multimodal_parser().parse_args()
    args.workdir = os.environ['HW_WORKDIR']

    index(args)
