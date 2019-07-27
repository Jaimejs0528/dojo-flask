def encode_document(data):
    if isinstance(data, list):
        for item in data:
            item['_id'] = str(item['_id'])
    elif isinstance(data, dict):
        data['_id'] = str('_id')

    return data