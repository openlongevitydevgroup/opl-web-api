import json
def parse_submitted_references(data:str, id):
    parsed_data = json.loads(data)
    reference_list = []
    for ref in parsed_data.values():
        ref["submission_id"] = id
        reference_list.append(ref) 

    return reference_list
    
