""" Problem 18.py: Maximum Path Sum 1

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

                            (3)
                          (7)  4
                         2  (4)  6
                       8   5  (9)  3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""

triangle_string = (
"                             75\n"
"                           95  64\n"
"                         17  47  82\n"
"                       18  35  87  10\n"
"                     20  04  82  47  65\n"
"                   19  01  23  75  03  34\n"
"                 88  02  77  73  07  63  67\n"
"               99  65  04  28  06  16  70  92\n"
"             41  41  26  56  83  40  80  70  33\n"
"           41  48  72  33  47  32  37  16  94  29\n"
"         53  71  44  65  25  43  91  52  97  51  14\n"
"       70  11  33  28  77  73  17  78  39  68  17  57\n"
"     91  71  52  38  17  14  91  43  58  50  27  29  48\n"
"   63  66  04  68  89  53  67  30  73  16  69  87  40  31\n"
" 04  62  98  27  23  09  70  98  73  93  38  53  60  04  23  ")
print(triangle_string)

process_data = lambda triangle_row: list(map( int, triangle_row.split() ))
triangle = list(map( process_data, triangle_string.split('\n') ))

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

print( "\n\tThe maximum path sum of the triangle is: %d" % triangle[0][0] )


