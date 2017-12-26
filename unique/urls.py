from django.conf.urls import *
import views


urlpatterns = [

    url(r'^$', views.home),
    url(r'^home/', views.home),
    url(r'^about-us/',views.aboutus),
    url(r'^contact-us/',views.contactus),
    url(r'^our-services/',views.services),
    url(r'^our-portfolio/',views.portfolio),

    #Services url

    url(r'^land-surveys/',views.land_surveys),
    url(r'^topographical-surveys/',views.topographical_surveys),
    url(r'^physical-surveys/',views.physical_surveys),
    url(r'^alignment-surveys/',views.alignment_surveys),
    url(r'^building-surveys/',views.building_surveys),
    url(r'^quantity-surveys/',views.quantity_surveys),
    url(r'^demarcation-surveys/',views.demarcation_surveys),
    url(r'^road-surveys/',views.road_surveys),
    url(r'^digitization/',views.digitization),
    url(r'^architecture/',views.Architechture),
    url(r'^our-clients/',views.clients),

]
