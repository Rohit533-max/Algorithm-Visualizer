
import pygame
import time
import random


class Grid:
    def __init__(self, board, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.win = win

        self.cubes = [
            [Cube(board[i][j], i, j, width, height) for j in range(cols)]
            for i in range(rows)
        ]

        self.start_time = time.time()
        self.play_time = 0
        self.running = True
        self.return_to_menu = False
        self.update_model()

    def update_model(self):
        self.model = [
            [self.cubes[i][j].value for j in range(self.cols)]
            for i in range(self.rows)
        ]

    def format_time(self):
        minutes = self.play_time // 60
        seconds = self.play_time % 60
        return f"{minutes}:{seconds:02d}"

    def draw(self):
        self.win.fill((240, 239, 209))
        gap = self.width / 9

        for i in range(self.rows + 1):
            thick = 4 if i % 3 == 0 and i != 0 else 1
            pygame.draw.line(self.win, (0, 0, 0),
                             (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(self.win, (0, 0, 0),
                             (i * gap, 0), (i * gap, self.height), thick)

        for row in self.cubes:
            for cube in row:
                cube.draw(self.win)

    def draw_controls(self):
        mouse = pygame.mouse.get_pos()
        font = pygame.font.SysFont("calibri", 25)

        color = (194, 167, 45) if 10 <= mouse[0] <= 230 and 550 <= mouse[1] <= 595 else (232, 191, 9)
        pygame.mouse.set_cursor(
            *(pygame.cursors.tri_left if color == (194, 167, 45) else pygame.cursors.arrow)
        )

        pygame.draw.rect(self.win, color, (10, 550, 220, 45))
        self.win.blit(font.render("Back to main menu", True, (59, 60, 84)), (23, 560))

        self.play_time = round(time.time() - self.start_time)
        timer = font.render("Time - " + self.format_time(), True, (59, 60, 84))

        pygame.draw.rect(self.win, (240, 239, 209), (350, 560, 190, 50))
        self.win.blit(timer, (400, 560))

    def redraw(self):
        self.draw()
        self.draw_controls()
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 <= x <= 230 and 550 <= y <= 595:
                    self.running = False
                    self.return_to_menu = True
                    return False

        return self.running

    def solve_gui(self, speed):
        if not self.running:
            return False

        self.update_model()
        empty = find_empty(self.model)

        if empty is None:
            return True

        row, col = empty
        gap = self.width / 9
        delay = max(1, (101 - speed) // 3)

        for num in range(1, 10):
            if not self.handle_events():
                return False

            if valid(self.model, num, (row, col)):
                self.model[row][col] = num
                self.cubes[row][col].set(num)
                self.redraw()

                pygame.draw.rect(self.win, (0, 255, 0),
                                 (col * gap, row * gap, gap, gap), 3)
                self.draw_controls()
                pygame.display.update()
                pygame.time.delay(delay)

                if self.solve_gui(speed):
                    return True

                if not self.running:
                    return False

                self.model[row][col] = 0
                self.cubes[row][col].set(0)
                self.redraw()

                pygame.draw.rect(self.win, (255, 0, 0),
                                 (col * gap, row * gap, gap, gap), 3)
                self.draw_controls()
                pygame.display.update()
                pygame.time.delay(delay)

        return False


class Cube:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def draw(self, win):
        font = pygame.font.SysFont("comicsans", 40)
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            win.blit(text, (
                x + gap / 2 - text.get_width() / 2,
                y + gap / 2 - text.get_height() / 2
            ))
        elif self.temp != 0:
            text = font.render(str(self.temp), True, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))

    def set(self, value):
        self.value = value


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def valid(board, num, pos):
    row, col = pos

    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def valid_board(board):
    for i in range(9):
        for j in range(9):
            num = board[i][j]

            if num != 0:
                board[i][j] = 0
                is_valid = valid(board, num, (i, j))
                board[i][j] = num

                if not is_valid:
                    return False

    return True


def sudoku(speed):
    pygame.init()
    pygame.font.init()

    win = pygame.display.set_mode((540, 670))
    pygame.display.set_caption("Sudoku Solver Visualizer")

    boards = [
        [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ],
        [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ],
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    ]

    selected_board = [row[:] for row in random.choice(boards)]
    board = Grid(selected_board, 9, 9, 540, 540, win)

    if not valid_board(board.model):
        print("Invalid Sudoku board")
        pygame.quit()
        return

    board.redraw()

    solved = board.solve_gui(max(1, min(100, int(speed))))

    if not board.running:
        pygame.quit()

        if board.return_to_menu:
            import Start_Threading
            Start_Threading.open_main_window()

        return

    message = "Sudoku Solved!" if solved else "No Solution!"
    color = (59, 60, 84) if solved else (255, 0, 0)

    font = pygame.font.SysFont("comicsans", 45)
    text = font.render(message, True, color)
    win.blit(text, (100, 615))
    pygame.display.update()

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if 10 <= x <= 230 and 550 <= y <= 595:
                    run = False
                    pygame.quit()

                    import Start_Threading
                    Start_Threading.open_main_window()
                    return

        pygame.display.update()

    pygame.quit()
