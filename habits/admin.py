from django.contrib import admin

from habits.models import NiceHabit, Habit


@admin.register(NiceHabit)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'place', 'action',)


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = (
    'pk', 'user', 'time', 'place', 'action', 'reward', 'associated_nice_habit', 'periodicity', 'is_public',
    'duration_time', 'next_date',)
