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


<br><code> </code>

#### freeze the dependencies
<br><code>uv pip freeze > requirements.txt</code>

dagster dev -f assets.py

--------------------

dagster project scaffold --name car_data

cd car_data
mkdir data

// $Env:PYTHONLEGACYWINDOWSSTDIO = 'enable'

to run - dagster dev

dagster webserver - http://127.0.0.1:3000




