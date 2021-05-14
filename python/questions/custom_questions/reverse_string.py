# Time complexity: O(N * 2). O(N) for iterating through string. O(N) to build output string
# Space O(N). strings are not mutable

def reverse_string(str):
    output = ''
    for character in str:
        output = character + output
    return output


# Time Complexity: O(N) start with last letter, append it to output array. decrement index and then return joined output array
# Space Complexity : O(N)
def reverse_string_array(str):
    index = len(str) - 1
    output_array = []

    for x in range(0, len(str)):
        output_array.append(str[index])
        index -= 1
    return ''.join(output_array)


if __name__ == '__main__':
    # print(reverse_string('hello') == 'olleh')
    # print(reverse_string('dammitimmad') == 'dammitimmad')
    # print(reverse_string('rats') == 'star')

    print(reverse_string_array('rats') == 'star')
    print(reverse_string_array('') == '')

    print('rats'[::-1])