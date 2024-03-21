from rest_framework import serializers
from habits.models import Habit, NiceHabit
from habits.validators import check_duration_time, check_habit_periodicity, validate_fields


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для привычки"""
    duration_time = serializers.TimeField(validators=[check_duration_time])
    periodicity = serializers.IntegerField(validators=[check_habit_periodicity])

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        if data.get('reward'):
            reward = data.get('reward')
        else:
            reward = None
        if data.get('associated_nice_habit'):
            associated_nice_habit = data.get('associated_nice_habit')
        else:
            associated_nice_habit = None
        validate_fields(reward, associated_nice_habit)
        return data


class PublicHabitsSerializer(serializers.ModelSerializer):
    """Сериализатор для публичных привычек"""
    class Meta:
        model = Habit
        fields = '__all__'


class NiceHabitSerializer(serializers.ModelSerializer):
    """Сериализатор для хороших привычек"""
    class Meta:
        model = NiceHabit
        fields = "__all__"
