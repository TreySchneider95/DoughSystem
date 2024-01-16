from .models import Calcs

class Convert():

    def __init__(self, one_to_convert, convert_qty, base):
        self.base = base
        self.one_to_convert = one_to_convert
        self.convert_qty = convert_qty

    def convert(self):
        calc = Calcs.objects.get(one_to_convert = self.one_to_convert.pk, base = self.base.pk).conversion
        
        return self.convert_qty * calc
