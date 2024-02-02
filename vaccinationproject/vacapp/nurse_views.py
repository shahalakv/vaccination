from urllib import request

from django.contrib import messages
from django.shortcuts import redirect, render

from vacapp.filters import VaccineFilter, VaccinesFilter, UsersFilter, HospitalsFilter, SchedulesFilter, \
    ComplaintsFilter
from vacapp.form import AppointmentForm, ComplaintForm, NurseForm
from vacapp.models import Appointment, Complaint, Vaccine, Vaccination, Hospital, Book_Appointment


def vaccine_views(request):
    new = Vaccine.objects.all()
    vaccinesFilter = VaccinesFilter(request.GET, queryset=new)
    new = vaccinesFilter.qs
    context = {
        'vaccines': new,
        'vaccinesFilter': vaccinesFilter,
    }
    return render(request, 'nursetemp/vaccine_views.html', context)

def user_views(request):
    new = Vaccination.objects.filter(is_user=True)
    usersFilter = UsersFilter(request.GET, queryset=new)
    new = usersFilter.qs
    context = {
        'users': new,
        'usersFilter': usersFilter,
    }
    return render(request, 'nursetemp/user_views.html', context)

def hospital_views(request):
    new = Hospital.objects.all()
    hospitalsFilter = HospitalsFilter(request.GET, queryset=new)
    new = hospitalsFilter.qs
    context = {
        'hospitals': new,
        'hospitalsFilter': hospitalsFilter,
    }
    return render(request, 'nursetemp/hospital_views.html', context)

def complaints(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            ob = form.save(commit=False)
            ob.user = u
            ob.save()
        return redirect('complaint_views')
    return render(request, 'nursetemp/complaints.html', {'form': form})

def complaint_views(request):
    new = Complaint.objects.filter(user=request.user)
    complaintsFilter = ComplaintsFilter(request.GET, queryset=new)
    new = complaintsFilter.qs
    context = {
        'complaints': new,
        'complaintsFilter': complaintsFilter,
    }
    return render(request, 'nursetemp/complaint_views.html', context)

def complaint_updates(request, up):
    taskupdate = Complaint.objects.get(id=up)
    updateform = ComplaintForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = ComplaintForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("complaint_views")
    return render(request, 'nursetemp/complaint_updates.html', {"updateform": updateform})

def complaint_deletes(request, dl):
    taskdelete = Complaint.objects.get(id=dl)
    taskdelete.delete()
    return redirect("complaint_views")
def complaint_replay_status(request):
    new = Complaint.objects.filter(user=request.user)
    return render(request, 'nursetemp/complaint_replay_status.html', {"new": new})
def profile_view(request):
    new = Vaccination.objects.filter(username=request.user).first()
    return render(request, 'nursetemp/profile_view.html', {"new": new})




def schedules(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_views')
    return render(request, 'nursetemp/schedules.html', {'form': form})

def schedule_views(request):
    new = Appointment.objects.all()
    schedulesFilter = SchedulesFilter(request.GET, queryset=new)
    new = schedulesFilter.qs
    context = {
        'schedules': new,
        'schedulesFilter': schedulesFilter,
    }
    return render(request, 'nursetemp/schedule_views.html', context)


def schedule_updates(request, up):
    taskupdate = Appointment.objects.get(id=up)
    updateform = AppointmentForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = AppointmentForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("schedule_views")
    return render(request, 'nursetemp/schedule_updates.html', {"updateform": updateform})

def schedule_deletes(request, dl):
    taskdelete = Appointment.objects.get(id=dl)
    taskdelete.delete()
    return redirect("schedule_views")


def view_book_appointments(request):
    new = Book_Appointment.objects.filter(status=1).order_by('schedule__date')
    return render(request, 'nursetemp/view_book_appointments.html', {"new": new})
def vaccination(request,id):
    n = Book_Appointment.objects.get(id=id)
    print(n)
    n.vaccinated = 1
    n.save()
    messages.info(request, 'Vaccinated')
    return redirect('view_book_appointments')


def profile_updates(request,up):
    taskupdate = Vaccination.objects.get(id=up)
    updateform = NurseForm(instance=taskupdate)
    print(updateform)
    if request.method == 'POST':
        updateform = NurseForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("profile_view")
    return render(request, 'nursetemp/profile_updates.html', {"updateform": updateform})
