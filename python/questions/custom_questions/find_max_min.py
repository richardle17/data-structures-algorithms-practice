class Test():

    # Edge case: empty array
    # set min and max to first index, that way we don't need to use "MAX" or "MIN" stuff
    # Iterate through array once
    #   Compare current value to max and min.
    #       update depending on comparison.
    # return max min

    # Time: O(N) iterate through length of array
    # Space: O(1)
    def find_max_min(array):
        if not array:
            return None
        min = array[0]
        max = array[0]
        for x in range(1, len(array)):
            if array[x] > max:
                max = array[x]
            if array[x] < min:
                min = array[x]
        return [min, max]

    def find_max_min_easy(array):
        return [min(array), max(array)]


if __name__ == '__main__':
    input = [4, 7, 109, 34, 86, -34, 12, 4, 8, 94]
    print(Test.find_max_min(input) == [-34, 109])
    print(Test.find_max_min_easy(input) == [-34, 109])

    print(Test.find_max_min([]) is None)