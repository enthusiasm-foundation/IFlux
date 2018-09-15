# IFlux

Kernel to run [Flux](https://github.com/influxdata/flux) queries by
communicating with `fluxd` (connected to an InfluxDB instance).

### Run locally

Install jupyter:

```
$ pip install jupyter
```

Install dependencies and kernel:

```
$ pip install -r requirements.txt
$ export FLUX_HOST="localhost"
$ export FLUX_PORT=8093
$ jupyter kernelspec install iflux_kernel
```

Start notebook:

```
$ jupyter notebook
```

You can now select `IFlux` kernel and start querying with Flux.

### Run with Docker

```
$ docker run -p 8888:8888 -e FLUX_HOST=localhost -e FLUX_PORT=8093 \
  --rm enthusiasm/iflux-notebook:latest
```

connect to `localhost:8888` and copy paste the token. Enjoy Flux.

__Example query__:

```
from(bucket: "telegraf") |> range(start: -10s) |> filter(fn: (r) => r._measurement == "cpu" and r._field == "usage_system")
```
