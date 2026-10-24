# HelloWorldSample

A tiny Python sample app for learning GitHub Copilot workflows.

## What it does
- Starts a local web server on `http://127.0.0.1:8000`
- Serves a simple HTML page with a "Hello, World!" message
- Exposes a JSON endpoint at `/api/hello`

## Run it
From the repo root:

```bash
python docs/HelloWorldSample/app.py
```

Then open:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/api/hello`

## Notes
This is intentionally minimal so it is easy to extend later with:
- a form
- a database
- a REST API
- a frontend framework
