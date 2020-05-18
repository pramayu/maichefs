import graphene as grap
from app.api.service.foodbasket.build_basket import BuildFoodBasket
from app.api.service.foodbasket.pushfoodbasket import PushFoodBasket
from app.api.service.foodbasket.pushfoodbasket import UpdateQuantiti
from app.api.service.foodbasket.pushfoodbasket import PullFooditem
from app.api.service.foodbasket.pushfoodbasket import PullFoodchef

class BasketServ(grap.ObjectType):
	pushfoodbasket 			= PushFoodBasket.Field()
	updatequantiti 			= UpdateQuantiti.Field()
	pullfooditem 			= PullFooditem.Field()
	pullfoodchef 			= PullFoodchef.Field()
	buildfoodbasket 		= BuildFoodBasket.Field()