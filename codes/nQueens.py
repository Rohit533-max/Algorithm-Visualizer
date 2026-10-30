import pygame


class N_Queens:
    def __init__(self, size, speed):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("N-Queens")

        # ---- settings ----
        self.n = size
        self.speed = speed                      # steps per second
        self.x, self.y = 600, 600
        self.block = self.x // self.n
        self.queen_size = (3 * self.block) // 4
        self.offset = (self.block - self.queen_size) // 2

        # colors (same as your original project)
        self.WHITE = (255, 255, 255)
        self.BROWN = (145, 96, 22)
        self.BG = (240, 239, 209)
        self.TEXT = (59, 60, 84)
        self.ATTACK_COL = (255, 51, 0)
        self.SAFE_COL = (40, 180, 70)

        self.screen = pygame.display.set_mode((self.x, self.y + 130))

        # image: loaded once, after set_mod
        self.queen = pygame.image.load("Images/queen.png").convert_alpha()
        self.queen = pygame.transform.scale(self.queen, (self.queen_size, self.queen_size))
        self.ghost = self.queen.copy()          # see-through copy for the square being tried
        self.ghost.set_alpha(130)

        # fonts: created once, not every frame
        self.font = pygame.font.SysFont("calibri", 25)
        self.big_font = pygame.font.SysFont("calibri", 45)

        # ---- algorithm state ----
        self.board = [['.'] * self.n for _ in range(self.n)]   # your grid
        self.queens = []            # queens[row] = column (used for drawing)
        self.candidate = None       # (row, col) being tested right now
        self.attacker = None        # (row, col) of the queen that attacks it
        self.solved = False
        self.steps = self.solve(0)  # the generator

        self.back_rect = pygame.Rect(15, 615, 215, 50)
        self.run()

    # ------------------------------------------------------------------
    # DRAWING (your functions, with small changes)
    # ------------------------------------------------------------------
    def draw_board(self, screen, n, side):
        block = side // n
        for i in range(n):
            for j in range(n):
                color = self.WHITE if (i + j) % 2 == 0 else self.BROWN
                pygame.draw.rect(screen, color, (i * block, j * block, block, block))

    def draw_queens(self, screen, queens, image, block, offset):
        for row, col in enumerate(queens):
            screen.blit(image, (col * block + offset, row * block + offset))

    def center(self, row, col):
        return (col * self.block + self.block // 2,
                row * self.block + self.block // 2)

    def draw_candidate(self):
        """Show the square being tried: green if safe, red + a line if attacked."""
        if self.candidate is None:
            return
        row, col = self.candidate
        bad = self.attacker is not None

        tint = pygame.Surface((self.block, self.block), pygame.SRCALPHA)
        tint.fill((*(self.ATTACK_COL if bad else self.SAFE_COL), 110))
        self.screen.blit(tint, (col * self.block, row * self.block))
        self.screen.blit(self.ghost, (col * self.block + self.offset,
                                      row * self.block + self.offset))
        if bad:
            pygame.draw.line(self.screen, self.ATTACK_COL,
                             self.center(row, col), self.center(*self.attacker), 7)

    def draw_footer(self, seconds):
        pygame.draw.rect(self.screen, self.BG, (0, self.y, self.x, 130))

        # back button with hover colour, like your original
        hover = self.back_rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(self.screen, (194, 167, 45) if hover else (232, 191, 9), self.back_rect)
        self.screen.blit(self.font.render("Back to main menu", True, self.TEXT), (25, 627))

        self.screen.blit(
            self.font.render(f"Time - {seconds // 60}:{seconds % 60:02d}", True, self.TEXT),
            (465, 627))

        if self.solved:
            self.screen.blit(
                self.big_font.render(f"{self.n} Queens Solved!", True, self.TEXT), (145, 680))

    # ------------------------------------------------------------------
    # THE N-QUEENS LOGIC (your code, turned into a generator)
    # ------------------------------------------------------------------
    def find_attacker(self, row, col):
        """Your is_safe checks. Returns the (r, c) of an attacking queen, or None if safe."""
        n = self.n
        board = self.board

        # vertical
        for j in range(n):
            if board[j][col] == "Q":
                return (j, col)

        # top left
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return (i, j)
            i -= 1
            j -= 1

        # top right
        r, c = row, col
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return (r, c)
            r -= 1
            c += 1

        return None

    def solve(self, row):
        """Same backtracking as your nQueens, but it pauses at each yield."""
        if row == self.n:
            return True

        for col in range(self.n):
            self.candidate = (row, col)
            self.attacker = self.find_attacker(row, col)
            yield                                   # show the square being tried

            if self.attacker is None:               # safe: place the queen
                self.board[row][col] = "Q"
                self.queens.append(col)
                self.candidate = None
                yield                               # show the placed queen

                if (yield from self.solve(row + 1)):
                    return True

                self.board[row][col] = "."          # backtrack
                self.queens.pop()
                self.candidate = None
                yield                               # show the queen removed
        return False

    # ------------------------------------------------------------------
    # MAIN LOOP
    # ------------------------------------------------------------------
    def run(self):
        clock = pygame.time.Clock()
        start = pygame.time.get_ticks()
        last_step = start
        seconds = 0
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_rect.collidepoint(event.pos):
                        running = False             # back to menu
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.speed = min(30, self.speed + 1)
                    elif event.key == pygame.K_DOWN:
                        self.speed = max(1, self.speed - 1)

            # advance the algorithm one step when enough time has passed
            now = pygame.time.get_ticks()
            if not self.solved:
                seconds = (now - start) // 1000
                if now - last_step >= 1000 // self.speed:
                    try:
                        next(self.steps)
                    except StopIteration:
                        self.solved = True
                        self.candidate = None
                        self.attacker = None
                    last_step = now

            # draw everything
            self.screen.fill(self.BG)
            self.draw_board(self.screen, self.n, self.x)
            self.draw_queens(self.screen, self.queens, self.queen, self.block, self.offset)
            self.draw_candidate()
            self.draw_footer(seconds)

            pygame.mouse.set_cursor(
                pygame.cursors.Cursor(
                    pygame.SYSTEM_CURSOR_HAND
                    if self.back_rect.collidepoint(pygame.mouse.get_pos())
                    else pygame.SYSTEM_CURSOR_ARROW))

            pygame.display.update()
            clock.tick(60)

        pygame.quit()      # no quit(): control goes back to main() and the menu


if __name__ == "__main__":
    N_Queens(8,5)