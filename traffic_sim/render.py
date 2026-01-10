# render.py
import pygame

SCREEN_SIZE = 500

def render(world):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    screen.fill((30, 30, 30))  # background

    # Draw lanes
    # in render.py, lane rendering
    for lane in world.lanes:
        lane_height = 30
        if lane.direction == "horizontal":
            lane_y = to_screen_y(lane.y_pos)
            pygame.draw.rect(screen, (50, 50, 50), (0, lane_y - lane_height//2, SCREEN_SIZE, lane_height))
            pygame.draw.line(screen, (200,200,200), (0, lane_y), (SCREEN_SIZE, lane_y), 2)
        else:  # vertical
            lane_x = to_screen_x(lane.x_pos)
            pygame.draw.rect(screen, (50, 50, 50), (lane_x - lane_height//2, 0, lane_height, SCREEN_SIZE))
            pygame.draw.line(screen, (200,200,200), (lane_x, 0), (lane_x, SCREEN_SIZE), 2)


    # Draw agent
    agent_pos = world.agent.position
    pygame.draw.circle(screen, (0, 255, 0), to_screen(agent_pos), 10)

    # Draw goal
    goal_pos = world.goal
    pygame.draw.circle(screen, (255, 255, 0), to_screen(goal_pos), 10)

    # Draw cars
    for lane in world.lanes:
        for car in lane.cars:
            car_x, car_y = to_screen(car.position)
            pygame.draw.rect(screen, (255, 0, 0), (car_x - 10, car_y - 5, 20, 10))

    pygame.display.flip()


def to_screen(pos):
    """Convert world coordinates (-1 to 1) to screen pixels (x, y)"""
    x = int((pos[0] + 1) / 2 * SCREEN_SIZE)
    y = int((1 - (pos[1] + 1) / 2) * SCREEN_SIZE)
    return x, y

def to_screen_y(y):
    """Only convert y-coordinate for lane rendering"""
    return int((1 - (y + 1) / 2) * SCREEN_SIZE)
def to_screen_x(x):
    return int((x + 1) / 2 * SCREEN_SIZE)
