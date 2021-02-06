# Adaptación de un modelo YOLOv3 preentrenado con MSCOCO para el reconocimiento de señales de tráfico.

## Uso:

- train.ipynb entrenará el modelo según los valores establecidos en config.json y devolverá la mAP para el conjunto de
validación. Está preparado para usarse en Google Colab con el resto de archivos en '/content/drive/My Drive/Yolov3'.

- predict.py se puede usar en local de la siguiente manera: python predict.py -c config.json -i /path/to/image/or/video.
Devolverá el resultado de aplicar el modelo a una imagen. Puede ser necesario ajustar el campo saved_weights_name, que es
la ruta de acceso a los pesos preentrenados.

## Referencias:

- Implementación original: https://github.com/experiencor/keras-yolo3
- Dataset: https://www.kaggle.com/andrewmvd/road-sign-detection
- Pesos obtenidos del entrenamiento final: https://drive.google.com/file/d/1-Jg549LFj6jE06icVAuyqVErdyYvrTty/view?usp=sharing

## Licencias

Todo el código original extraído del repositorio referenciado anteriormente permanece bajo la licencia original:

MIT License

Copyright (c) 2017 Ngoc Anh Huynh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Todos los cambios realizados están licenciados bajo la GNU General Public License v3.0 que se adjunta en este repositorio