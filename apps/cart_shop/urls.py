from django.urls import path
from .views import ViewCart, ViewWishlist, ViewCartBuy, ViewCartDel, ViewCartAdd, AddInWishList, WishListDel

app_name = 'cart_shop'

urlpatterns = [
    path('', ViewCart.as_view(), name='cart'),
    path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
    path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
    path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
    path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
    path('wish/<int:product_id>', AddInWishList.as_view(), name='wish'),
    path('delwish/<int:item_id>', WishListDel.as_view(), name='del_from_wish'),

]