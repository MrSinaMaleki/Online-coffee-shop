from product.models import Category


def link_creator(request, path):
    return "#" if request.path == path else path


def get_subcategories(category, request):
    subcategories = []
    if category.subcategories.exists():
        for sub in category.subcategories.all():
            subcategories.append({
                'title': sub.title,
                'link': link_creator(request, f"/shop/products/category/{sub.id}")
            })
    return subcategories


def menu_context_processor(request):
    my_list = [
        dict(title="Home", link=link_creator(request, "/shop/products/")),
        dict(title="About Us", link=link_creator(request, "/shop/about/")),
        dict(title="All Foods", link=link_creator(request, "/shop/products/"))
    ]

    categories = Category.objects.filter(parent__isnull=True)

    for cat in categories:
        subcategories = get_subcategories(cat, request)
        my_list.append({
            'title': cat.title,
            'link': link_creator(request, f"/shop/products/category/{cat.id}"),
            'subcategories': subcategories
        })

    return {
        'menu': my_list
    }

# change paths!!!!!!!!!!!!!!!

