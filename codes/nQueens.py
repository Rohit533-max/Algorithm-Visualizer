import pygame
def draw_board(screen, n, side):
    block = side // n
    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "black"
            pygame.draw.rect(screen,color,(i*block,j*block, block, block))


pygame.init()
#screen size
x,y = 600,600
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("NQueens")

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # window color
    screen.fill("black")
    draw_board(screen,8,x)

    #update the display after every action
    pygame.display.update()

    clock.tick(60)

pygame.quit()

class Solution:
    def solve(self, n):
        board = [['.']* n for i in range(n)]
        ans = []
        def is_safe(row,col,n):

            #vertical
            for j in range(n):
                if board[j][col] == "Q":
                    return False

            #top left
            i,j = row,col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i-=1
                j-=1

            # top right
            r,c = row,col
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -=1
                c+=1

            return True

        def nQueens(board,row,n):
            if row == n:
                ans.append(["".join(row) for row in board])

            for j in range(n):
                if is_safe(row,j,n):
                    board[row][j] = "Q"

                    nQueens(board,row+1,n)

                    board[row][j] = "."

        nQueens(board,0,n)
        return ans

