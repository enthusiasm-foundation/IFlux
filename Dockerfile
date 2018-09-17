FROM jupyter/minimal-notebook

COPY ./ ./
RUN git clone https://github.com/enthusiasm-foundation/pyflux.git
RUN pip install -e ./pyflux/
RUN pip install -e .

ENV FLUX_HOST=""
ENV FLUX_PORT=""

RUN jupyter kernelspec install --user iflux_kernel
