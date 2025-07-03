# dagster-demo

#### LINK - https://youtu.be/sKqDq4TFbmY?si=C5EJys44R9a18g_d

### This project uses uv, to install (on WSL2/Ubuntu)
> wget -qO- https://astral.sh/uv/install.sh | sh

### create virtual environment
<br><code>uv venv</code>
<br><code> </code>

#### activate virtual environment
<br><code>source .venv/bin/activate</code>

uv pip install dagster dagster-webserver polars duckdb

uv pip list

uv pip freeze > requirements.txt

dagster dev -f assets.py

--------------------

dagster project scaffold --name car_data

cd car_data
mkdir data

// $Env:PYTHONLEGACYWINDOWSSTDIO = 'enable'

to run - dagster dev

dagster webserver - http://127.0.0.1:3000




