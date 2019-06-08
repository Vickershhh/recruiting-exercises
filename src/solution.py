def InventoryAllocator(order: dict, inventorys: list):
    result = []
    for product in order:
        for obj in inventorys:
            if order[product] > 0 and product in obj["inventory"]:
                min_value = min(order[product], obj["inventory"][product])
                order[product] -= min_value
                obj["inventory"][product] -= min_value
                flag = False
                for x in result:
                    if obj["name"] in x:
                        flag = True
                        if product in x[obj["name"]]:
                            x[obj["name"]][product] += min_value
                        else:
                            x[obj["name"]][product] = min_value
                if not flag:
                    result.append({obj["name"]: {product: min_value}})
                if order[product] == 0:
                    break
        if order[product] > 0:
            return []
    return result
