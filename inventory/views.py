from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


from inventory.models import *
from inventory.serializers import IngredientSerializer, ItemSerializer, CompanySerializer, PackagingSerializer, PharmaceuticalFormSerializer


# def index(request):
#     companies = Company.objects.all()
#     l = len(companies)
#     names = " ".join([c.name for c in companies])
#     locs = " ".join([c.country for c in companies])
#     return HttpResponse(f"Hello, world: There are {l} companies in the database. <br/>\
#       they are  {names}<br />\
#       and they are based in {locs}</br>")



def index(request):
    api_index = {
      'companies': 'http://localhost:8000/inventory/companies',
      'ingredients': 'http://localhost:8000/inventory/ingredients',
      'items': 'http://localhost:8000/inventory/items',
      'packagings': 'http://localhost:8000/inventory/packagings',

    }
    return JsonResponse(api_index)

def companies_listing(request):
    companies = Company.objects.all()[:40]
    response = [CompanySerializer(company).to_dict() for company in companies]
    return JsonResponse(response, safe=False)

def company_items_listing(request, uuid=None):
    company = Company.objects.get(uuid = uuid)
    items = Item.objects.filter(company_uuid_id = uuid)
    print(company)


    response = {
      'company': CompanySerializer(company).to_dict(),
      'number_of_items': len(items),
      'items': [ItemSerializer(item).to_dict() for item in items]
    }
    return JsonResponse(response, safe=False)

##################################################################

def items_listing(request):
  items = Item.objects.all()[:40]
  response = [ItemSerializer(item).to_dict() for item in items]
  return JsonResponse(response, safe=False)

def ingredients_listing(request):
  ingredients = Ingredient.objects.all()[:40]
  response = [IngredientSerializer(ingredient).to_dict() for ingredient in ingredients]
  return JsonResponse(response, safe=False)

def packaging_listing(request):
  packagings = Packaging.objects.all()[:40]
  response = [PackagingSerializer(packaging).to_dict() for packaging in packagings]
  return JsonResponse(response, safe=False)

def ingridient_items_listing(request, uuid=None):
    ingredient = Ingredient.objects.get(uuid = uuid)
    items = Item.objects.filter(ingredient_uuid = uuid)
    print(ingredient)
   

    response = {
      'Ingredients': IngredientSerializer(ingredient).to_dict(),
      'number_of_ingredients': len(items),
      'Items': [ItemSerializer(item).to_dict() for item in items],
      
    }
    return JsonResponse(response, safe=False)

