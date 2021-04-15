from .models import Category

def menu_link(request):
    link=Category.objects.all()
    return dict(link=link)
#
# def doctor_link(request):
#     doc=Doctor.objects.all()
#     return dict(doc=doc)