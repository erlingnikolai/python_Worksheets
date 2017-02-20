import numpy as np
import pydoc
import worksheet5


filename = ("raintemp.csv")
    




def read_data(filename):
    """ will read_the data from a file"""
    a = np.loadtxt(filename, dtype=float, skiprows=1)
    return a


    
def find_offset(x):
    """ will find the offset """
    a = read_data(filename)
    i = 0
    for row in a:
        if x in row:
            return(i)
        i = i+1
  
def get_years(array, startYear, endYear):
    """ will find all years between startYear and endYear in an array """
    return(array[find_offset(startYear):find_offset(endYear)+1]);
    
    
def mean_temps(array):
    """ will find the mean_temps for summer and winter """
    summer = ("summer", np.average(array[:, 3]))
    winter = ("winter", np.average(array[:, 1]))
    temps = (summer, winter)
    return temps;    
    

def time_slot(tuples):
    """ will get a tupple """
    return tuples;

  

file = read_data(filename)
victorianEra = time_slot(mean_temps(get_years(file, 1845, 1900)))
modernEra = time_slot(mean_temps(get_years(file, 1970, 2011)))





def main():
    """ the main for the Spyder """
 #   print(victorianEra)
 #   print(modernEra)
    
if __name__ == "__main__":
    """ the main for script """
    # execute only if run as a script
    main()
    
  
    
#print(find_offset(1845))
#print(get_years(file, 1845, 1850))
print(victorianEra)
print(modernEra)
pydoc.writedoc(worksheet5)