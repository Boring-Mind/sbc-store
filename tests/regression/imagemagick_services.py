import os

from wand.image import Image
# from wand.image import COMPARE_METRICS

from selenium_services import BASELINE_DIR, SCREENSHOTS_DIR


def create_diff(base_img: str, test_img: str):
    with Image(filename=base_img) as base:
        with Image(filename=test_img) as img:
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
    base_path = os.path.join(BASELINE_DIR, f"{base_img}.png")
    test_path = os.path.join(SCREENSHOTS_DIR, f"{test_img}.png")

    diff_image, distortion = create_diff(base_path, test_path)

    # If images differs in more, than 1%
    if distortion > 0.01:
        with diff_image:
            filename = os.path.join(SCREENSHOTS_DIR, f"diff_{test_img}.png")
            if os.path.exists(filename):
                os.remove(filename)

            diff_image.save(
                filename=filename
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
    screenshots_equal('login', 'login')
    # convert_to_webp()
    # print_metrics()
