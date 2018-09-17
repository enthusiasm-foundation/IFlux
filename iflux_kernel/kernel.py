from ipykernel.kernelbase import Kernel
from IPython.display import display, HTML

from pyflux import Flux, Render
import json, os
import pandas as pd

class IFluxKernel(Kernel):
    implementation = 'IFlux'
    implementation_version = '1.0'
    language = 'fluxlang'
    language_version = '0.1'
    language_info = {
        'name': 'FluxLang',
        'mimetype': 'text/plain',
        'file_extension': '.flux',
    }
    banner = "IFlux Kernel"

    def __init__(self, hostname="localhost", port=8093, *args, **kwargs):
        super().__init__(*args, **kwargs)
        hn = os.environ.get("FLUX_HOST", hostname)
        p = os.environ.get("FLUX_PORT", port)
        self.client = Flux(host=hn, port=p)

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            resp = self.client.eval_query(code)

            for res in resp:
                if "error" not in res.headers[0] :
                    df = Render().table(res)
                    
                    stream_content = {
                        'name': 'stdout',
                        'data': {'text/html': df.to_html()}
                    }
                    self.send_response(self.iopub_socket, 'display_data', stream_content)

                    display(stream_content)
                else:
                    self.send_response(self.iopub_socket, 'stream', {'name':'stdout', 'text':res.headers[0]})

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
