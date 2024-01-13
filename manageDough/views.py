from django.shortcuts import render, redirect
from django.views.generic import View
from .models import InventoryRaw, Unit, Purchase
from pint import UnitRegistry


ureg = UnitRegistry(system="US")

print(ureg.get_compatible_units("pounds"))

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
        print('here')
        if request.POST['product'] != 'null':
            product = InventoryRaw.objects.get(pk = int(request.POST['product']))
        date_purchased = request.POST['date']
        price = request.POST['price']
        where = request.POST['where']
        qty = int(request.POST['qty'])
        unit = Unit.objects.get(pk = int(request.POST['unit']))
        product_name = request.POST['product_name']
        refrigerated = True if request.POST.get('refrigerated', False) else False
        # print(f'product:{product}, date:{date_purchased}, price:{price}, where:{where}, qty:{qty}, unit:{unit}, refrigerated:{refrigerated}, product_name:{product_name}')
        if product_name:
            product = InventoryRaw(name=product_name, unit_used=unit)
            product.save()
        new_purchase = Purchase(date_purchased=date_purchased, price=price, where=where, product=product, qty_purchased=qty, qty_left=qty, refrigerated=refrigerated, unit=unit, person_who_purchased=request.user)
        if product.unit_used != unit:
            # new_qty = qty * ureg(unit.unit.lower())
        
            # new_qty.to(f'{product.unit_used.unit.lower()}s')
            # print(new_qty)
            pass
        # product.qty += qty
        # product.save()
        # new_purchase.save()
        return redirect('make_purchases')