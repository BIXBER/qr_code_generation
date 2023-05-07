import qrcode
import numpy as np
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask


data = 'https://practicum.yandex.ru/'
file_name = 'qr_code.png'


def generate_qr_code(data, file_name):
    qr_object = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr_object.add_data(data)
    qr_object.make(fit=True)
    print("The shape of the QR image:", np.array(qr_object.get_matrix()).shape)
    img = qr_object.make_image(image_factory=StyledPilImage,
                               module_drawer=RoundedModuleDrawer(),
                               color_mask=HorizontalGradiantColorMask(
                                          (255, 255, 255),
                                          (70, 70, 70),
                                          (10, 10, 10)
                                          ),
                               )
    img.save(file_name)


generate_qr_code(data, file_name)
print(f"QRCode saved as {file_name}")
