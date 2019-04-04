class Technology:
    def __init__(self, language, course_name, participants):
        self.language = language
        self.course_name = course_name
        self.participants = participants
        self.course = {self.course_name: int(self.participants)}
        self.total_participants = int(participants)

    def add_course(self, course_name, participants):
        if course_name not in self.course:
            self.course.update({course_name: int(participants)})
        else:
            self.course[course_name] = self.course[course_name] + \
                                            int(participants)
        self.total_participants += int(participants)

    def __str__(self):
        return f"language - {self.language} / total_participants - {self.total_participants}  / course - {self.course}"


data = input()
objects = []

while data != 'end':
    data = data.split(' - ')
    language = data[0]
    courses = data[1]
    courses = courses.split(", ")

    for item in courses:
        course_name = item.split(":")[0]
        participants = item.split(":")[1]

        if language not in [x.language for x in objects]:
            obj = Technology(language, course_name, participants)
            objects.append(obj)
        else:
            for i in objects:
                if i.language == language:
                    i.add_course(course_name, participants)

    data = input()


tech_sort = sorted(objects, key=lambda x: -x.total_participants)

print(f"Most popular: {tech_sort[0].language} ({tech_sort[0].total_participants} participants)")
print(f"Least popular: {tech_sort[-1].language} ({tech_sort[-1].total_participants} participants)")

for index, elem in enumerate(tech_sort):
    print(f"{tech_sort[index].language} \
            ({tech_sort[index].total_participants} participants):")
    course_sort = sorted(elem.course.items(), key=lambda x: -x[1])

    for item in course_sort:
        print(f"--{item[0]} -> {item[1]}")
