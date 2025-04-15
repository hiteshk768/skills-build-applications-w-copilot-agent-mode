from django.core.management.base import BaseCommand
from ...models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members = [user1, user2]
        team1.save()

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(minutes=30))
        Activity.objects.create(user=user2, activity_type='Cycling', duration=timedelta(hours=1))

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=150)
        Leaderboard.objects.create(user=user2, score=200)

        # Create test workouts
        workout1 = Workout.objects.create(name='Push-ups', description='Do 20 push-ups')
        self.stdout.write(f'Created workout: {workout1}')
        workout2 = Workout.objects.create(name='Sit-ups', description='Do 30 sit-ups')
        self.stdout.write(f'Created workout: {workout2}')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
