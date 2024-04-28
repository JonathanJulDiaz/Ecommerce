from django.conf import settings

from posts.models import Product

class Saved(object):
    def __init__(self, request):
        self.session = request.session
        saved = self.session.get(settings.SAVED_SESSION_ID)

        if not saved:
            saved = self.session[settings.SAVED_SESSION_ID] = {}
        
        self.saved = saved
        
    def __iter__(self):
        for p in self.saved.keys():
            self.saved[str(p)]['product'] = Product.objects.get(pk=p)
        
        for item in self.saved.values():
            item['total_price'] = int(item['product'].precio * item['quantity']) / 100

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.saved.values())
    
    def save(self):
        self.session[settings.SAVED_SESSION_ID] = self.saved
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.saved:
            self.saved[product_id] = {'quantity': int(quantity), 'id': product_id}
        
        if update_quantity:
            self.saved[product_id]['quantity'] += int(quantity)
            
            if self.saved[product_id]['quantity'] == 0:
                self.remove(product_id)
        
        self.save()

    def remove(self, product_id):
        if product_id in self.saved:
            del self.saved[product_id]

            self.save()