from django.contrib import messages
from django.shortcuts import redirect, render
from vacapp.filters import SchedulezFilter, ComplaintzFilter, ReportcardzFilter
from vacapp.form import ComplaintForm, UserForm
from vacapp.models import Complaint, Appointment, Vaccination, Book_Appointment


def schedule_viewz(request):
    new = Appointment.objects.all()
    schedulezFilter = SchedulezFilter(request.GET, queryset=new)
    new = schedulezFilter.qs
    context = {
        'schedulez': new,
        'schedulezFilter': schedulezFilter,
    }
    return render(request, 'usertemp/schedule_viewz.html', context)

def complaintz(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            ob = form.save(commit=False)
            ob.user = u
            ob.save()
            return redirect('complaint_viewz')
    else:
        form=ComplaintForm()
    return render(request, 'usertemp/complaintz.html', {'form': form})

def complaint_viewz(request):
    new = Complaint.objects.filter(user=request.user)
    complaintzFilter = ComplaintzFilter(request.GET, queryset=new)
    new = complaintzFilter.qs
    context = {
        'complaintz': new,
        'complaintzFilter': complaintzFilter,
    }
    return render(request, 'usertemp/complaint_viewz.html', context)


def complaint_updatez(request, up):
    taskupdate = Complaint.objects.get(id=up)
    updateform = ComplaintForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = ComplaintForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("complaint_viewz")
    return render(request, 'usertemp/complaint_updatez.html', {"updateform": updateform})

def complaint_deletez(request, dl):
    taskdelete = Complaint.objects.get(id=dl)
    taskdelete.delete()
    return redirect("complaint_viewz")
def complaint_status(request):
    new = Complaint.objects.filter(user=request.user)
    return render(request, 'usertemp/complaint_status.html', {"new": new})


def profile(request):
    new = Vaccination.objects.filter(username=request.user).first()
    return render(request, 'usertemp/profile.html', {"new": new})

def book_appointment(request, id):
    schedule = Appointment.objects.get(id=id)
    data = request.user
    appointment = Book_Appointment.objects.filter(user_id=data, schedule=schedule)
    if appointment.exists():
        messages.info(request, 'you have already requested appointment for this schedule')
        return redirect('schedule_viewz')
    else:
        if request.method == 'POST':
            obj = Book_Appointment()
            obj.user = data
            obj.schedule = schedule
            obj.vaccine_name = schedule.vaccine
            obj.save()
            return redirect('view_appointment')
    return render(request, 'usertemp/book_appointment.html', {'schedule': schedule})


def view_appointment(request):
    u = request.user
    print(u)
    new = Book_Appointment.objects.filter(user=u)
    appointmentzFilter = SchedulezFilter(request.GET, queryset=new)
    new = appointmentzFilter.qs
    context = {
        'appointmentz': new,
        'appointmentzFilter': appointmentzFilter,
    }
    return render(request, 'usertemp/view_appointment.html', context)


def profile_update(request,up):
    taskupdate = Vaccination.objects.get(id=up)
    updateform = UserForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = UserForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("profile_view")
    return render(request, 'usertemp/profile_update.html', {"updateform": updateform})


def reportcard_viewz(request):
    new = Book_Appointment.objects.filter(user=request.user)
    reportcardzFilter = ReportcardzFilter(request.GET, queryset=new)
    new = reportcardzFilter.qs
    context = {
        'reportcardz': new,
        'reportcardzFilter': reportcardzFilter,
    }
    return render(request, 'usertemp/reportcard_viewz.html', context)
