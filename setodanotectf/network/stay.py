import base64
data = b"UEsDBBQAAQAAADBq8FK0Nz5zSgAAAD4AAAATAAAAUmVwb3J0LUFWLVQwMDk3LnR4dAzRMzm6s5vAM3huF0n2GEKFrarxVD3WvzurjKz9sjA7iD6nWis0GBRcIdcyrQkqliocBi2lCUB6J0hRUgHzDVCnVx6LnLS5LenqUEsBAj8AFAABAAAAMGrwUrQ3PnNKAAAAPgAAABMAJAAAAAAAAAAgAAAAAAAAAFJlcG9ydC1BVi1UMDA5Ny50eHQKACAAAAAAAAEAGADNWpx++XnXARJtllL6edcB0TOVfvl51wFQSwUGAAAAAAEAAQBlAAAAewAAAAAA"
base64_decoded=base64.b64decode(data)
f = open("Report-AV-T0097.zip","wb")
f.write(base64_decoded)
f.close()