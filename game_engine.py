import config


class GameEngine:

    def __init__(self):

        self.ball_x = config.WINDOW_WIDTH // 2
        self.ball_y = config.WINDOW_HEIGHT // 2

        self.speed_x = config.BALL_SPEED_X
        self.speed_y = config.BALL_SPEED_Y

        self.score = 0

    def update_ball(self):

        self.ball_x += self.speed_x
        self.ball_y += self.speed_y

        if self.ball_x < 0 or self.ball_x > config.WINDOW_WIDTH:
            self.speed_x *= -1

        if self.ball_y < 0:
            self.speed_y *= -1

    def check_paddle_collision(self, paddle_x):

        paddle_y = config.WINDOW_HEIGHT - config.PADDLE_Y_OFFSET

        if (
            paddle_x - config.PADDLE_WIDTH // 2
            < self.ball_x
            < paddle_x + config.PADDLE_WIDTH // 2
        ):
            if paddle_y - 20 < self.ball_y < paddle_y:
                self.speed_y *= -1
                self.score += 1

    def reset(self):

        self.ball_x = config.WINDOW_WIDTH // 2
        self.ball_y = config.WINDOW_HEIGHT // 2
        self.score = 0