def filemaker():
    valu_l = [f"hello{x}.txt" for x in range(3)]
    
    for file in valu_l:
        file_1 = open(f'{file}', "w+")
        file_1.write("hello")
        file_1.close()



filemaker()