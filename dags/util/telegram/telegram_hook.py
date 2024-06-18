from airflow.hooks.base import BaseHook
import requests

class TelegramHook(BaseHook):
    def __init__(self, telegram_conn_id):
        """
        Initialize the TelegramHook with the given connection ID.

        :param telegram_conn_id: The connection ID for Telegram.
        """
        super().__init__()
        self.telegram_conn_id = telegram_conn_id
        self.base_url = "https://api.telegram.org/bot"
    
    def get_conn(self):
        """
        Get the connection for Telegram.

        :return: The Telegram connection.
        """
        connection = self.get_connection(self.telegram_conn_id)
        return connection
    
    def send_message(self, chat_id, message):
        """
        Send a message to a Telegram chat.

        :param chat_id: The ID of the chat to send the message to.
        :param message: The message to send.
        :return: The response from the Telegram API.
        """
        connection = self.get_conn()
        token = connection.password
        url = f"{self.base_url}{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, data=data)
        return response.json()
