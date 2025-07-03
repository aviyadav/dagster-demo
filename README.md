# dagster-demo

#### LINK - https://youtu.be/sKqDq4TFbmY?si=C5EJys44R9a18g_d

#### This project uses uv, to install (on WSL2/Ubuntu)
> wget -qO- https://astral.sh/uv/install.sh | sh

#### create virtual environment
<br><code>uv venv</code>

#### activate virtual environment
<br><code>source .venv/bin/activate</code>

#### install dependencies

- uv pip install dagster dagster-webserver polars duckdb
<br>  or
- uv pip install -r requirements.txt

#### To verify the installed dependencies
<br><code>uv pip list</code>

#### freeze the dependencies
<br><code>uv pip freeze > requirements.txt</code>

### Test a asset
<br><code>dagster dev -f assets.py</code>

--------------------

#### create dagster project
<br><code>dagster project scaffold --name car_data</code>

cd car_data
mkdir data

// $Env:PYTHONLEGACYWINDOWSSTDIO = 'enable'

### to run - 
<code>dagster dev</code>

dagster webserver - http://127.0.0.1:3000




