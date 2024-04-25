from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User_report
from .forms import User_reportForm
from django.contrib import messages
from django.shortcuts import render



@login_required
def create_report(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        if User_report.objects.filter(user_id=user).exists():
            messages.error(request, 'Пользователь с таким ID уже существует.')
            return redirect('create_report')
        else:
            form = User_reportForm(request.POST)
            if form.is_valid():
                report = form.save(commit=False)
                report.user = request.user
                report.save()
                messages.success(request, 'Сообщение от пользователя создано.')
                return redirect('bug_report_home')
    else:
        form = User_reportForm()
    return render(request, 'bug_report/create_report.html', {'form': form})

@login_required
def bug_report_home(request):
    bug_reports = User_report.objects.filter(user=request.user)
    return render(request, 'bug_report/bug_report_home.html', {'bug_reports': bug_reports})

@login_required
def one_bug_report(request, pk_bug_report):
    bug_report = get_object_or_404(User_report, pk=pk_bug_report, user=request.user)
    return render(request, 'bug_report/one_bug_report.html', {'bug_report': bug_report})

@login_required
def download_log_file(request, pk_bug_report):
    bug_report = get_object_or_404(User_report, pk=pk_bug_report, user=request.user)
    if bug_report.file:
        with bug_report.file.open('rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename="log_file.log"'
            return response
    return HttpResponse("Файл не найден", status=404)

@login_required
def update_bug_status(request, pk_bug_report):
    bug_report = get_object_or_404(User_report, pk=pk_bug_report, user=request.user)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        bug_report.status = new_status
        bug_report.save()

        if new_status == 'D':  # Если статус "выполнено", удаляем запись
            bug_report.delete()

        return redirect('bug_report_home')

    return redirect('bug_report_home')


