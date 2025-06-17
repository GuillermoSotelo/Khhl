def leer_texto():
    m=open("ordenes25.txt","rt")
    
    
    return m
def codigo_moneda(moneda):
    if "ARS" not in moneda and "JPY" not in moneda and "GBP" not in moneda and "USD" not in moneda and "EUR" not in moneda:
            return False
    return True
def dos_o_mas_diferentes(moneda):
    x=0
    
    if "ARS" in moneda:
         x+=1
    if "USD" in moneda:
         x+=1
    if "EUR" in moneda:
         x+=1
    if "GBP" in moneda:
         x+=1
    if "JPY" in moneda:
         x+=1
    if x>1:
         return False
    return True
    
         
def es_mayuscula(c):
    return c.isupper()
def es_numero(c):
    return c.isdigit()
def es_guion(c):
    return c in "-_"

def principal():
    texto=leer_texto()
    line=texto.readline()
    cant_binvalida=0
    cant_minvalida=0
    condicion_minvalida1=False
    condicion_minvalida2=False
    for line in texto:
        nombre_destinatario=line[0:20]
        codigo_identificacion=line[20:30].strip()
        orden_de_pago=line[30:40]
        monto_nominal=line[40:50]
        ide_algoritmo_comision=line[50:52]
        ide_algoritmo_impositvo=line[52:54]
        
        codigo_identificacion_destinatario_es_invalido=False
        todos_guiones=True
        for c in codigo_identificacion:
             
             if not es_guion(c):
                  todos_guiones=False
            
             
          #    if (not es_mayuscula(c) and es_numero(c) and not es_guion(c)):#todos numeros(valido)
          #         codigo_identificacion_destinatario_es_invalido=False
          #         print("hola mundo")
          #    if (es_mayuscula(c) and not es_numero(c) and not es_guion(c)):#todas mayusculas(valido)
          #         codigo_identificacion_destinatario_es_invalido=False
          #    if (es_mayuscula(c) or es_numero(c)) and (not es_guion(c)):#mayusculas y numeros(sin guiones, valido)
          #         codigo_identificacion_destinatario_es_invalido=False
             if (not es_mayuscula(c) and not es_numero(c) and not es_guion(c)):
                    codigo_identificacion_destinatario_es_invalido=True
               
          
        condicion_minvalida1,condicion_minvalida2=False,False     
        if (not codigo_moneda(orden_de_pago) or not dos_o_mas_diferentes(orden_de_pago)):
             condicion_minvalida1=True
        if codigo_identificacion_destinatario_es_invalido or todos_guiones:
             condicion_minvalida2=True
              
        
        
        if condicion_minvalida1 or (condicion_minvalida1 and condicion_minvalida2):
             cant_minvalida+=1
        if condicion_minvalida2 and (codigo_moneda(orden_de_pago) and dos_o_mas_diferentes(orden_de_pago)):
            cant_binvalida+=1
     #    if not (condicion_minvalida1 and condicion_minvalida2) and condicion_minvalida2:
     #         cant_binvalida+=1
    print("cont minvalida",cant_minvalida)
    print("cont_binvalida",cant_binvalida)
        


        

principal()
   

   
