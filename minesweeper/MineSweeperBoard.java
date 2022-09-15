package minesweeper;


public class MineSweeperBoard {

    /**
     * A constant value representing a covered cell. A covered cell is any cell
     * which does not contains a mine, has not been flagged and has not yet been
     * uncovered.
     */
    public static final int COVERED_CELL = -1;

    /**
     * A constant value representing a a cell that has not been uncovered yet
     * but contains a mine.
     */
    public static final int MINE = -2;

    /**
     * A constant value representing a cell which does not contain a mine but
     * has had a flag placed on it.
     */
    public static final int FLAG = -3;

    /**
     * A constant value representing a cell which contains a mine and has had a
     * flag placed on it.
     */
    public static final int FLAGGED_MINE = -4;

    /**
     * A constant value representing a cell containing a mine that has been
     * uncovered.
     */
    public static final int UNCOVERED_MINE = -5;

    /**
     * A constant value representing the contents of an invalid cell. This value
     * is returned by the getCell method when an invalid cell is specified.
     */
    public static final int INVALID_CELL = -10;

    /**
     * A constant value representing the easiest level of play.
     */
    public static final int BEGINNER_LEVEL = 1;

    /**
     * A constant value representing an intermediate level of play.
     */
    public static final int INTERMEDIATE_LEVEL = 2;

    /**
     * A constant value representing the hardest level of play.
     */
    public static final int EXPERT_LEVEL = 3;


    

    public MineSweeperBoard() {
    }


    public MineSweeperBoard(int level) {
    }


    public int getRows() {
        return 5;
    }


    public int getColumns() {
        return 10;
    }


    public int getNumMines() {
        return -1;
    }


    public int getCell(int row, int col) {
        return -1;
    }


    public int numAdjMines(int row, int col) {
        return -1;
    }


    public void uncoverCell(int row, int col) {
    }

   
    public void flagCell(int row, int col) {
    }


    public void revealBoard() {
    }


    public boolean gameLost() {
        return false;
    }


    public boolean gameWon() {
        return false;
    }
}
