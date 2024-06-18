from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from util.telegram.telegram_hook import TelegramHook

class TelegramOperator(BaseOperator):
    """
    Operator for sending messages via Telegram.

    :param telegram_conn_id: The connection ID to use for Telegram.
    :type telegram_conn_id: str
    :param chat_id: The ID of the chat where the message will be sent.
    :type chat_id: str
    :param message: The message to send.
    :type message: str
    :param args: Additional arguments for the BaseOperator
    :param kwargs: Additional keyword arguments for the BaseOperator
    """
    @apply_defaults
    def __init__(self, telegram_conn_id, chat_id, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.telegram_conn_id = telegram_conn_id
        self.chat_id = chat_id
        self.message = message
        
    
    def execute(self, context):
        """
        Execute the TelegramOperator.

        :param context: The context of the execution.
        """
        hook = TelegramHook(self.telegram_conn_id)
        hook.send_message(self.chat_id, self.message)
