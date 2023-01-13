class game_of_life:
    def gameOfLife(self, board:List[List[int]]) -> None:

        neighbors = array[]

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col = neighbor[1])

    