from django.shortcuts import render

# oy = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
#       'December']


# Create your views here.


# def months(request):
#     return render(request, 'months/days.html', {'oy': oy})


def file_contents(request):

    with open('lessons.txt', 'r') as file:
        lines = file.readlines()

    lessons = []
    for i, line in enumerate(lines):
        col = 'red' if i < 6 else 'green'
        lesson = {
            'line': line.strip(),
            'color': col
        }
        lessons.append(lesson)
    return render(request, 'file_contents.html', {'lessons': lessons})


