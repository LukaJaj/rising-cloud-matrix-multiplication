import json
import logging
import numpy as np

def are_matrices_multiplicable(firstMatrix, secondMatrix):
    if len(firstMatrix[0]) != len(secondMatrix):
        return False
    return True

def multiply_matrices(firstMatrix, secondMatrix):
    if not are_matrices_multiplicable(firstMatrix,secondMatrix):
        return None
    result = np.dot(firstMatrix, secondMatrix)
    return result


if __name__ == "__main__":
    with open('request.json', 'r') as req_file:
        request = json.load(req_file)
        try:
            firstMatrix = np.array(request['A'])
            secondMatrix = np.array(request['B'])
        except Exception as Argument:
            logging.exception("json malformed, unable to bin")
        result = multiply_matrices(firstMatrix, secondMatrix)

    with open('response.json', 'w+') as res_file:
        response = {}
        response['app'] = result.tolist()
        json.dump(response, res_file)
