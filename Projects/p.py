import json

# people_string = '''
# {
#     "people": [
#         {
#             "name": "John Smith",
#             "phone": "615-555-7164",
#             "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
#             "has_license": false
#         },
#         {
#             "name": "Jane Doe",
#             "phone": "560-555-5153",
#             "emails": null,
#             "has_license": true
#         }
#     ]
# }
# '''

# data=json.loads(people_string)
# # print(data)

# new_string=json.dumps(data,indent=1, sort_keys=True)
# print(new_string)



with open('Projects\\one.json') as f1:
    data=json.load(f1)
for state in data:
    print(state)