class Video:
    def __init__(self, lecture, trainer, course, duration):
        self.lecture = lecture
        self.trainer = trainer
        self.course = course
        self.duration = duration

videos = []
servers = []
server_time = 0

data = input()

while True:
    data = data.split(';')
    if len(data) < 2:
        if len(videos) != 0:
            servers.append(videos)
        break

    lecture = None
    trainer = None
    course = None
    duration = 0

    for item in data:
        first_elem = item.split(':')[0]
        second_elem = item.split(':')[1]

        if first_elem == "lecture":
            lecture = second_elem
        elif first_elem == 'trainer':
            trainer = second_elem
        elif first_elem == 'course':
            course = second_elem
        else:
            minutes = second_elem.split("h")[0]
            seconds = second_elem.split("h")[1][:-1]
            if seconds[0] == '0':
                seconds = seconds[1:]
            duration = (int(minutes) * 60) + int(seconds)

    video = Video(lecture, trainer, course, duration)
    if server_time + video.duration <= 600:
        server_time += video.duration
        videos.append(video)
    else:
        servers.append(videos)
        server_time = 0
        server_time += video.duration
        videos = [video]

    data = input()


data = data[0].split(' ')
first_param = data[1]
second_param = data[2]

total_duration = 0
for index, item in enumerate(servers):
    for vid in item:
        if vid.course == second_param:
            print(f"https://streamcdn{index + 1}.softuni.bg/course={vid.course}&lecture={vid.lecture}&trainer={vid.trainer}")
            total_duration += vid.duration
        elif vid.trainer == second_param:
            print(f"https://streamcdn{index + 1}.softuni.bg/course={vid.course}&lecture={vid.lecture}&trainer={vid.trainer}")
            total_duration += vid.duration

hours = total_duration // 60
minutes = total_duration - (hours * 60)


def input_zero(integer):
    if len(str(integer)) == 1:
        return "0" + str(integer)
    else:
        return integer

print(f"total duration: {input_zero(hours)}:{input_zero(minutes)}:00")
