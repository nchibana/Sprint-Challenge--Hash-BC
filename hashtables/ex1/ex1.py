#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    ht2 = HashTable(16)

    for i in range(length):
        if hash_table_retrieve(ht, weights[i]) is None:
            hash_table_insert(ht, weights[i], i)
        else:
            hash_table_insert(ht2, weights[i], i)

    answer = None
    for j in range(length):
        value1 = hash_table_retrieve(ht, limit - weights[j])
        value2 = hash_table_retrieve(ht2, limit - weights[j])
        value3 = hash_table_retrieve(ht, weights[j])
        if value1:
            answer = (max(value1, value3), min(value1, value3))
        elif value2:
            answer = (max(value2, value3), min(value2, value3))
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")