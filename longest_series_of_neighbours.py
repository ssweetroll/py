def longest_series_of_neighbours(list : list):
    i = 0
    n = 1
    checklist = []
    while i < len(list):
        
        while list[i] + 1 == list[i+1] or list[i] - 1 == list[i+1]:
            n +=1
            i +=1
            if i+1 == len(list):
                break
        
        checklist.append(n)
        i += 1
        n = 1
    
    checklist.sort()
    return checklist[-1]

my_list = [1, 2, 3, 4, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours (my_list))