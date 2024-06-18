from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from telegram import Bot
from airflow.models import Variable
import telegram
import asyncio

# Retrieve chat_id and token from Airflow Variables
chat_id = Variable.get('TELEGRAM_CHATID')
token = Variable.get('TELEGRAM_TOKEN')

# Asynchronous function to send a message via Telegram
async def send_telegram_message_async():
    bot_token = token
    message = '''   
    Hello from Airflow! 
    
This message is sent using the Airflow Python Operator.
    '''

    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

# Synchronous wrapper to run the async function


def send_telegram_message():
    asyncio.run(send_telegram_message_async())


# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'python_telegram_notification',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=days_ago(1),
    tags=['example'],
    catchup=False
)

# DummyOperator to mark the start of the DAG
start = DummyOperator(
    task_id='start',
    retries=3,
    dag=dag
)

# PythonOperator to send a message via Telegram
python_task = PythonOperator(
    task_id='python_task',
    python_callable=send_telegram_message,
    dag=dag,
)

# DummyOperator to mark the end of the DAG
end = DummyOperator(
    task_id='end',
    retries=3,
    dag=dag
)

# Set the task dependencies
start >> python_task >> end
