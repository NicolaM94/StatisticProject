from matplotlib import pyplot as plt

class SimpleRegression:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def mean_x (self):
        return self.x.mean()

    def mean_y (self):
        return self.y.mean()

    def mean_diff_x (self):
        results = [(x-self.mean_x()) for x in self.x.values]
        return results
    
    def mean_diff_y (self):
        results = [(y-self.mean_y()) for y in self.y.values]
        return results

    def stdev_x(self):
        deviations = [((n) ** 2) for n in self.mean_diff_x()]
        return (sum(deviations) / (len(self.x.values) - 1)) ** (1 / 2)

    def stdev_y(self):
        deviations = [((n) ** 2) for n in self.mean_diff_y()]
        return  (sum(deviations)/(len(self.y.values)-1)) ** (1/2)

    def covariance(self):
        numerator = sum([(couple[0]*couple[1]) for couple in zip(self.mean_diff_x(),self.mean_diff_y())])
        return numerator/(len(self.x.values)-1)

    def slope(self):
        numerator = sum([(couple[0]*couple[1]) for couple in zip(self.mean_diff_x(),self.mean_diff_y())])
        denominator = sum([(n**2) for n in self.mean_diff_x()])
        return numerator/denominator

    def intercept(self):
        return self.mean_y() - self.slope()*self.mean_x()

    def calculate(self,x):
        return self.intercept()+x*self.slope()
    
    def mse(self):
        predictions = [(self.calculate(x)) for x in self.x.values]
        numerator = [((couple[0]-couple[1])**2) for couple in zip(predictions,self.y.values)]
        return sum(numerator)/len(self.x.values)
    
    def rmse(self):
        return self.mse()**(1/2)

    def pearson_corr(self):
        r = self.covariance()/(self.stdev_x()*self.stdev_y())
        if r == 1.0:
            print(f'''Pearson R coefficient of correlation is {r} > perfect positive correlation found.
Function returning the pearson coefficient value.''')
        elif r == -1.0:
            print(f'''Pearson R coefficient of correlation is {r} > perfect negative correlation found.
Function returning the pearson coefficient value.''')
        elif r>-1 and r<0:
            print(f'''Pearson R coefficient of correlation is {r} > negative correlation found.
Function returning the pearson coefficient value.''')
        elif r<1 and r>0:
            print(f'''Pearson R coefficient of correlation is {r} > positive correlation found.
Function returning the pearson coefficient value.''')
        else:
            print(f'''! Pearson R coefficient of correlation is {r} ! Please check your calculations.''')
        return r

    def plot_it(self):
        estimates = [(self.calculate(x)) for x in self.x.values]
        line = plt.plot(self.x.values,estimates)
        scatter = plt.scatter(self.x.values,self.y.values,c="red")
        plt.title("Regression line plot")
        plt.ylabel("Regression results")
        plt.xlabel("Dataset values")
        plt.show()