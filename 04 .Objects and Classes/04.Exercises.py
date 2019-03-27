class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems

data = input()

exercises = []
while data != "go go go":
    split_data = data.split(" -> ")
    object_exercise = Exercise(split_data[0], split_data[1], split_data[2],
                               [x for x in split_data[3].split(", ")])
    exercises.append(object_exercise)

    data = input()

for item in exercises:
    print(f"Exercises: {item.topic}")
    print(f'Problems for exercises and homework for the "{item.course_name}" \
            course @ SoftUni.')
    print(f"Check your solutions here: {item.judge_contest_link}")
    for x, y in enumerate(item.problems):
        print(f"{x+1}. {y}")
