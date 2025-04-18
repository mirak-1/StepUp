from user import User
from habit import Habit

u = User("Karim")
h1 = Habit("Training", 50)
h2 = Habit("Reading", 60)
h3 = Habit("Steps", 40)

u.trackHabit(h1)
u.trackHabit(h2)
u.trackHabit(h3)

u.getTrackedHabits()

