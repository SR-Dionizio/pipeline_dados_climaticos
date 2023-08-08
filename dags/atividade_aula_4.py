from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

with DAG(
    'Boas_vindas',
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag:
    def cumprimentos():
        print("Boas-vindas ao Airflow!")

    tarefa_4 = PythonOperator(
        task_id= 'Printando',
        python_callable = cumprimentos
    )

