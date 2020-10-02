import math

sale_prices = [100, 83, 220, 40, 100, 400, 10, 1, 3,]

# My solution odd

# def median_finder(list_name) :
#     sorted_list = sorted(list_name)
#     x = math.floor(len(sorted_list) / 2)
#     print(sorted_list[x])
    
# median_finder(sale_prices)

# My solution even



# jordans solution

# sorted_list = sorted(sale_prices)
# num_of_sales = len(sorted_list)
# half_slice = math.floor(num_of_sales / 2)
# first_sales_items = sorted_list[:half_slice]
# last_sales_items = sorted_list[-(half_slice):]
# median = sorted_list[math.floor(half_slice):(math.floor(half_slice) + 1)]

# print(sorted_list)
# print(num_of_sales)
# print(first_sales_items)
# print(last_sales_items)
# print(median)