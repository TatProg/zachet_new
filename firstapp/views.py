from django.shortcuts import render
from .models import Sotrudnik
from .forms import Sotrudnik


def sotrudnik_list(request):
    queryset = Sotrudnik.objects.all()
    return render(request, 'firstapp/sotrudnik_list.html', context={'all_sotrudnik': queryset})

# def sotrudnik_list(request):
#     return render(request, 'firstapp/sotrudnik_list.html', {})
#
#
# def index(request):
#     text = Sotrudnik.objects.all()
#     return render(request, "firstapp/sotrudnik_list.html", {"text": text})
#
#
# def edit(request, id):
#     try:
#         s = Sotrudnik.objects.get(id=id)
#         if request.method == 'POST':
#             s.name_f = request.POST.get('name_f')
#             s.name_i = request.POST.get('name_i')
#             s.name_o = request.POST.get('name_o')
#             s.address = request.POST.get('address')
#             s.birth_date = request.POST('birth_date')
#             s.education = request.POST('education')
#             s.attestat_form = request.POST('attestat_form')
#             s.save()
#             return redirect('sotrudnik_list')
#         # else:
#         #     return render(request, 'firstApp/edit.html', {'student': student})
#     except Sotrudnik.DoesNotExit:
#         return HttpResponseNotFound('Sotrudnik not found')
#
#
# def delete(request, name_f):
#     try:
#         s = Sotrudnik.objects.get(name_f=name_f)
#         s.delete()
#         return redirect('sotrudnik_list.html')
#     except Sotrudnik.DoesNotExist:
#         return HttpResponseNotFound("<h2>Sotrudnik not found</h2>")
