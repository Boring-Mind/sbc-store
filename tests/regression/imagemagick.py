from wand.image import Image
# from wand.image import COMPARE_METRICS


def create_diff(base_img: str, test_img: str):
    with Image(filename='index-base.png') as base:
        with Image(filename='index.png') as img:
            base.fuzz = base.quantum_range * 0.05
            diff_image, distortion = base.compare(
                image=img,
                metric='root_mean_square'
            )
            # with diff_image:
                # diff_image.save(filename='diff.png')
            return (diff_image, distortion)


def convert_to_webp():
    with Image(filename='index.png') as img:
        img.format = 'webp'
        img.save(filename='index.webp')


# def print_metrics():
#     print(COMPARE_METRICS)


if __name__ == '__main__':
    create_diff()
    # convert_to_webp()
    # print_metrics()
