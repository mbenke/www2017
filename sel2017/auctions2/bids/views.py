from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from bids.models import Bid
from django.http import HttpResponse

@ensure_csrf_cookie
def showAuction(request):
    bid = get_object_or_404(Bid, pk=1)
    return render(request, 'auction.html', locals())
 
@require_POST
def ajaxBid(request):
    bid = get_object_or_404(Bid, pk=1)
    newPrice = int(request.POST['price'])
    if newPrice > bid.price:
        bid.price = newPrice
        bid.save()
    return HttpResponse(bid.price)
