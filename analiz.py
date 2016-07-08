from math import* 
import datetime        
d=datetime.datetime.today()
date_of_data_analyse="Дата обробки даних: " + str(d.day) + "." + str(d.month) + "." +str(d.year)+" року, " + str(d.hour) +" год. " + str(d.minute) +" хв."
def analiz(data_file):
    """Tis function analise input data file and return results"""
    f_data=open(data_file)  
    data=f_data.readlines()   
    i=0
    for key in data:          
        data[i]=float(key)
        i=i+1
    number_of_elements=len(data)
    max_data=max(data)
    min_data=min(data)
    suma=fsum(data)
    midle=suma/number_of_elements
    sum=0
    for key in data:
        numerator=(key-midle)**2
        sum=sum+numerator
    standart_deviation=sqrt(sum/number_of_elements) 
    a={'data_file': data_file, 'number_of_elements': number_of_elements, 'min_data': min_data, 'max_data': max_data, 'midle': midle, 'standart_deviation':standart_deviation}
    return a

d1=analiz ("data_input_1.txt")
d2=analiz ("data_input_2.txt")

#Статистичне порiвняння вибiрок
#Критерiй Кохрена:
def Kohren(d1, d2):
    """  Порiвняння даних двох стандартних вiдхилень двох вибiрок
    за  критерiєм Кохрена. Для визначення табличного значення критерiю Кохренна:
    k - число ступенiв вiльностi, k=n-1, де n-розмiр вибiрки, l- кiлькiсть вибiрок, 
    приблизно, потрiбно використати формулу для визначення табличного критерiя вiдповiдно до k i l"""
    if d1['standart_deviation'] > d2['standart_deviation'] :
        standart_deviation_max=d1['standart_deviation'] 
    else:
        standart_deviation_max=d2['standart_deviation'] 
    G=(standart_deviation_max**2)/((d1['standart_deviation'] **2)+(d2['standart_deviation'] **2))
    
    Q=0.6 
    if G>Q:
        result='Вибiрки суттєво вiдрiзняються, що свiдчить про їх належнiсть до рiзних генеральних сукупностей'
    else:
        result='Вибiрки суттєво не вiдрiзняються i належать однiй генеральнiй сукупностi'
    a={'result_text':result, 'standart_deviation_max': standart_deviation_max, 'Q':Q, 'G':G}
    return a
result=Kohren(d1, d2)   
result_string=[]
result_string.append("Результати статистичного аналiзу вхiдних даних \n")
result_string.append(date_of_data_analyse +"\n")
result_string.append("******************************\n")

#Запис результатiв у файл
def result_str (d1, d2):
    def res (d, i):
        result_string.append(i  + " (файл iз даними: "  + "'"+d['data_file'] + "'" + ") \n" )
        result_string.append("******************************\n")
        result_string.append("Розмiр вибiрки: "+str(d['number_of_elements'])+" елементiв \n")
        result_string.append("Максимальне значення вибiрки: "+str(d['max_data'])+"\n")
        result_string.append("Мiнiмальне значення вибiрки: " +str(d['min_data'])+"\n")
        result_string.append("Середнє значення вибiрки: " +str(d['midle'])+"\n")
        result_string.append("Середнє квадратичне вiдхилення вибiрки: " +str(round(d['standart_deviation'],2))+"\n")
        result_string.append("******************************\n")
        
    res(d1, "Вибiрка №1")
    res(d2, "Вибiрка №2")
    
    result_string.append("Розраховане значення критерiю Кохрена: " +str(result['G'])+"\n")
    result_string.append("Критичне значення критерiю Кохрена: " +str(result['Q'])+"\n")
    result_string.append("*****************************\n")
    result_string.append("Висновок: " +"\n")
    result_string.append(result['result_text']+"\n")

result_str (d1, d2)
f_results=open("results.txt", 'w')
for key in result_string:
    f_results.write(key)
    print (key)

f_results.close()