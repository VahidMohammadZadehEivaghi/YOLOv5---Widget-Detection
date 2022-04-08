from detect import *


def inference(screen_shot, run_device="0"):
    config = parse_opt()
    config.source = screen_shot
    config.device = run_device
    config.weights = 'weights/best.pt'
    widget_coordinates = main(config)
    return widget_coordinates

