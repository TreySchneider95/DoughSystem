def context_processor(request):
    context = {}
    context['company'] = "Dough"            
    return {'VARS': context}