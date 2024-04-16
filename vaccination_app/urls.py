from django.urls import path
from . import views,admin_views,cust_views,nur_views


urlpatterns= [
    path('', views.index, name='index'),
    path('cust_reg', views.cust_reg, name='cust_reg'),
    path('nurse_reg', views.nurse_reg, name='nurse_reg'),
    path('log', views.login_view, name='login'),
    path('logout',views.logout1,name='logout'),







    path('admin_log', admin_views.admin_log, name='admin_log'),
    path('hospital', admin_views.create, name='hospital'),
    path('view', admin_views.view, name='view'),
    path('img_update/<int:id>', admin_views.hos_update, name='hos_update'),
    path('img_delete/<int:dl>', admin_views.hos_delete, name='hos_delete'),
    path('vaccine',admin_views.create1,name='vaccine'),
    path('view1',admin_views.view1,name='view1'),
    path('vacc_update/<int:id>',admin_views.vacc_update,name='vacc_update'),
    path('vacc_delete/<int:dl>',admin_views.vacc_delete,name='vacc_delete'),
    path('cust_view',admin_views.cust_view,name='cust_view'),
    path('cust_update/<int:id>',admin_views.cust_update,name='cust_update'),
    path('cust_delete/<int:dl>',admin_views.cust_delete,name='cust_delete'),
    path('nur_view',admin_views.nur_view,name='nur_view'),
    path('nur_update/<int:id>',admin_views.nur_update,name='nur_update'),
    path('nur_delete/<int:dl>',admin_views.nur_delete,name='nur_delete'),
    path('reply',admin_views.reply,name='reply'),
    path('reply1/<int:id>',admin_views.admin_reply,name='reply1'),
    path('appo_view',admin_views.appointment_view,name='appo_view'),
    path('approve/<int:id>',admin_views.approve,name='approve'),
    path('reject/<int:id>',admin_views.reject,name='reject'),




    path('cust_log', cust_views.cust_log, name='cust_log'),
    path('cmplt_add',cust_views.complaint_add,name='cmplt_add'),
    path('cmplt_view',cust_views.complaint_view,name='cmplt_view'),
    path('cmplt_update/<int:id>',cust_views.complaint_update,name='cmplt_update'),
    path('cmplt_delete/<int:dl>',cust_views.complaint_delete,name='cmplt_delete'),
    path('sched_view',cust_views.schedule_view1,name='sched_view'),
    path('book/<int:id>',cust_views.book_appointment,name='book'),
    path('appo_view1',cust_views.appointment_view1,name='appo_view1'),




    path('nurse_log', nur_views.nurse_log, name='nurse_log'),
    path('cmplt_add1',nur_views.nurcomplaint_add,name='cmplt_add1'),
    path('cmplt_view1',nur_views.nurcomplaint_view,name='cmplt_view1'),
    path('cmplt_update1/<int:id>',nur_views.nurcomplaint_update,name='cmplt_update1'),
    path('cmplt_delete1/<int:dl>',nur_views.nurcomplaint_delete,name='cmplt_delete1'),
    path('schedule',nur_views.schedule,name='schedule'),
    path('sche_view',nur_views.schedule_view,name='sche_view'),
    path('sche_update/<int:id>',nur_views.schedule_update,name='sche_update'),
    path('sche_delete/<int:dl>',nur_views.schedule_delete,name='sche_delete'),






    

]

