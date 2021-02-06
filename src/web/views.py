from flask import Blueprint
from google.cloud import bigquery


PROJECT_ID = 'per-dt'
DATA_SET = 'models'
TABLE_NAME = 'charge_dynamics'
table_id = PROJECT_ID + '.' + DATA_SET + '.' + TABLE_NAME
client = bigquery.Client()

views = Blueprint("views", __name__)


@views.route("/")
def home():
    QUERY = (f"""SELECT * FROM {table_id}""")
    query_job = client.query(QUERY)
    rows = query_job.result()
    df = rows.to_dataframe()
    return get_format(df)


def get_format(df):
    mill_power = df["mill_power"][0]
    total_weight = df["total_weight"][0]

    string = f"""
    <h1 align=center>Digital Twin</h1>
    <div align=center>
    Mill Power = {mill_power} <br>
    Total Weight = {total_weight}
    </div>
    """
    return string
