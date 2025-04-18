class Habit:
    def __init__(self, name: str, value: int):
        self.value = value
        self.name = name
        
    def getHabitValue(self) -> int:
        return self.value
    
    def getHabitName(self) -> str:
        return self.name
    
    