from airflow import DAG
from airflow.providers.telegram.operators.telegram import TelegramOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable

# Retrieve the chat ID from Airflow Variables
chat_id = Variable.get('TELEGRAM_CHATID')

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
with DAG('telegram_notification_dag',
         default_args=default_args,
         schedule_interval='@daily',
         start_date=days_ago(1),
         tags=['example'],
         catchup=False) as dag:

    # Task to send a message using the TelegramOperator
    send_message = TelegramOperator(
        task_id='send_message',
        telegram_conn_id='telegram',  # Ensure this connection is set up in Airflow
        chat_id=chat_id,
        text = '''
        Hello from Airflow! 
        
This message is sent using the Airflow Telegram Operator.''',
    )
