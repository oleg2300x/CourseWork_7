from rest_framework import serializers


def check_duration_time(duration):
    """Проверяем длительность привычки. Продолжительность не должна превышать 120 секунд"""
    duration_seconds = duration.hour * 3600 + duration.minute * 60 + duration.second
    if duration_seconds >= 120:
        raise serializers.ValidationError("Время для выработки привычки должно составлять не более 120 секунд")


def check_habit_periodicity(days):
    """Проверяем периодичность привычки. Периодичность не должна превышать 7 дней"""
    if days > 7:
        raise serializers.ValidationError("Периодичность для привыкания должна составлять не более 7 дней")


def validate_fields(reward, associated_nice_habit):
    """Проверка полей привычки. Привычка должна иметь награду или связанную с ней приятную привычку. Не оба поля."""
    if reward and associated_nice_habit:
        raise serializers.ValidationError("Привычка может иметь награду или связанную с ней приятную привычку")
    if not reward and not associated_nice_habit:
        raise serializers.ValidationError("Привычка должна иметь награду или связанную с ней приятную привычку")
