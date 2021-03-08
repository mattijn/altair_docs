# Development

Do a clean doc build:

The following dependencies are required to build the docs:

jupyter-book
numpydoc
pandas
toolz
recommonmark
vega_datasets
altair_saver
pillow

```bash
$ cd doc
$ make clean-all
$ make html
$ cd _build/html; python -m http.server
```

Navigate to http://localhost:8000 and ensure it looks OK (particularly
do a visual scan of the gallery thumbnails).
