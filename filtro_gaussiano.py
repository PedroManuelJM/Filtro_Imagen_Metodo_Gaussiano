from PIL import Image

ancho, alto = 0,0
def filtrar3x3(img,M):
    salida = Image.new("L",(ancho,alto))
    # el valor de la matriz de la mascara
    Ma,Mb,Mc = M[0][0],M[0][1],M[0][2]
    Md,Me,Mf = M[1][0],M[1][1],M[1][2]
    Mg,Mh,Mi = M[2][0],M[2][1],M[2][2]
    for i in range(2,img.size[0]-1):
        for j in range(2,img.size[1]-1):
            # valor de la porcion de la imagen
            Ia,Ib,Ic = float(img.getpixel((i-1,j-1))), float(img.getpixel((i-1,j))), float(img.getpixel((i-1,j+1)))
            Id,Ie,If = float(img.getpixel((i,j-1))), float(img.getpixel((i,j))), float(img.getpixel((i,j+1)))
            Ig,Ih,Ii = float(img.getpixel((i+1,j-1))), float(img.getpixel((i+1,j))), float(img.getpixel((i+1,j+1)))
            q = int(Ia*Ma+Ib*Mb+Ic*Mc+Id*Md+Ie*Me+If*Mf+Ig*Mg+Ih*Mh+Ii*Mi)
            salida.putpixel((i,j),q)
    return salida
    
imgGray = Image.open("snoopygris.jpg").convert("L")
imgGray.show()
ancho,alto = imgGray.size
Promedio = [[1/9,1/9,1/9],
            [1/9,1/9,1/9],
            [1/9,1/9,1/9]]

Gaussiano = [[1/16,2/16,1/16],
            [2/16,4/16,2/16],
            [1/16,2/16,1/16]]
Gaussiano = [[1/16,2/16,1/16],
            [2/16,4/16,2/16],
            [1/16,2/16,1/16]]
Gaussiano = [[1/16,2/16,1/16],
            [2/16,4/16,2/16],
            [1/16,2/16,1/16]]



resultado = filtrar3x3(imgGray,Gaussiano)# filtro de la imagen filtrar3x3
resultado.save("promedio_Gaussiano.tiff")
resultado.show()
