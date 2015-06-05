
#  Kent Han 23271274.  ICS 32 Lab sec 8.  Project 4.
import othello_logic
import othello_beginings


def game():
    g_thang = othello_logic.State(othello_beginings.init_dict())
    while othello_beginings.winner_print(g_thang) == othello_logic.NONE:
        othello_beginings.print_score(g_thang)
        othello_beginings.print_board(g_thang.board())
        othello_beginings.get_move(g_thang)
    othello_beginings.print_board(g_thang.board())
    othello_beginings.print_score(g_thang)

if __name__ == '__main__':
    game()

