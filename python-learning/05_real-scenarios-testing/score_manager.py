"""
Problem Statement:
------------------
Create a class `ScoreManager` that manages exam scores for students.

Implement:
- add_score(student: str, score: int): Adds a student's score.
- average_score(): Returns the average score of all students.
- top_student(): Returns the student with the highest score.

What it tests:
--------------
- List and dictionary manipulation.
- Loops, sorting, and simple average calculation.
"""

class ScoreManager:
    def __init__(self):
        self.scores = {}

    def add_score(self, student: str, score: int):
        """Add or update the student's score."""
        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            return
        self.scores[student] = score

    def average_score(self) -> float:
        """Return the average score of all students."""
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)

    def top_student(self) -> str:
        """Return the student with the highest score."""
        if not self.scores:
            return "No students yet."
        return max(self.scores, key=self.scores.get)


# Example usage
if __name__ == "__main__":
    sm = ScoreManager()
    sm.add_score("Alice", 90)
    sm.add_score("Bob", 85)
    sm.add_score("Charlie", 95)
    print(sm.average_score())   # Output: 90.0
    print(sm.top_student())     # Output: Charlie
