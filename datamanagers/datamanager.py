import matplotlib.pyplot as plt

class Dataset:

    def __init__(self, values):
        self.values = values

    def minimum(self):
        return min(self.values)

    def maximum(self):
        return max(self.values)

    def mean(self):
        return sum(self.values) / len(self.values)

    def median(self):
        if len(self.values)%2 == 1:
            return self.values[round(len(self.values)/2)]
        else:
            half_lenght = int(len(self.values)/2)
            return (self.values[half_lenght]+self.values[half_lenght+1])/2

    def trend(self):
        results = {}
        for n in self.values:
            if n not in results:
                results[n] = self.values.count(n)
            else:
                continue
        for line in results:
            print("Counted", line, ":", results[line])
        return results[max(results)]

    def trend_plot(self):
        results = {}
        for n in self.values:
            if n not in results:
                results[n] = self.values.count(n)
            else:
                continue
        plt.bar(results.keys(), results.values())
        plt.ylabel("Number of recusions")
        plt.xlabel("Value from the set")
        plt.title("Distribution of the set")
        plt.show()

    def geometric_mean(self):
        result = 1
        for n in self.values:
            result *= n
        return (result ** (1 / len(self.values)))

    def harmonic_mean(self):
        try:
            reciproci = [(1 / value) for value in self.values]
            return len(self.values) / sum(reciproci)
        except ZeroDivisionError:
            print(
                "A 0 was found as a value in the set - division by zero error while evaluating relatives coefficients")

    def quadratic_mean(self):
        quads = [(n ** 2) for n in self.values]
        return (sum(quads) / len(self.values)) ** (1 / 2)

    def st_dev(self):
        avg = self.mean()
        deviations = [((x - avg) ** 2) for x in self.values]
        return ((sum(deviations) / (len(self.values))) ** (1 / 2))

    def st_dev_plot(self):
        results = [(x - self.mean()) for x in self.values]
        plt.bar(self.values, results)
        plt.bar(self.mean(), max(results))
        plt.ylabel("Deviation from the mean")
        plt.xlabel("Observations")
        plt.title("Deviation of observations plot")
        plt.show()

    def variance(self):
        return self.st_dev() ** 2

    def distribution_type(self):
        if self.mean == self.median:
            print("Normal distribution over the mean and median values of",self.mean)

if __name__ != "__main__":
    print(('''-----------------------------------------------------------------------------------------
Imported dataset manager v.0.01, tool to manage dataset and perform calculations over it.
For more information see helper file in the installation folder.
Copyright Nicola Moro, 2019.
-----------------------------------------------------------------------------------------'''))
