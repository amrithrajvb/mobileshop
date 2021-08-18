from django.urls import path

from owner import views
urlpatterns=[
    path("",views.home),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("phones/items",views.items,name="items"),
    path("phones/addphone",views.addmobile,name="addphone"),
    path("phones/viewphones",views.viewphone,name="viewphones"),
    path("phones/change/<int:id>",views.changephone,name="changephone"),
    path("phones/remove/<int:id>",views.removephone,name="removephone")
]