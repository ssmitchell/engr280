from file_utils import loadWithJSON
import constants

class CovidDataset:
    """
    Represents a set of COVID data and provides methods to analyze
    said data
    """

    def __init__(self, data: list):
        self.data = data

    def get_first_positive(self) -> str:
        """
        Returns the date of the first positive case in the dataset
        in the form of a string
        """
        for data_point in self.data:
            if data_point[1] > 0:
                return data_point[0]

    def get_max_case_day(self) -> str:
        """
        Returns the date of the day with the highest number of
        cases in the dataset
        """
        max_case_day = self.data[0][0] 
        max_case_num = self.data[0][1]
        for data_index in range(1, len(self.data)):
            increase = self.data[data_index][1] - self.data[data_index-1][1] 
            if increase > max_case_num:
                max_case_day = self.data[data_index][0]
                max_case_num = increase
        return max_case_day


    def get_worst_n_days(self, days:int) -> str:
        """
        Returns the worst rolling n-day period in terms of the
        total number of cases over that period.
        """
        days -= 1
        # Sets worst day number and range to first n days
        worst_seven_days_num = self.data[days][1] - self.data[0][1]
        worst_seven_days_range = [0, days]

        for i in range(0, len(self.data) - days):
            n_day_diff = [datapoint[1] for datapoint 
                in self.data[i:i+days]] 
            if n_day_diff[-1] - n_day_diff[0] > worst_seven_days_num:
                worst_seven_days_num = n_day_diff[-1] - n_day_diff[0] 
                worst_seven_days_range = [i, i+days]

        return (str(self.data[worst_seven_days_range[0]][0]),
            str(self.data[worst_seven_days_range[1]][0]))



if __name__ == "__main__":
    harrisonburg_data = loadWithJSON('harrisonburg.json')
    print(CovidDataset(harrisonburg_data).
        get_worst_n_days(constants.DAYS_IN_WEEK))
    
