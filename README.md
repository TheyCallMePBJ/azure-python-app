# Python Resume Web App

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open <http://localhost:5000>.

## Upload to Azure App Service

Create a Linux Azure Web App with a Python runtime, upload this folder, and set the startup command to:

```text
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```

Azure installs the packages from `requirements.txt` during deployment.
