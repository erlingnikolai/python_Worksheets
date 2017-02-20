import numpy

filename = ("raintemp.csv")
    





def read_data(filename):
    a = np.loadtxt(filename, dtype=float, skiprows=1)
    return a


    
def find_offset(x):
    a = read_data(filename)
    i = 0
    for row in a:
        if x in row:
            return(i)
        i = i+1
  




def get_years(array, startYear, endYear):
    return(array[find_offset(startYear):find_offset(endYear)+1]);
    
    
def mean_temps(array):
    summer = ("summer", np.average(array[:, 3]))
    winter = ("winter", np.average(array[:, 1]))
    temps = (summer, winter)
    return temps;    
    

def time_slot(tuples):
    return tuples;

  

file = read_data(filename)
victorianEra = time_slot(mean_temps(get_years(file, 1845, 1900)))
modernEra = time_slot(mean_temps(get_years(file, 1970, 2011)))




def script_main():
    print(victorianEra)
    print(modernEra)
    
if __name__ == "__main__":
    # execute only if run as a script
    script_main()
    
  
    
print(find_offset(1845))
print(get_years(file, 1845, 1850))
print(victorianEra)
print(modernEra)