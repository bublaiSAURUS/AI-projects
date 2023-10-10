import java.util.ArrayList;

/**
 * Solution code for Comp24011 Reversi lab
 *
 * @author USERNAME
 */

public class AlphaBetaMoveChooser extends MoveChooser {
    /**
     * MoveCooser implementation AlphaBetaMoveChooser(int)
     *
     * @param   searchDepth The requested depth for minimax search
     */
    public AlphaBetaMoveChooser(int searchDepth) {
        // Add object initialisation code...
        super("MyAwesomeAgent",searchDepth);
    }

    /**
     * Need to implement chooseMove(BoardState,Move)
     *
     * @param   boardState  The current state of the game board
     *
     * @param   hint        Skip move or board location clicked on the UI
     *                      This parameter should be ignored!
     *
     * @return  The move chosen by alpha-beta pruning as discussed in the course
     */
    public Move chooseMove(BoardState boardState, Move hint) {
        // Add alpha-beta pruning code...
        Move ans= null;
        int optimum = Integer.MIN_VALUE;

        int alpha = Integer.MIN_VALUE;
        int beta = Integer.MAX_VALUE;
        //int bestVal = Max(boardState,Integer.MIN_VALUE, Integer.MAX_VALUE,this.searchDepth);
        ArrayList<Move> legalMoves = boardState.getLegalMoves();
        for(int i = 0; i<legalMoves.size(); i++)
        {
            Move a = legalMoves.get(i);
            BoardState b = boardState.deepCopy();
            b.makeLegalMove(a);
            int h = Min(b, alpha, beta, this.searchDepth-1);
            if (h>optimum)
            {
                optimum = h;
                System.out.println(optimum);
                ans = a;
            }
            alpha = Math.max(alpha, optimum);
            if (alpha >= beta) 
            {
                break;
            }
        }
        //System.out.println(optimum); 
        return ans;
    }

    private int Max(BoardState b, int alpha, int beta, int depth) 
    {
        if (b.gameOver() || depth == 0)
        {
            int k = boardEval(b);
            //System.out.println(k);
            return (k);
        }
        int m = Integer.MIN_VALUE;
        ArrayList<Move> lM = b.getLegalMoves();
        for(int i = 0; i<lM.size(); i++)
        {
            BoardState b1 = b.deepCopy();
            b1.makeLegalMove(lM.get(i));
            int v = Min(b1, alpha, beta, depth-1);
            m = Math.max(m,v);
            alpha = Math.max(alpha,m);
            if(alpha>=beta){
                //System.out.println("Pruning");
            break;
            }
        }
        return m;
    }

    private int Min(BoardState b, int alpha, int beta, int depth) 
    {
        if (b.gameOver() || depth == 0)
        {
            int k = boardEval(b);
            //System.out.println(k);
            return (k);
        }
        int m = Integer.MAX_VALUE;
        ArrayList<Move> lM = b.getLegalMoves();
        for(int i = 0; i<lM.size(); i++)
        {
            BoardState b1 = b.deepCopy();
            b1.makeLegalMove(lM.get(i));
            int v = Max(b1, alpha, beta, depth-1);
            m = Math.min(m,v);
            beta = Math.min(m,beta);
            if(alpha>=beta){
            //System.out.println("Pruning");
            break;
            }
        }
        return m;
    }


    /**
     * Need to implement boardEval(BoardState)
     *
     * @param   boardState  The current state of the game board
     *
     * @return  The value of the board using Norvig's weighting of squares
     */
    public int boardEval(BoardState boardState) {
        // Add board evaluation code...
        int weightedboard[][] = new int[8][8];
        weightedboard[0][0] = 120; 
        weightedboard[0][1] = -20;
        weightedboard[0][2] = 20;
        weightedboard[0][3] = 5;
        weightedboard[0][4] = 5;
        weightedboard[0][5] = 20;
        weightedboard[0][6] = -20;
        weightedboard[0][7] = 120;
        
        weightedboard[1][0] = -20;
        weightedboard[1][1] = -40;
        weightedboard[1][2] = -5;
        weightedboard[1][3] = -5;
        weightedboard[1][4] = -5;
        weightedboard[1][5] = -5;
        weightedboard[1][6] = -40;
        weightedboard[1][7] = -20;
        
        weightedboard[2][0] = 20;
        weightedboard[2][1] = -5;
        weightedboard[2][2] = 15;
        weightedboard[2][3] = 3;
        weightedboard[2][4] = 3;
        weightedboard[2][5] = 15;
        weightedboard[2][6] = -5;
        weightedboard[2][7] = 20;

        weightedboard[3][0] = 5;
        weightedboard[3][1] = -5;
        weightedboard[3][2] = 3;
        weightedboard[3][3] = 3;
        weightedboard[3][4] = 3;
        weightedboard[3][5] = 3;
        weightedboard[3][6] = -5;
        weightedboard[3][7] = 5;

        weightedboard[4][0] = 5;
        weightedboard[4][1] = -5;
        weightedboard[4][2] = 3;
        weightedboard[4][3] = 3;
        weightedboard[4][4] = 3;
        weightedboard[4][5] = 3;
        weightedboard[4][6] = -5;
        weightedboard[4][7] = 5;

        weightedboard[5][0] = 20;
        weightedboard[5][1] = -5;
        weightedboard[5][2] = 15;
        weightedboard[5][3] = 3;
        weightedboard[5][4] = 3;
        weightedboard[5][5] = 15;
        weightedboard[5][6] = -5;
        weightedboard[5][7] = 20;

        weightedboard[6][0] = -20;
        weightedboard[6][1] = -40;
        weightedboard[6][2] = -5;
        weightedboard[6][3] = -5;
        weightedboard[6][4] = -5;
        weightedboard[6][5] = -5;
        weightedboard[6][6] = -40;
        weightedboard[6][7] = -20;

        weightedboard[7][0] = 120; 
        weightedboard[7][1] = -20;
        weightedboard[7][2] = 20;
        weightedboard[7][3] = 5;
        weightedboard[7][4] = 5;
        weightedboard[7][5] = 20;
        weightedboard[7][6] = -20;
        weightedboard[7][7] = 120;
        
        int ans = 0;

        for(int i = 0; i<8; i++)
        {
            for(int j = 0; j<8; j++)
            {
                int p = boardState.getContents(i,j);
                ans = ans + p*weightedboard[i][j];                
            }
        }
        //int ans= -1;
        return ans;
    }
}

/* vim:set et ts=4 sw=4: */
