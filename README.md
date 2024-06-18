# User Guide for Airflow Telegram Notifications

This GitHub repository contains a step-by-step guide for receiving notifications via Telegram using Apache Airflow. The guide covers the process from creating the Telegram bot to setting up the Airflow environment on Docker.

## Purpose

The purpose of this repository is to create and configure a Telegram bot that will allow you to receive notifications while managing your workflows with Apache Airflow. This way, you can receive real-time notifications about the status of your Airflow workflows and intervene quickly when needed.

## Requirements

Before you begin, ensure you have the following:

- Python 3.6 or higher installed
- Docker and Docker Compose installed
- Access to a Telegram account

## How to Use

1. **Creating a Telegram Bot**: The first step is to create a bot on Telegram. To do this, send a message to `@BotFather` on Telegram, create a new bot, and make a note of the token you receive.

2. **Getting the Chat ID**: You need to obtain the chat ID of the chat you will use with your Telegram bot. You can use the `get_chat_id.py` script found in the repository.

   - Install the required packages:

     ```bash
     pip install -r requirements.txt
     ```

   - Create a `.env` file and add the following lines:

     ```env
     TELEGRAM_TOKEN=YOUR_TOKEN
     TITLE=YOUR_TITLE
     ```

   - Run the script:

     ```bash
     python get_chat_id.py
     ```

3. **Setting up the Airflow Environment with Docker**: Use the `docker-compose.yml` file in the repository to start Airflow on Docker.

   ```bash
   docker-compose up --build -d
   ```

4. **Connecting Airflow with Telegram**: Access the Airflow web server container in Docker and configure Airflow with your Telegram token and chat ID.

   ```bash
   docker exec -it airflow-webserver bash

   airflow variables set TELEGRAM_TOKEN YOUR_TOKEN
   airflow variables set TELEGRAM_CHATID YOUR_CHATID

   airflow connections add telegram \
       --conn-type=telegram \
       --conn-password=YOUR_TOKEN
   ```

Once you have completed these steps, you will receive the notifications you have set up via Telegram when your Airflow workflows run.
