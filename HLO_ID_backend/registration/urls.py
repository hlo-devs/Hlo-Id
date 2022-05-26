from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name="index"),
    path("index",views.index,name="ind"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("privacy",views.privacy,name="privacy"),
    path("terms",views.terms,name="terms"),
    path("sign_up_myself",views.sign_up_myself,name="sign_up_myself"),
    path("sign_up_org",views.sign_up_org,name="sign_up_org"),
    path("form1",views.form1,name="form1"),
    path("s_ms_f2",views.s_ms_f2,name="s_ms_f2")
]
