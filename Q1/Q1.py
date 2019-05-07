def check_overlap (A,B):
    # sort the input tupples and assign to respective variables representing their position on x axis
    line1 = sorted(A)
    line2 = sorted(B)

    #assign coordinates of line to the sorted tuples 
    [a0,a1]=line1
    [b0,b1]=line2

    #check if any of line2 coordinates can be found in the range of line1 coordinates
    mirrora = b0 <= a1 and b0 >= a0
    mirrorb = b1 <= a1 and b1 >= a0

    #if line2 coordinates map line 1 coordinates, the two lines overlaps on x axis
    if(mirrora or mirrorb):
        print(True)
        return True
    else:
        print(False)
        return False