from wand.image import Image
# from wand.image import COMPARE_METRICS

from selenium_services import SCREENSHOTS_DIR


def create_diff(base_img: str, test_img: str):
    with Image(filename=SCREENSHOTS_DIR + r'/' + base_img + '.png') as base:
        with Image(filename=SCREENSHOTS_DIR + r'/' + test_img + '.png') as img:
            base.fuzz = base.quantum_range * 0.05
            diff_image, distortion = base.compare(
                image=img,
                metric='root_mean_square'
            )
            return (diff_image, distortion)


def screenshots_equal(base_img: str, test_img: str) -> bool:
    """Return True if sreenshots are equal, False if not.
    
    base_img - name of baseline image file
    test_img - name of image file, created by current test
    """
    diff_image, distortion = create_diff(base_img, test_img)

    # If images differs in more, than 1%
    if distortion > 0.01:
        with diff_image:
            diff_image.save(
                filename=SCREENSHOTS_DIR + r'/' + 'diff_' + test_img + '.png'
            )
        return False
    else:
        return True


def convert_to_webp():
    with Image(filename='index.png') as img:
        img.format = 'webp'
        img.save(filename='index.webp')


# def print_metrics():
#     print(COMPARE_METRICS)


if __name__ == '__main__':
    create_diff('asfasdf', 'bsdkcksjdbc')
    # convert_to_webp()
    # print_metrics()
