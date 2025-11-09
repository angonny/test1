
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged

if __name__ == "__main__":
    import ast
    s = input().strip()
    if not s:
        print("No numbers provided.")
    else:
        try:
            parsed = ast.literal_eval(s)
            if not isinstance(parsed, (list, tuple)):
                raise ValueError("Input must be a list or tuple.")
            nums = [float(x) if isinstance(x, float) else int(x) if isinstance(x, int) else
                    float(x) if isinstance(x, str) and ('.' in x or 'e' in x.lower()) else int(x)
                    for x in parsed]
        except Exception:
            s2 = s.replace(",", " ").replace("[", " ").replace("]", " ")
            try:
                nums = [int(x) for x in s2.split()]
            except ValueError:
                nums = [float(x) for x in s2.split()]
        sorted_nums = merge_sort(nums)
        print(sorted_nums)
