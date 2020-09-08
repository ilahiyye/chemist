class CompanySerializer:
    def __init__(self, company):
        self.company = company


    def to_dict(self):
        # company_name, origin_country = self.company.name.split(", ")
        return {
          'uuid': str(self.company.uuid),
          'name': self.company.name,
          'list_items': f'http://localhost:8000/inventory/companies/{self.company.uuid}'
        }


    def to_xml(self):
        pass

class ItemSerializer:
    def __init__(self, item):
        self.item = item


    def to_dict(self):
        return {
          'uuid': str(self.item.uuid),
          'name': self.item.name,
          'ingredient_uuid': str(self.item.ingredient_uuid_id),
          'dosage': f'{self.item.dosage_qty} {self.item.dosage_unit}',
          'wholesale_price': self.item.wholesale_price,
          'sale_price': self.item.sale_price
        }
class ItemSerializer:
    def __init__(self, item):
        self.item = item


    def to_dict(self):
        return {
          'uuid': str(self.item.uuid),
          'name': self.item.name,
          'ingredient_uuid': str(self.item.ingredient_uuid_id),
          'dosage': f'{self.item.dosage_qty} {self.item.dosage_unit}',
          'wholesale_price': self.item.wholesale_price,
          'sale_price': self.item.sale_price
        }
#################################################################
class IngredientSerializer:
    def __init__(self, ingredient):
        self.ingredient = ingredient


    def to_dict(self):
        return {
        'uuid': str(self.ingredient.uuid),
        'name': self.ingredient.name,
        'list_items': f'http://localhost:8000/inventory/ingredients/{self.ingredient.uuid}'
        }

class PackagingSerializer:
    def __init__(self, packaging):
        self.packaging = packaging

    def to_dict(self):
        return{
            'uuid': str(self.packaging.uuid),
            'name': self.packaging.name,
        }

class PharmaceuticalFormSerializer:
    def __init__(self, pharm):
        self.pharm = pharm

    def to_dict(self):
        return{
            'uuid': str(self.pharm.uuid),
            'name': self.pharm.name,
        }


