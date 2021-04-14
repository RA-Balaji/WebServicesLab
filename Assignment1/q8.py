import pyqrcode 
import png 
from pyqrcode import QRCode 
  

def generate_qr(s):
  
    # Generate QR code 
    url = pyqrcode.create(s) 
    
    # Create and save the png file naming "myqr.png" 
    url.png('../UI/images/Qr/'  + s + '.png', scale = 6)
