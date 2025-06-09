# LangChain01

Corresponds to Udemy course, part 2, "Chaining a simple prompt"

## Set up virtual environment
```
rm -rf venv
virtualenv -p python3.12 venv
. venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt
```

## Usage

update .env file with your API key

Then export it with

```bash
export $(grep -v '^#' .env | xargs)
```

Then run the app with

```bash
python app.py
```

# Later

```
deactivate
```

