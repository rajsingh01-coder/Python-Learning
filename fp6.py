#Write a python function to remove duplicates from a dictionary
#data = [{"id": 1, "name": "Alice"},  {"id": 2, "name": "Bob"},{"id": 1, "name": "Charlie"}, {"id": 3, "name": "Alice"} ]
def remove_duplicates(data):
    seen_ids = set()   #ye check karata hai ki id pehle se hai ya nhi
    unque_data = []    #ye unique data ko store karnta hai konse id pehle se nhi hai
    for item in data:
        if item["id"] not in seen_ids:
            unque_data.append(item)
            seen_ids.add(item["id"])    
    return unque_data
print(remove_duplicates([{"id": 1, "name": "Alice"}, 
                          {"id": 2, "name": "Bob"},
                          {"id": 1, "name": "Charlie"},
                          {"id": 3, "name": "Alice"} 
                        ]))