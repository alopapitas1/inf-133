def render_store_list(stores):
    return[
        {
            "id":store.id,
            "name":store.name,
            "description":store.description,
            "price":store.price,
            "stock":store.stock
        }
        for store in stores
    ]
    
def render_store_detail(store):
    return [
        {
            "id":store.id,
            "name":store.name,
            "description":store.description,
            "price":store.price,
            "stock":store.stock
        }
    ]

