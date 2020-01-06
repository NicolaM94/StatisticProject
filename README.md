# Stats project guide

###### Stat project is a tool that tries to provide an easy way to calculate and perfoms operations over datasets and lists of variables.
###### The project contains multiple modules that will be explained along this guide.

##### Note: A Python interpreter is required to run the project.

---

## API
1. ##### dataset
    1. ###### Dataset
        * values
        * maximum
        * minimum
        * mean
        * median
        * trend
        * trend_plot
        * geometric_mean
        * harmonic_mean
        * quadratic_mean
        * st_dev
        * st_dev_plot
        * variance
2. ##### linear_regs
    1. ###### SimpleRegression
        * x
        * y
        * mean_x
        * mean_y
        * mean_diff_x
        * mean_diff_y
        * covariance
        * slope
        * intercept
        * calculate
        * mse
        * rmse
        * plot_it
---

### 1. dataset.py
This module contains classes and functions to perform basics operations over a dataset and manage
dataset files like .csv, .xls and other.

#### i. Dataset
Basic dataset manager. A list or tuple needs to be passed as parameter to create a dataset
object.
> observations = [1,1,2,3,1,5,7,0,10,4,5,6,4,7,8,3,1,4]
>
>set  = Dataset (observations)

* ##### set.values
Values used as the class parameter. These must be passed as parameter during the class object creation.
> set.values
>
>[1,1,2,3,1,5,7,0,10,4,5,6,4,7,8,3,1,4]

* ##### maximum()
Maximum value found in the observations
>set.maximum()
>
>10

* ##### minimum()
Minimum value found in the observatons
>set.minimum()
>
>0

* ##### mean()
Average value found in the observations
>set.avg()
>
>4

* ##### median()
Median value found in the observations. If the lenght of the dataset is even, there will be a no-median message promted on the shell.
>set.median()
>
>Lenght of the set is even - no median value found

* ##### trend()
Trend value of the observations set. This is the most recurrent value in the dataset.
A dictionary is printed to the shell to show results from iteration thru the values but the function returns the value with the most observations in the set.
>set.trend()
>
>Counted 1 : 4
>
>Counted 2 : 1
>
>Counted 3 : 2
>
>Counted 5 : 2
>
>Counted 7 : 2
>
>Counted 0 : 1
>
>Counted 10 : 1
>
>Counted 4 : 3
>
>Counted 6 : 1
>
>Counted 8 : 1
>
>1

* ##### trend_plot()
Returns a plot of the dataset distribution in a new level window.
>set.trend_plot()

* ##### geometric_mean()
Returns the geometric average of the observations found in the dataset.
>set.geometric_avg()
>
>1.2681923779934947

* ##### harmonic_mean()
Returns the harmonic average of the observations found in the dataset. If a values is a zero, the error message is printed in the shell.
>set.armonic_avg()
>
>A 0 was found as a value in the set - division by zero error while evaluating relatives coefficients

* ##### quadratic_mean()
Returns the quadratic average of the observations found in the dataset.
>set.quadratic_avg()
>
>4.8419463487779835

* ##### st_dev()
Returns the standard deviation of the observatons found in the dataset.
>set.st_dev()
>
>2.807552838536876

* ##### st_dev_plot()
Graphical rappresentation of the deviation of the observations from the arithmetic mean calculated.
>set.st_dev_plot()

* ##### variance()
Returns the variance of the observations found in the dataset.
>set.variance()
>
>7.882352941176471

### 1. linear_regs
Module containing the classes to perform simple, multiple and other linear regressions.

#### i. 