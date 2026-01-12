// Last updated: 1/12/2026, 3:12:48 PM
class Spreadsheet {
    Map<Integer, Map<Integer, Integer>> grid = new HashMap<>();

    public record Pair<K, V>(K first, V second) {}

    public Spreadsheet(int rows) {
        for(int i = 0; i < 26; i++) {
            grid.put(i, new HashMap<>());
        }
    }

    Pair<Integer, Integer> getColRow(String cell) {
        char col = cell.charAt(0);
        int colInteger = col - 'A';
        int row = Integer.parseInt(cell.substring(1));

        return new Pair<>(colInteger, row);
    }
    
    public void setCell(String cell, int value) {
        Pair<Integer, Integer> colRow = getColRow(cell);
        grid.get(colRow.first()).put(colRow.second(), value);
    }
    
    public void resetCell(String cell) {
        Pair<Integer, Integer> colRow = getColRow(cell);
        grid.get(colRow.first()).put(colRow.second(), 0);
    }
    
    public int getValue(String formula) {
        int additionIdx = formula.indexOf('+');
        String left = formula.substring(1, additionIdx);
        String right = formula.substring(additionIdx + 1);

        int leftValue = 0;
        if(left.charAt(0) >= 'A' && left.charAt(0) <= 'Z') {
            Pair<Integer, Integer> colRow = getColRow(left);
            if(grid.get(colRow.first()) == null || grid.get(colRow.first()).get(colRow.second()) == null) {
                leftValue = 0;
            } else {
                leftValue = grid.get(colRow.first()).get(colRow.second());
            }
        } else {
            leftValue = Integer.parseInt(left);
        }

        int rightValue = 0;
        if(right.charAt(0) >= 'A' && right.charAt(0) <= 'Z') {
            Pair<Integer, Integer> colRow = getColRow(right);
            if(grid.get(colRow.first()) == null || grid.get(colRow.first()).get(colRow.second()) == null) {
                rightValue = 0;
            } else {
                rightValue = grid.get(colRow.first()).get(colRow.second());
            }
        } else {
            rightValue = Integer.parseInt(right);
        }

        return leftValue + rightValue;
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */