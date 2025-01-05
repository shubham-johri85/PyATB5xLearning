my_tuple = (1, 4, 9, 16, 25)

# my_tuple[3] = 64 - 'tuple' object does not support item assignment
print(my_tuple)
print("-----------------")

my_tuple2=("tta.com", "sdet.live")
print(len(my_tuple2))
my_api_list = list(my_tuple2)  # converted tuple into list so that it can be mutable
print(my_api_list)
my_api_list.append("tmna.com")
print(my_api_list)

"""
In real case example we use tuple where we store our urls for API testing which will not change.
"""
API_URL= ("http://www.company1.com", "http://www.company2.com", "http://www.company3.com" )
print(API_URL[2])
print(API_URL[0])



