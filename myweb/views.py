from django.shortcuts import render

def for_view(request):
    return render(request, 'myweb/for.html')

def home(request):
    return render(request, 'myweb/home.html')

def about(request):
    return render(request, 'myweb/about.html')

def contact(request):
    return render(request, 'myweb/contact.html')

def skills(request):
    table = None
    results = None
    if request.method == 'POST':
        try:
            table = int(request.POST.get('table', 0))
            if 2 <= table <= 12:
                results = [
                    {'formula': f'{table} x {i}', 'result': table * i}
                    for i in range(1, 13)
                ]
        except Exception:
            table = None
            results = None
    return render(request, 'myweb/skills.html', {'table': table, 'results': results})

def skill_detail(request, name):
    skills = {
        'HTML': {'name': 'HTML', 'level': 'ดี', 'level_class': 'success'},
        'CSS': {'name': 'CSS', 'level': 'ดี', 'level_class': 'success'},
        'JavaScript': {'name': 'JavaScript', 'level': 'พอใช้', 'level_class': 'warning text-dark'},
        'Python': {'name': 'Python', 'level': 'กำลังเรียนรู้', 'level_class': 'info text-dark'},
        'Game Design': {'name': 'Game Design', 'level': 'พอใช้', 'level_class': 'primary'},
    }
    skill = skills.get(name, {'name': name, 'level': 'ไม่พบข้อมูล', 'level_class': 'secondary'})
    return render(request, 'myweb/skill_detail.html', {'skill': skill})
