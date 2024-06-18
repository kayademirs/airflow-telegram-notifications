FROM apache/airflow:2.9.2

RUN pip install python-telegram-bot 
RUN pip install apache-airflow-providers-telegram




