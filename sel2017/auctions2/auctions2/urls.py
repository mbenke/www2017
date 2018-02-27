from django.conf.urls import include, url
from django.contrib import admin
import bids.views
urlpatterns = [
    # website
    url(r'^$', bids.views.showAuction),
    url(r'^admin/', include(admin.site.urls)),
    
    # ajax
    url(r'^ajax/bid/', bids.views.ajaxBid),
]
