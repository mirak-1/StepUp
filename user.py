from habit import Habit

class User:
    def __init__(self, username: str):
        self.username = username
        self.current_xp = 0
        self.current_level = 1
        self.threshold = 100
        self.habits = []
        

    def computeXP(self, xp_value) -> None:
        value = xp_value + self.current_xp
        self.current_xp = value % self.threshold
        if (value > self.threshold):
            self.current_level += value // self.threshold
            print(f"Congratulations, you gained {value // self.threshold} level(s)! ")
        
    
    def getCurrentXP(self) -> int:
        return self.current_xp
    
    def getCurrentLevel(self) -> int:
        return self.current_level
    
    def trackHabit(self, habit: Habit) -> None:
        self.habits.append(habit)
        
    def getTrackedHabits(self) -> None:
        for habit in self.habits:
            print(habit.getHabitName())

    