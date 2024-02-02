from django.urls import path
from . import views, admin_views, nurse_views, user_views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_reg', views.user_reg, name='user_reg'),
    path('nurse_reg', views.nurse_reg, name='nurse_reg'),
    path('user_page', views.user_page, name='user_page'),
    path('nurse_page', views.nurse_page, name='nurse_page'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),

    path('admin_page', admin_views.admin_page, name='admin_page'),
    path('nurse_view', admin_views.nurse_view, name='nurse_view'),
    path('nurse_update/<int:up>', admin_views.nurse_update, name='nurse_update'),
    path('nurse_delete/<int:dl>', admin_views.nurse_delete, name='nurse_delete'),

    path('user_view', admin_views.user_view, name='user_view'),
    path('user_update/<int:up>', admin_views.user_update, name='user_update'),
    path('user_delete/<int:dl>', admin_views.user_delete, name='user_delete'),

    path('hospital', admin_views.hospital, name='hospital'),
    path('hospital_view', admin_views.hospital_view, name='hospital_view'),
    path('hospital_update/<int:up>', admin_views.hospital_update, name='hospital_update'),
    path('hospital_delete/<int:dl>', admin_views.hospital_delete, name='hospital_delete'),

    path('vaccine', admin_views.vaccine, name='vaccine'),
    path('vaccine_view', admin_views.vaccine_view, name='vaccine_view'),
    path('vaccine_update/<int:up>', admin_views.vaccine_update, name='vaccine_update'),
    path('vaccine_delete/<int:dl>', admin_views.vaccine_delete, name='vaccine_delete'),

    path('appointment_view', admin_views.appointment_view, name='appointment_view'),
    path('appointment_update/<int:up>', admin_views.appointment_update, name='appointment_update'),
    path('appointment_delete/<int:dl>', admin_views.appointment_delete, name='appointment_delete'),

    path('complaint_view', admin_views.complaint_view, name='complaint_view'),
    path('complaint_update/<int:up>', admin_views.complaint_update, name='complaint_update'),
    path('complaint_delete/<int:dl>', admin_views.complaint_delete, name='complaint_delete'),
    path('complaint_replay/<int:id>', admin_views.complaint_replay, name='complaint_replay'),

    path('book_appointment_view', admin_views.book_appointment_view, name='book_appointment_view'),
    path('approve_appointment/<int:id>', admin_views.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>', admin_views.reject_appointment, name='reject_appointment'),
    path('vaccination_view', admin_views.vaccination_view, name='vaccination_view'),


    path('vaccine_views', nurse_views.vaccine_views, name='vaccine_views'),
    path('user_views', nurse_views.user_views, name='user_views'),
    path('hospital_views', nurse_views.hospital_views, name='hospital_views'),

    path('schedules', nurse_views.schedules, name='schedules'),
    path('schedule_views', nurse_views.schedule_views, name='schedule_views'),
    path('schedule_updates/<int:up>', nurse_views.schedule_updates, name='schedule_updates'),
    path('schedule_deletes/<int:dl>', nurse_views.schedule_deletes, name='schedule_deletes'),

    path('view_book_appointments/', nurse_views.view_book_appointments, name='view_book_appointments'),
    path('vaccination/<int:id>', nurse_views.vaccination, name='vaccination'),

    path('complaints', nurse_views.complaints, name='complaints'),
    path('complaint_views', nurse_views.complaint_views, name='complaint_views'),
    path('complaint_updates/<int:up>', nurse_views.complaint_updates, name='complaint_updates'),
    path('complaint_deletes/<int:dl>', nurse_views.complaint_deletes, name='complaint_deletes'),
    path('complaint_replay_status', nurse_views.complaint_replay_status, name='complaint_replay_status'),

    path('schedule_viewz', user_views.schedule_viewz, name='schedule_viewz'),
    path('book_appointment/<int:id>', user_views.book_appointment, name='book_appointment'),

    path('complaintz', user_views.complaintz, name='complaintz'),
    path('complaint_viewz', user_views.complaint_viewz, name='complaint_viewz'),
    path('complaint_updatez/<int:up>', user_views.complaint_updatez, name='complaint_updatez'),
    path('complaint_deletez/<int:dl>', user_views.complaint_deletez, name='complaint_deletez'),
    path('complaint_status', user_views.complaint_status, name='complaint_status'),

    path('reportcard_viewz', user_views.reportcard_viewz, name='reportcard_viewz'),
    path('profile', user_views.profile, name='profile'),
    path('profile_view', nurse_views.profile_view, name='profile_view'),
    path('profile_updates/<int:up>', nurse_views.profile_updates, name='profile_updates'),
    path('view_appointment', user_views.view_appointment, name='view_appointment'),
    path('profile_update/<int:up>', user_views.profile_update, name='profile_update'),
    path('card/<int:id>', admin_views.card, name='card'),
]
