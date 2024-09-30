from product.models import Category


def link_creator(request, path):
    return "#" if request.path == path else path


def get_subcategories(category, request):
    subcategories = []
    if category.subcategories.exists():
        for sub in category.subcategories.all():
            subcategories.append({
                'title': sub.title,
                'link': link_creator(request, f"/product/category/{sub.id}"),
                'subcategories': get_subcategories(sub, request)
            })
    return subcategories


def menu_context_processor(request):
    my_list = [
        dict(title="Home", link=link_creator(request, "/shop/products/")),
        dict(title="About Us", link=link_creator(request, "/pages/about-us")),
        dict(title="All Foods", link=link_creator(request, "/product/products")),
        dict(title="Coffee Shop", link=link_creator(request, "/product/coffeeshop/")),
        dict(
            title="Restaurant",
            link=link_creator(request, "#"),
            subcategories=[
                dict(title="Breakfast", link=link_creator(request, "/product/restaurant/Breakfast")),
                dict(title="Lunch", link=link_creator(request, "/product/restaurant?time=Lunch")),
                dict(title="Dinner", link=link_creator(request, "/product/restaurant?time=Dinner"))
            ]
        )
    ]

    categories = Category.objects.filter(parent__isnull=True)

    category_menu = dict(
        title="Category",
        link=link_creator(request, "#"),
        subcategories=[]
    )

    for cat in categories:
        category_menu['subcategories'].append({
            'title': cat.title,
            'link': link_creator(request, f"/product/category/{cat.id}"),
            'subcategories': get_subcategories(cat, request)
        })

    my_list.append(category_menu)

    return {
        'menu': my_list
    }

