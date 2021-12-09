import numpy as np
import pandas as pd

PRINT_INTRO = False
PRINT_IDX_SEL = False
PRINT_MULTI_INDEX = True

if PRINT_INTRO:
    # introduction Series (is like a hashmap)
    data = pd.Series([0.25, 0.5, 0.75, 1.0])
    print(f'full data: \n {data}')
    print(f'data values \n {data.values}')
    print(f'data index \n {data.index}')
    print(data[1])
    print(data[2:])
    
    data = pd.Series([0.25, 0.5, 0.75, 1.0] ,
                    index = ['a', 'b', 'c', 'd'])
    print(f'serie with char as index \n {data}')
    print(data['b'])
    population_dict = {'California':38000000,
                       'Texas':26000000,
                       'Florida':19000000,
                       'New York': 19000000}
    population = pd.Series(population_dict)
    print(population)
    print(population['California'])
    data = pd.Series({1:'a',2:'b',3:'c'}, index=[3,2])
    print(data)

    #introduction DataFrame 
    population_dict = {'California':38000000,
                       'Texas':26000000,
                       'Florida':19000000,
                       'New York':19000000}
    population = pd.Series(population_dict)
    area_dict = {'California':420000,'Texas':700000,'Florida':170000,'New York':140000}
    area = pd.Series(area_dict)
    states = pd.DataFrame({'population':population,
                            'area':area})
    print(f'full data frame: \n {states}')
    print(f'index data frame: \n {states.index}')
    print(f'columns data frame: \n {states.columns}')
    print(states['area'])

    df1 = pd.DataFrame(population, columns = ['population'])
    print(f'construct from series \n {df1}')
    data = [{'a': i, 'b':2 * i}
            for i in range(3)]
    df2 = pd.DataFrame(data)
    print(f'construct from list of dicts \n {df2}')
    df3 = pd.DataFrame([{'a':1, 'b':2}, {'b':645, 'c':6545}])
    print(f'construct with missign keys: \n {df3}')
    df4 = pd.DataFrame(np.random.rand(3,2), columns = ['foo', 'bar'], index = ['a', 'b', 'c'])
    print(f'from a 2 dimensional numpy array: \n {df4}')
    A = np.zeros(3, dtype=[('A','i8'), ('B','f8')])
    df5 = pd.DataFrame(A)
    print(f'from numpy structured array \n {df5}') 

    ind = pd.Index([2,3,4,7,11])
    print(ind)
    print(ind[3])
    print(ind[::2])

    indA = pd.Index([1,2,5,7])
    indB = pd.Index([1,5,9])
    print(f'index intersection: \n {indA & indB}')
    print(f'index reunion: \n {indA | indB}')
    print(f'index simmetric difference: \n {indA ^ indB}')

if PRINT_IDX_SEL:
    data  = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
    print(data['b'])
    print(f'keys {data.keys()}')
    print(list(data.items()))
    # extend Series
    data['e'] = 1.25
    print(list(data.items()))
    print('slicing an implicit index: \n' + str(data['a':'c']))
    print('slicing by implicit integter index \n' + str(data[0:2]))
    print('slicing by masking \n' + str(data[(data > 0.3) & (data < 0.8)]))
    print('########################')
    population_dict = {'California':38000000,
                       'Texas':26000000,
                       'Florida':19000000,
                       'New York':19000000}
    population = pd.Series(population_dict)
    area_dict = {'California':420000,'Texas':700000,'Florida':170000,'New York':140000}
    area = pd.Series(area_dict)
    data = pd.DataFrame({'population':population,
                            'area':area})
    data['density'] = data['population'] / data['area']
    print(data)
    print(data.T)
    print(data.values[0])
    print(data.population)
    print(data['population'])
    print('##################################')
    print("### fun with loc, iloc and idx ###")
    print(f"first 2 lines \n {data.iloc[0:2]}")
    print(f"first 2 lines and 2 columns \n {data.iloc[:3,:2]}")
    print(f"explicit index \n {data.loc[:'Florida', :'area']}")
    print("masking and fancy indexing \n " + str(data.loc[data.density > 80, ['population','density']]))


if PRINT_MULTI_INDEX:
    index = [('California', 2000), ('California', 2010), 
            ('New York', 2000), ('New York', 2010),
            ('Texas', 2000), ('Texas', 2010)]
    populations = [33000000, 37000000, 18000000, 19000000, 20000000, 25000000]
    pop = pd.Series(populations, index = index)
    print(pop)
    print(pop[('California', 2010):('Texas', 2000)]) # already sorted, that's why it works
    


