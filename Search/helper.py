from copy import deepcopy

# a recursive function that generates all permutations of the elements of Alist
def permute( Alist, idx=0, Plist = None ):
	if Plist == None:
		Plist = []
	"""Logic inspired by http://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
	"""

	if idx >= len(Alist):
		Plist.append( Alist )

	for s in range( idx, len(Alist) ):
		newList = deepcopy( Alist )
		newList[idx], newList[s] = newList[s], newList[idx]
		permute( newList, idx+1, Plist )
	return Plist

# This flattens a singly nested list  [[1], [2], [3]] -> [1, 2, 3]
def flatten( Alist ):
	z = []
	for el in Alist:
		z.extend(el)
	return z


def makeBoxes(Alist, bRows, bCols):
    # Alist is list of lists of rows in nxn puzzle
    # brows, bcols are dimensions of inner box (e.g. 6x6 puzzle is made of 6 2x3 boxes, so makeBoxes(Alist,2,3)
    # This composes the inner boxes, numbering from top to bottom, left to right.
    # For example 6x6 = | box 0 | box 2 |
    #                   | box 1 | box 3 |

    puzzleSize = len(Alist)
    boxesAcrossCols = puzzleSize // bCols
    boxesDownRows = puzzleSize // bRows
    boxesTotal = boxesAcrossCols * boxesDownRows

    boxes = [ [] for b in range( boxesTotal )]
    for b in range( boxesTotal ):
        # Take all relevant column values from the bRows relevant to box "b"
        # For example, box 3 from above is composed of rows 2,3 and cols 2,3
        for row in range( b%boxesDownRows*bRows, b%boxesDownRows*bRows+bRows ):
            boxes[b].extend( Alist[row][b//boxesDownRows*bCols : b//boxesDownRows*bCols+bCols] )
    return boxes



