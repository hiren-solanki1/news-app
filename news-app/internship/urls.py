from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="indexfile"),
    path('aboutus',views.about,name="aboutusfile"),
    path('sports',views.sports,name="sportsfile"),
    path('entertainment',views.entertainment,name="entertainmentfile"),
    path('business',views.business,name="businessfile"),
    path('national',views.national,name="nationalfile"),
    path('world',views.world,name="worldfile"),
    path('politics',views.politics,name="politicsfile"),
    path('technology',views.technology,name="technologyfile"),
    path('startup',views.startup,name="startupfile"),
    path('science',views.science,name="sciencefile"),
    path('miscellaneous',views.miscellaneous,name="miscellaneousfile"),
    path('hatke',views.hatke,name="hatkefile"),
    path('automobile',views.automobile,name="automobilefile"),
]