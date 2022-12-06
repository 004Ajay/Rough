import pyqrcode
import png

link = 'www.google.com'

qr = pyqrcode.create(link)

qr.png('test_qr.png', scale=10)