from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import pandas as pd

df_ingredientes = pd.read_csv('pedido_semanal_ingredientes.csv',encoding='latin1')

ingredientes = Element('Ingredientes')

for i in range(len(df_ingredientes)):
    fila = SubElement(ingredientes, 'row{}'.format(i))
    SubElement(fila, 'Indice', name=str(df_ingredientes.iloc[i][0]))
    SubElement(fila, 'Ingrediente', name=str(df_ingredientes.iloc[i][1]))
    SubElement(fila, 'Cantidad', name=str(df_ingredientes.iloc[i][2]))

ficheros = ['orders.csv','data_dictionary.csv','order_details.csv',
            'pizzas.csv','pizza_types.csv']
tipologia = Element('Tipologia')
for j in range(len(ficheros)):
    fichero = SubElement(tipologia,ficheros[j])
    nulls_total = SubElement(fichero,'Cantidad total de nulls',cantidad='0')
    nulls_columna = SubElement(fichero,'Cantidad de nulls por columnas')
    SubElement(nulls_columna,'order_id',cantidad = '0')
    SubElement(nulls_columna,'date',cantidad = '0')
    SubElement(nulls_columna,'time',cantidad = '0')

    NaN_total = SubElement(fichero,'Cantidad total de NaN',cantidad='0')
    NaN_columna = SubElement(fichero,'Cantidad de NaN por columnas')
    SubElement(NaN_columna,'order_id',cantidad = '0')
    SubElement(NaN_columna,'date',cantidad = '0')
    SubElement(NaN_columna,'time',cantidad = '0')

    tipos_columnas = SubElement(fichero,'Tipos de las columnas: ')

    if ficheros[j] == 'orders.csv':
        SubElement(tipos_columnas,'order_id',tipo='int64')
        SubElement(tipos_columnas,'date',tipo='object')
        SubElement(tipos_columnas,'time',tipo='object')

    elif ficheros[j] == 'data_dictionary.csv':
        SubElement(tipos_columnas,'Table',tipo='object')
        SubElement(tipos_columnas,'Field',tipo='object')
        SubElement(tipos_columnas,'Description',tipo='object')

    elif ficheros[j] == 'order_details.csv':
        SubElement(tipos_columnas,'order_details_id',tipo='int64')
        SubElement(tipos_columnas,'order_id',tipo='int64')
        SubElement(tipos_columnas,'pizza_id',tipo='object')
        SubElement(tipos_columnas,'quantity',tipo='int64')

    elif ficheros[j] == 'pizzas.csv':
        SubElement(tipos_columnas,'pizza_type_id',tipo='object')
        SubElement(tipos_columnas,'size',tipo='object')
        SubElement(tipos_columnas,'pizza_id',tipo='object')
        SubElement(tipos_columnas,'price',tipo='float64')

    elif ficheros[j] == 'pizzas_types.csv':
        SubElement(tipos_columnas,'pizza_type_id',tipo='object')
        SubElement(tipos_columnas,'name',tipo='object')
        SubElement(tipos_columnas,'category',tipo='object')
        SubElement(tipos_columnas,'ingredients',tipo='float64')



output_file = open('tipologia_e_ingredientes.xml', 'w')
output_file.write('<?xml version="1.0"?>')
output_file.write(str(ElementTree.tostring(ingredientes)))
output_file.write(str(ElementTree.tostring(tipologia)))
output_file.close()
