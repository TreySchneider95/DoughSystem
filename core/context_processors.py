def context_processor(request):
    context = {}
    context['company'] = "Dough"
    context['product'] = "Dough"
    return {'VARS': context}