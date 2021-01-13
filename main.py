from new_user import NewUser
from habit_graph import Habits
from post_habit import PostHabit
from edit_habit import EditGraph
from del_habit import DelGraph

# Instances:
new_user = NewUser()
habits = Habits()
post_habit = PostHabit()
edit_habit = EditGraph()
del_habit = DelGraph()


class HabitTracker:
    def __init__(self):
        # new_user.new_user_response()
        # habits.habit_response()
        # post_habit.post_response()
        edit_habit.update_response()
        # del_habit.del_response()


HabitTracker()
