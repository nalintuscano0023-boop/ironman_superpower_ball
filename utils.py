import cv2
import config


def draw_ball(img, x, y):

    cv2.circle(img, (x, y), config.BALL_RADIUS, config.BALL_COLOR, -1)


def draw_paddle(img, paddle_x):

    y = config.WINDOW_HEIGHT - config.PADDLE_Y_OFFSET

    cv2.rectangle(
        img,
        (paddle_x - config.PADDLE_WIDTH // 2, y),
        (paddle_x + config.PADDLE_WIDTH // 2, y + config.PADDLE_HEIGHT),
        config.PADDLE_COLOR,
        -1,
    )


def draw_score(img, score):

    cv2.putText(
        img,
        f"Score: {score}",
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        config.TEXT_COLOR,
        2,
    )