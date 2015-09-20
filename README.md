# zipfs-paperclips
The paperclip experiment from the Vsauce video "The Zipf Mystery", written in python

Choose how many paperclips and how many linking iterations to run in args.

Does not do any stats yet, but will generate chains and print each iteration.

Run

    python paperclips.py <number of paperclips> <iterations>
    
Example

    $python paperclips.py 8 4
    
    Got 6 and 3
    New chain : 6 3
    0 : 0
    1 : 1
    2 : 2
    3 : 6 3
    4 : 4
    5 : 5
    6 : 6 3
    7 : 7
    
    Got 1 and 5
    New chain : 1 5
    0 : 0
    1 : 1 5
    2 : 2
    3 : 6 3
    4 : 4
    5 : 1 5
    6 : 6 3
    7 : 7

    Got 6 and 2
    New chain : 6 3 2
    0 : 0
    1 : 1 5
    2 : 6 3 2
    3 : 6 3 2
    4 : 4
    5 : 1 5
    6 : 6 3 2
    7 : 7
    
    Got 7 and 6
    New chain : 7 6 3 2
    0 : 0
    1 : 1 5
    2 : 7 6 3 2
    3 : 7 6 3 2
    4 : 4
    5 : 1 5
    6 : 7 6 3 2
    7 : 7 6 3 2
