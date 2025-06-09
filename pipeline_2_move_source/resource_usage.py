
def check_resource_keywords(source_code):
    flags = {}
    keywords = ['has key', 'has store', 'move_from', 'borrow_global', 'delete']
    for k in keywords:
        if k in source_code:
            flags[k] = True
    return flags


