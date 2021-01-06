import glob
from bs4 import BeautifulSoup

# Trasladar las coordenadas de x/y min y max a centro,altura y anchura
def translate(input_path, output_path ):
    # Por cada fichero .xml del directorio
    for name in glob.glob(input_path,recursive=True):

        # Abrimos el fichero en el que escribiremos los datos
        out_file = open(output_path+name.split("/")[-1][:-3]+"txt","w")
        
        print("Leyendo:",name)
        # Extraemos los datos y los parseamos como .xml
        with open(name, 'r') as f: 
            data = f.read()

        Bs_data = BeautifulSoup(data, "lxml")

        # Buscamos los objetos que hay anotados
        objetos = Bs_data.find_all('object') 

        # Por cada objeto hacemos la traducción y la guardamos en el archivo de destino
        for obj in objetos:
            clase = obj.find("name").get_text(strip=True)
            
            xmin = int(obj.find("xmin").get_text(strip=True))
            xmax = int(obj.find("xmax").get_text(strip=True))
            ymin = int(obj.find("ymin").get_text(strip=True))
            ymax = int(obj.find("ymax").get_text(strip=True))

            x_centro = (xmin+xmax)/2
            y_centro = (ymin+ymax)/2
            anchura = xmax-xmin
            altura = ymax-ymin

            out_file.write(" ".join(map(str,(clase,x_centro,y_centro,anchura,altura)))+"\n")

        out_file.close()

translate('../Dataset/test_zip/test/*.xml','../Dataset/test/')
translate('../Dataset/train_zip/train/*.xml','../Dataset/train/')
