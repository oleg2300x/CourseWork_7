import requests

from config.settings import TELEGRAM_BOT_API_KEY

telegram_token = TELEGRAM_BOT_API_KEY
send_message_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'


def create_message(habit, user):
    """Создаём сообщение"""
    if habit.reward:
        reward_text = f"Побалуйте себя {habit.reward}!"
    else:
        reward_text = f"Вы можете {habit.associated_nice_habit.action}!"
    result = f"Здавствуйте, {user.name}! Сегодня в {habit.time} на {habit.place} вам нужно {habit.action} " \
             f"в течении {habit.duration_time}! {reward_text} Хороше дня!!!"
    return result


def send_telegram_message(habit):
    """Функция отправки сообщения в Telegram"""
    user = habit.user
    message = create_message(habit, user)
    requests.post(
        url=send_message_url,
        data={
            'chat_id': user.telegram_chat_id,
            'text': message
        })
