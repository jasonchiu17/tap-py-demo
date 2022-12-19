# tap-py-demo
python demo code for Vmware TAP CI/CD.<BR>
A basic sample which began life as part of the [Packeto Buildpack](https://github.com/paketo-buildpacks/samples) samples.

## Running Locally
```
flask --app app.server run --port=5001

Debug mode: 
flask --debug --app  app.server run --port=5001
```

## Viewing
```
curl http://localhost:5001
```

## Application Endpoints
1. `/` :  Index page
2. `/index2` : url_for() test
3. `/api` : API response json data

## Unit test (pytest)
```
pytest

pytest -s -v  (Increase verbosity)
```

