from django.shortcuts import render, redirect
from django.views.generic import View
from .models import InventoryRaw, Unit, Purchase
from .utils import Convert



# Create your views here.

class DoughView(View):
    def get(self, request):
        return render(request, 'manageDough/doughs.html')
    

class MakePurchases(View):
    def get(self, request):
        context = {}
        context["units"] = Unit.objects.all()
        context["products"] = InventoryRaw.objects.all()
        return render(request, 'manageDough/make_purchases.html', {'context':context})
    
    def post(self, request):
        if request.POST['product'] != 'null':
            product = InventoryRaw.objects.get(pk = int(request.POST['product']))
        date_purchased = request.POST['date']
        price = request.POST['price']
        where = request.POST['where']
        qty = int(request.POST['qty'])
        unit = Unit.objects.get(pk = int(request.POST['unit']))
        product_name = request.POST['product_name']
        if request.POST.get('default_unit', None):
            default_unit = Unit.objects.get(pk = int(request.POST['default_unit']))
        refrigerated = True if request.POST.get('refrigerated', False) else False
        # print(f'product:{product}, date:{date_purchased}, price:{price}, where:{where}, qty:{qty}, unit:{unit}, refrigerated:{refrigerated}, product_name:{product_name}')
        if product_name:
            product = InventoryRaw(name=product_name, unit_used=default_unit)
            product.save()
        new_purchase = Purchase(date_purchased=date_purchased, price=price, where=where, product=product, qty_purchased=qty, qty_left=qty, refrigerated=refrigerated, unit=unit, person_who_purchased=request.user)
        if product.unit_used != unit:
            conversion = Convert(unit, qty, product.unit_used).convert()
            product.qty += conversion
        else:
            product.qty += qty
        product.save()
        new_purchase.save()
        if "another" in request.POST:
            return redirect('make_purchases')
        return redirect('manage_doughs')
    
class ManageRawInventory(View):
    def get(self, request):
        products = InventoryRaw.objects.filter(qty__gt = 0)
        for product in products:
            active_purchases = Purchase.objects.filter(qty_left__gt = 0, product = product.pk)
            if active_purchases:
                total_purchased = sum([purchase.qty_purchased for purchase in active_purchases])
                total_left = sum([purchase.qty_left for purchase in active_purchases])
                product.total_purchased = total_purchased
                product.total_left = total_left
                product.total_percent = (total_left/total_purchased) * 100
        return render(request, 'manageDough/manage_raw_inventory.html', {'products': products})