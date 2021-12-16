from django.shortcuts import render


# Create your views here.

def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        first_number = int(request.POST.get('first_number'))
        second_number = int(request.POST.get('second_number'))
        context = {}
        if request.POST.get('math_action') == 'add':
            context = {'Result': f'{first_number} + {second_number} = {first_number + second_number}'}
        elif request.POST.get('math_action') == 'subtract':
            context = {'Result': f'{first_number} - {second_number} = {first_number - second_number}'}
        elif request.POST.get('math_action') == 'divide':
            context = {'Result': f'{first_number} / {second_number} = {first_number / second_number}'}
        elif request.POST.get('math_action') == 'multiply':
            context = {'Result': f'{first_number} * {second_number} = {first_number * second_number}'}
        return render(request, 'index.html', context)



