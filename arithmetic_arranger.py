import re #imports Regular Expressions 

#it makes the opperations if answers == true and returns the values
def sumas(list, extensions):
    resultados = []
    resultados_format =""
    resultados2 = []
  #looks if it's a sum or a substraction and makes the operation 
    for equation in list:
        if '-' in equation:
            numbers_1 = equation.split("-")
            temp = str(int(numbers_1[0]) - int(numbers_1[1]))
            resultados.append(temp)
        else:
            numbers_1 = equation.split("+")
            temp = str(int(numbers_1[0]) + int(numbers_1[1]))
            resultados.append(temp)
    
  #justifies
    index3 = 0
    for value in extensions:
        resultados2.append(resultados[index3].rjust(value +2))
        index3 += 1
    
  #joins the results and returns 
    resultados_format = '    '.join(resultados2)
    return resultados_format
  
  
#MAIN FUNCTION

def arithmetic_arranger(problems, answers='False'):
  
    
      
    problemsToString = str(problems)
    line_1 = re.findall('([0-9]*)\s[\+|\-]', problemsToString)
    line_2 = re.findall('[\+|\-]\s([0-9]*)', problemsToString)

    #TESTS

    #Nº1
    if len(problems) > 5:
        return 'Error: Too many problems.'

    #Nº2
    test2 = re.findall('[\*|\/]', problemsToString)
    if len(test2) != 0:
        return "Error: Operator must be '+' or '-'."
    
    #Nº3
    for number in line_1:
        if len(number) > 4:
          return 'Error: Numbers cannot be more than four digits.'
    for number in line_2:
        if len(number) > 4:
          return 'Error: Numbers cannot be more than four digits.'

    #Nº4
    test4 = re.findall('[a-zA-Z]', problemsToString)
    if len(test4) != 0:
        return 'Error: Numbers must only contain digits.'
  #END TESTS

  
    #creates a list with the length of the operands an decides the extension of the output ("extensions")
    extensions = list()
    for i in range(len(line_1)):
        if len(line_1[i]) > len(line_2[i]):
            extensions.append(len(line_1[i]))
        else:
            extensions.append(len(line_2[i]))
        
    #creates the final string lists      
    n_list_1 = list()
    n_list_2 = list()
    final_line = list()
  
   #Creates the "---" list
    for value in extensions:
        delimit = ""
        for times in range(value+2):
            delimit += "-"
        final_line.append(delimit)  

    #justifies the strings in the lists to the right with the maximum length of the two strings
    index1 = 0
    for value in extensions:
        n_list_1.append(line_1[index1].rjust(value+2))
        index1 += 1
    index2 = 0
    for value in extensions:
        if '-' in problems[index2]:
            n_list_2.append('- ' + line_2[index2].rjust(value))
        else:
            n_list_2.append('+ ' + line_2[index2].rjust(value))
        index2 += 1
  
   #joins the results with the 4 blank spaces  
    n_list_1 = '    '.join(n_list_1)
    n_list_2 = '    '.join(n_list_2)
    final_line = '    '.join(final_line)
    
    final = n_list_1.rstrip() + '\n' + n_list_2.rstrip() + '\n' + final_line.rstrip()

  #returns the outcome
    if answers == True:
        anexo = sumas(problems, extensions)
        final2= final + '\n' + anexo
        return(final2)
    else:
        return final
      