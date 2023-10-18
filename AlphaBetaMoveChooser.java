import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * Solution code for Comp24011 Reversi lab
 *
 * @author r67083sr
 */

public class AlphaBetaMoveChooser extends MoveChooser {
    /**
     * MoveCooser implementation AlphaBetaMoveChooser(int)
     *
     * @param   searchDepth The requested depth for minimax search
     */

     private class tableNode
     {
        protected int score;
        protected int depth;
        protected int type; // 0 is exact, 1 is upper bound and -1 is lower bound
        public tableNode(int score, int depth, int type){
            this.score = score;
            this.depth = depth;
            this.type = type;
        }
    }
    private Map<Integer,tableNode> transpositionTable;
    public AlphaBetaMoveChooser(int searchDepth) {
        // Add object initialisation code...
        super("MyAwesomeAgent",searchDepth);
        transpositionTable = new HashMap<>();
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
        int t = 1;
        if(boardState.colour == -1)
        {
            t = -1;
        }
        Move ans= null;
        int optimum = Integer.MIN_VALUE;

        int alpha = Integer.MIN_VALUE;
        int beta = Integer.MAX_VALUE;
        ArrayList<Move> legalMoves = boardState.getLegalMoves();
        for(int i = 0; i<legalMoves.size(); i++)
        {
            Move a = legalMoves.get(i);
            BoardState b = boardState.deepCopy();
            b.makeLegalMove(a);
            int h = Min(b, alpha, beta, this.searchDepth-1, t);
            if (h>optimum)
            {
                optimum = h;
                ans = a;
            }
            alpha = Math.max(alpha, optimum);
            if (alpha >= beta) 
            {
                break;
            }
        }
        return ans;
    }

    private int Max(BoardState b, int alpha, int beta, int depth, int t) 
    {
        int hash = b.hashCode();
        if(transpositionTable.containsKey(hash) && transpositionTable.get(hash).depth>depth)
        {
            int value = transpositionTable.get(hash).score;
            if(transpositionTable.get(hash).type == 0)
            {
                return value;
            }
            else if (transpositionTable.get(hash).type >0 && value <= alpha)
            {
                return value;
            }
            else if (transpositionTable.get(hash).type <0 && value >= beta)
            {
                return value;
            }
            else if (alpha >= beta)
            {
                return value;
            }
        }
        
        if (b.gameOver() || depth == 0)
        {
            int k = t*boardEval(b);
            if(k <= alpha)
            {
            transpositionTable.put(hash, new tableNode(k, depth, 1));
            }
            else if(k >= beta)
            {
            transpositionTable.put(hash, new tableNode(k, depth, -1));
            }
            else
            {
                transpositionTable.put(hash, new tableNode(k, depth,0));
            }
            return (k);
        }
        int m = Integer.MIN_VALUE;
        ArrayList<Move> lM = b.getLegalMoves();
        for(int i = 0; i<lM.size(); i++)
        {
            BoardState b1 = b.deepCopy();
            b1.makeLegalMove(lM.get(i));
            int v = Min(b1, alpha, beta, depth-1, t);
            m = Math.max(m,v);
            if(m>=beta)
            {
                return m;
            }
            alpha = Math.max(alpha,m);
        }
        return m;
    }

    private int Min(BoardState b, int alpha, int beta, int depth, int t) 
    {
        int hash = b.hashCode();
        if(transpositionTable.containsKey(hash) && transpositionTable.get(hash).depth>depth)
        {
            int value = transpositionTable.get(hash).score;
            if(transpositionTable.get(hash).type == 0)
            {
                return value;
            }
            else if (transpositionTable.get(hash).type >0 && value <= alpha)
            {
                return value;
            }
            else if (transpositionTable.get(hash).type <0 && value >= beta)
            {
                return value;
            }
            else if (alpha >= beta)
            {
                return value;
            }
        }
        if (b.gameOver() || depth == 0)
        {
            int k = t*boardEval(b);
            //System.out.println(k);
            if(k <= alpha)
            {
            transpositionTable.put(hash, new tableNode(k, depth, 1));
            }
            else if(k >= beta)
            {
            transpositionTable.put(hash, new tableNode(k, depth, -1));
            }
            else
            {
                transpositionTable.put(hash, new tableNode(k, depth,0));
            }
            return (k);
        }
        int m = Integer.MAX_VALUE;
        ArrayList<Move> lM = b.getLegalMoves();
        for(int i = 0; i<lM.size(); i++)
        {
            BoardState b1 = b.deepCopy();
            b1.makeLegalMove(lM.get(i));
            int v = Max(b1, alpha, beta, depth-1, t);
            m = Math.min(m,v);
            if(alpha>=m)
            {
                return m;
            }
            beta = Math.min(m,beta);
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
        return ans;
    }
}

/* vim:set et ts=4 sw=4: */
