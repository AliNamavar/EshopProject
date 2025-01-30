def split_list(input_list, chunk_size=4):
     return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]