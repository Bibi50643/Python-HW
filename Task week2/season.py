month=input("Input the month (e.g. [01-12]):") 
day=int(input("Input the day:")) 
 
 
d={'01':'January','02':'February','03':"March", '04':"April",'05':"May",'06':"June",'07':"July",'08':"August",'09':"September",'10':"October",'11':"November",'12':"December"} 
if month=='01': 
        print(d.get(month),day,"Season is winter") 
elif month=='02': 
        print(d.get(month),day,"Season is winter") 
elif month=='03': 
        print(d.get(month),day,"Season is spring") 
elif month=='04': 
        print(d.get(month),day,"Season is spring") 
elif month=='05': 
        print(d.get(month),day,"Season is spring") 
elif month=='06': 
        print(d.get(month),day,"Season is summer") 
elif month=='07': 
        print(d.get(month),day,"Season is summer") 
elif month=='08': 
        print(d.get(month),day,"Season is summer") 
elif month=='09': 
        print(d.get(month),day,"Season is autumn") 
elif month=='10': 
        print(d.get(month),day,"Season is autumn") 
elif month=='11': 
        print(d.get(month),day,"Season is autumn") 
elif month=='12': 
        print(d.get(month),day,"Season is winter")