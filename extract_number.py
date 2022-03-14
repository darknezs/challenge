
def convert(str):
    arr = []
    result = 0
    for character in str:
        if character.isdigit():
            arr.append(character)

    for number in range(0, len(arr)):
        if arr[number] == "1":
            result += 1 * (10 ** ((len(arr)-number)-1)   )
        elif arr[number] == "2":
            result += 2 * (10 ** ((len(arr)-number)-1)   )
        elif arr[number] == "3":
            result += 3 * (10 ** ((len(arr)-number)-1)   )
        elif arr[number] == "4":
            result += 4 * (10 ** ((len(arr)-number)-1)   )
        elif arr[number] == "5":
            result += 5 * (10 ** ((len(arr)-number)-1)   )
        elif arr[number] == "6":
            result += 6 * (10 ** ((len(arr)-number)-1)   )
        elif arr[number] == "7":
            result += 7 * (10 ** ((len(arr)-number)-1)   )
        elif arr[number] == "8":
            result += 8 * (10 ** ((len(arr)-number)-1)   )
        elif arr[number] == "9":
            result += 9 * (10 ** ((len(arr)-number)-1)   )
        elif arr[number] == "0":
            result += 0

    return result

a = "aaa103aaa"
print(a)
print(convert(a))
# * 10**len(arr)-1
# print( 10** ((len(arr)-number)-1)   )
