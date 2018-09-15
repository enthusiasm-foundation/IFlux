FROM jupyter/minimal-notebook

COPY ./iflux_kernel ./iflux_kernel
COPY requirements.txt .
RUN git clone https://github.com/enthusiasm-foundation/pyflux.git
RUN pip install -e ./pyflux/pyflux/
ENV FLUX_HOST=""
ENV FLUX_PORT=""
RUN pip install -r requirements.txt
RUN jupyter kernelspec install --user iflux_kernel
