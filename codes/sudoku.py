"""Beginner Sudoku solver with a small Pygame visualizer.

Run:
    python -m pip install pygame
    python game.py
"""
import pygame


# 0 means an empty square.
START_GRID = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

WINDOW_SIZE = 640
CELL_SIZE = 60
BOARD_SIZE = CELL_SIZE * 9
LEFT = (WINDOW_SIZE - BOARD_SIZE) // 2
TOP = 70
BACKGROUND = (246, 244, 232)
WHITE = (255, 255, 255)
DARK = (48, 55, 69)
BLUE = (48, 105, 190)
GREEN = (38, 155, 91)
RED = (210, 65, 65)
GRID_LINE = (155, 145, 118)


def can_place(grid, row, col, number):
    """Check whether number follows Sudoku rules at this empty square."""
    for index in range(9):
        if grid[row][index] == number:
            return False
        if grid[index][col] == number:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == number:
                return False

    return True


def find_empty(grid):
    """Return the first empty square as (row, column), or None if full."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def solve_steps(grid):
    """Solve with backtracking, yielding each guess so Pygame can show it."""
    empty = find_empty(grid)
    if empty is None:
        return True

    row, col = empty

    for number in range(1, 10):
        if can_place(grid, row, col, number):
            grid[row][col] = number
            yield row, col, number, True

            if (yield from solve_steps(grid)):
                return True

            grid[row][col] = 0
            yield row, col, number, False

    return False


def draw_board(screen, grid, candidate, font):
    """Draw the numbers, current solver guess, and 3x3 grid lines."""
    screen.fill(BACKGROUND)

    for row in range(9):
        for col in range(9):
            x = LEFT + col * CELL_SIZE
            y = TOP + row * CELL_SIZE

            is_candidate = candidate is not None and candidate[:2] == (row, col)
            if is_candidate:
                pygame.draw.rect(screen, (226, 239, 222) if candidate[3] else (247, 224, 220),
                                 (x, y, CELL_SIZE, CELL_SIZE))

            number = grid[row][col]
            if number:
                if START_GRID[row][col] != 0:
                    color = DARK
                elif is_candidate:
                    color = GREEN if candidate[3] else RED
                else:
                    color = BLUE

                text = font.render(str(number), True, color)
                screen.blit(text, text.get_rect(center=(x + CELL_SIZE // 2,
                                                        y + CELL_SIZE // 2)))
            elif is_candidate:
                text = font.render(str(candidate[2]), True, RED)
                screen.blit(text, text.get_rect(center=(x + CELL_SIZE // 2,
                                                        y + CELL_SIZE // 2)))

    for index in range(10):
        thickness = 4 if index % 3 == 0 else 1
        x = LEFT + index * CELL_SIZE
        y = TOP + index * CELL_SIZE
        pygame.draw.line(screen, GRID_LINE, (x, TOP), (x, TOP + BOARD_SIZE), thickness)
        pygame.draw.line(screen, GRID_LINE, (LEFT, y), (LEFT + BOARD_SIZE, y), thickness)


def main():
    pygame.init()
    pygame.display.set_caption("Sudoku Solver")
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 100))
    clock = pygame.time.Clock()
    number_font = pygame.font.SysFont("calibri", 30)
    message_font = pygame.font.SysFont("calibri", 20)

    grid = [row[:] for row in START_GRID]
    steps = None
    candidate = None
    solving = False
    paused = False
    solved = False
    last_step = pygame.time.get_ticks()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_s and not solving and not solved:
                    steps = solve_steps(grid)
                    solving = True
                elif event.key == pygame.K_SPACE and solving:
                    paused = not paused
                elif event.key == pygame.K_r:
                    grid = [row[:] for row in START_GRID]
                    steps = None
                    candidate = None
                    solving = False
                    paused = False
                    solved = False

        # Advance the solver every 120 milliseconds.
        now = pygame.time.get_ticks()
        if solving and not paused and now - last_step >= 120:
            try:
                candidate = next(steps)
            except StopIteration as result:
                solving = False
                solved = result.value
                candidate = None
            last_step = now

        draw_board(screen, grid, candidate, number_font)

        if solved:
            message = "Solved! Press R to restart or Esc to quit."
            message_color = GREEN
        elif paused:
            message = "Paused. Press Space to continue."
            message_color = DARK
        elif solving:
            message = "Solving... Space pauses, R restarts."
            message_color = DARK
        else:
            message = "Press S to solve, R to restart, Esc to quit."
            message_color = DARK

        text = message_font.render(message, True, message_color)
        screen.blit(text, text.get_rect(center=(WINDOW_SIZE // 2, TOP + BOARD_SIZE + 45)))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
