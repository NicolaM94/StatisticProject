from matplotlib import pyplot as plt

class SimpleRegression:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def mean_x (self):
        return sum(self.x)/len(self.x)

    def mean_y (self):
        return sum(self.y)/len(self.y)

    def mean_diff_x (self):
        results = [(x-self.mean_x()) for x in self.x]
        return results
    
    def mean_diff_y (self):
        results = [(y-self.mean_y()) for y in self.y]
        return results
    
    def covariance(self):
        numerator = sum([(couple[0]*couple[1]) for couple in zip(self.mean_diff_x(),self.mean_diff_y())])
        return numerator/(len(self.x)-1)

    def slope(self):
        numerator = sum([(couple[0]*couple[1]) for couple in zip(self.mean_diff_x(),self.mean_diff_y())])
        denominator = sum([(n**2) for n in self.mean_diff_x()])
        return numerator/denominator

    def intercept(self):
        return self.mean_y() - self.slope()*self.mean_x()

    def calculate(self,x):
        return self.intercept()+x*self.slope()
    
    def mse(self):
        predictions = [(self.calculate(x)) for x in self.x]
        numerator = [((couple[0]-couple[1])**2) for couple in zip(predictions,self.y)]
        return sum(numerator)/len(self.x)
    
    def rmse(self):
        return self.mse()**(1/2)

    def plot_it(self):
        estimates = [(self.calculate(x)) for x in self.x]
        line = plt.plot(self.x,estimates)
        scatter = plt.scatter(self.x,self.y,c="red")
        plt.title("Regression line plot")
        plt.ylabel("Regression results")
        plt.xlabel("Dataset values")
        plt.show()