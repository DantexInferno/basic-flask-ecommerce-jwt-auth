from src.orders.entities.order import Order


class ManageOrdersUsecase:

    def __init__(self, orders_repository):
        self.orders_repository = orders_repository

    def get_orders(self):

        return self.orders_repository.get_orders()


    def create_order(self, data):

        data["status"] = "created"

        product = self.orders_repository.product_by_sku(data["product_sku"])
        if product:
            if product.quantity < data["quantity"]:
                raise ValueError(f"Quantity you select exceed current stock.")
            

            update_quantity = {
                "quantity": product.quantity - data["quantity"]
            }

            self.orders_repository.update_product(product.id, update_quantity)
            
            order = Order.from_dict(data)
            order = self.orders_repository.create_order(order)
            
            return order
        else:    
            raise ValueError(f"Product does not exists.")


    def get_order(self, order_id):

        return self.orders_repository.get_order(order_id)


    def update_order(self, order_id, data):

        order = self.get_order(order_id)

        if order:

            if "status" in data:
                message = {
                    "message": "The status of the order with ID {order_id} has change to {data['status']}"
                }

                
            order = self.orders_repository.update_order(order_id, data)

            return order

        else:
            raise ValueError(f"Order of ID {order_id} doesn't exist.")


    def delete_order(self, order_id):

        order = self.get_order(order_id)

        if order:
            
            order = self.orders_repository.hard_delete_order(order_id)

        else:
            raise ValueError(f"Order of ID {order_id} doesn't exist or is already deleted.")
