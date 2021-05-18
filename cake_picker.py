import cake


class CakePicker:
    """handles AI task of picking a piece of cake
    """

    def __init__(self, cake):
        self.cake = cake

    def pick(self):
        """pick a piece of cake and return its index
        """
        min_pick = self.cake.prev(self.cake.taken_min)
        max_pick = self.cake.taken_max

        # simple greedy approach - pick bigger piece
        if self.cake.pieces[min_pick] > self.cake.pieces[max_pick]:
            return min_pick
        else:
            return max_pick

    # (b) Implement an algorithm which maximizes the computer player’s guaranteed overall total in each
    # step (as described above). This algorithm should run in polynomial time. [6 points]
    # Hint: Use dynamic programming techniques.

    # Returns list of possible options to pick
    def options(self):
        min_pick = self.cake.prev(self.cake.taken_min)
        max_pick = self.cake.taken_max
        remaining_min = self.cake.pieces[0:min_pick]
        remaining_max = self.cake.pieces[max_pick:]
        remaining_max.reverse()
        remaining = remaining_min + remaining_max
        return remaining

    def dynamic_pick(self):
        # Dynamic approach -  maximizes the computer player’s guaranteed overall total
        # Building the totals matrix
        best_score_matrix = []
        min_pick = self.cake.prev(self.cake.taken_min)
        max_pick = self.cake.taken_max
        # Creates a table of available pieces
        table = [self.options()]
        for current_row in range(1, len(self.options()) - 1):
            new_row = []
            for x in range(len(table[current_row - 1]) - 1):
                new_row.append((table[0][x:x + current_row + 1]))
            table.append(new_row)
        # Fills matrix with 0's
        for x in range(len(self.options()) - 1):
            new_row = []
            for i in range(len(self.options()) - x):
                new_row.append(0)
            best_score_matrix.append(new_row)
        # Matrix of best score paths
        best_score_matrix[0] = table[0]
        for row in range(1, len(table)):
            for col in range(len(table[row])):
                best_score_matrix[row][col] = sum(table[row][col]) - min(best_score_matrix[row - 1][col],
                                                                         best_score_matrix[row - 1][col + 1])
        # Choose the best path
        left = best_score_matrix[-1][0]
        right = best_score_matrix[-1][1]
        print("Best score options: ", best_score_matrix[-1])
        # Find max and return a piece
        best = max(left, right)
        if best == left:
            return min_pick
        if best == right:
            return max_pick

