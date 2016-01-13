""" Problem 67.py: Maximum Path Sum 2

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

                            (3)
                          (7)  4
                         2  (4)  6
                       8   5  (9)  3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in p067_triangle.txt, a 15K text file
containing a triangle with one-hundred rows.
"""

with open("../EulerFiles/p067_triangle.txt", "r") as triangle_file:
    triangle_string = triangle_file.read()

process_data = lambda triangle_row: list(map( int, triangle_row.split() ))
triangle = list(map( process_data, triangle_string.split('\n') ))
triangle.pop()

for row in range( len(triangle) - 1 ):
    top_row    = triangle[-2]
    bottom_row = triangle[-1]

    for i in range( len(top_row) ):
        left_sum  = top_row[i] + bottom_row[i]
        right_sum = top_row[i] + bottom_row[i+1]
        biggest_sum = max( left_sum, right_sum )

        top_row[i] =  biggest_sum

    triangle[-2] =  top_row
    triangle.remove(bottom_row)

print( "The maximum path sum of the triangle is: %d" % triangle[0][0] )
