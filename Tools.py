def split_into_chunks(arr, chunk_size=4):
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]