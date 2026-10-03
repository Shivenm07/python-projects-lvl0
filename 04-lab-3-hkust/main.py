# tuple[str, int, float, str, int, float] is a type hint for the return values.
def task1() -> tuple[str, int, float, str, int, float]:
    product1_name: str = input("Enter the name of the first product: ")
    product1_qty: int = input("Enter the initial quantity ordered of the first product: ")
    product1_cost: float = input("Enter the cost of the first product: ")
    product2_name: str = input("Enter the name of the second product: ")
    product2_qty: int = input("Enter the initial quantity ordered of the second product: ")
    product2_cost: float = input("Enter the cost of the second product: ")

    return product1_name, product1_qty, product1_cost, product2_name, product2_qty, product2_cost

products = task1()

def task2(qty: int, cost: float) -> float:
    item_cost = int(qty)*int(cost)
    return item_cost

def task3(product1_qty: int = products[1], product1_cost: float = products[2], product2_qty: int = products[4], product2_cost: float = products[5]) -> float:
    total_cost = task2(product1_qty, product1_cost) + task2(product2_qty, product2_cost)
    return total_cost

def task4(product1_name: str = products[0], product1_qty: int = products[1], product1_cost: float = products[2],
          product2_name: str = products[3], product2_qty: int = products[4], product2_cost: float = products[5], total_cost = task3()) -> float:

        print(f"Number of {product1_name} bought: {product1_qty}")
        print(f"Cost of {product1_name}: ${product1_cost}")
        print(f"Number of {product2_name} bought: {product2_qty}")
        print(f"Cost of {product2_name}: ${product2_cost}")
        print(f"Total cost: ${total_cost}")

if __name__ == "__main__":
    task4()