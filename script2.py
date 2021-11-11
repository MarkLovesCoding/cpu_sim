

test_memory = [1,2,3,4,5,2,7,3,5,2,5,2,8]

input_list = []
CACHE_SIZE = 4
cache = ["empty"]* CACHE_SIZE
def add_to_list():
    num = input("Type in number 0 - 9 to add to lists. Type 'D' to finish.\n")
    if num == 'D':
        print("input_list created: ", input_list)
        return input_list
    if (int(num) < 10 and int(num) >= 0):
        input_list.append(num)
        print(num, "added!")
        add_to_list()
    
    else:
        print("Not a number.")
        add_to_list()
  
# new_list = add_to_list()

def add_to_cache(el):
    removed = cache.pop(0)
    print(removed," removed from cache")
    print("Cache:", cache)
    cache.append(el)
    print(el, " added to cache")
    

def check_in_cache(el):
    for i in cache:
        if el == i:
            return True
        else:
            return False
def run_list_through_cache(l):
    for i in l:
        if not check_in_cache(i):
            print(i, "retrieved from memory")
            add_to_cache(i)
        elif check_in_cache(i):
            print(i, "Found in cache" )
            

run_list_through_cache(test_memory)