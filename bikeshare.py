import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = list(map(str, CITY_DATA))
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while True:
        city = input('Kindly choose a city. Chicago, New York City, or Washington?\n').lower()

        if city in cities:
            break
        else:
            print('please enter a valid city')

        # get user input for month (all, january, february, ... , june)
    month = ''
    while True:
        month = input('Kindly choose a month? January, February, March, April, May, June  or all?\n').lower()

        if month in months:
            break
        elif month == 'all':
            break
        else:
            print('please enter a valid month')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Kindly type a weekday as a string or type all for all weekdays.\n').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # loading the attached files to get data
    df = pd.read_csv(CITY_DATA[city])

    # Convert the start time column to get a pandas datetime object
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Apply new columns : [month, weekdays]
    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_name'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()
    print('\nThe most common month is:\n {}'.format(most_common_month))

    # display the most common day of week
    most_common_week_day = df['day_name'].mode()
    print('\nThe most common day of week is:\n {}'.format(most_common_week_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('\nThe most common start hour is: {}'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print('\nThe most commonly used start station is:\n {}'.format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print('\nThe most commonly used end station is:\n {}'.format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    most_frequent_combination = df[['Start Station', 'End Station']].mode()
    print('\nThe most frequent combination of start station and end station trip is:\n {}'.format(most_frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time is: {}'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_type = df['User Type'].value_counts()
    print('\nCounts of user types are:\n {}'.format(counts_of_user_type))

    # Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print('\nCounts of gender are:\n {}'.format(counts_of_gender))
    else:
        print('\nThere are no info about gender for your chosen city')

    # Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        earliest_year_of_birth = df['Birth Year'].min()
        print('Earliest year of birth is: {}'.format(earliest_year_of_birth))

        most_recent_year_of_birth = df['Birth Year'].max()
        print('\nThe most recent year of birth is: {}'.format(most_recent_year_of_birth))

        most_common_year_of_birth = df['Birth Year'].mode()
        print('\nThe most common year of birth is:\n {}'.format(most_common_year_of_birth))
    else:
        print('There are no info about birthday for your chosen city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """
        Asks the user to view five rows of the data

        Returns:
            (df) display the first five rows of the data frame, if the user said 'yes'
            (df) Continue iterating these prompt and display the next five rows if the answer is 'yes'
            (df) stop the function when the user says 'no'
    """
    # get user input for the prompt of the data display
    iteration = 0
    string = 'the first'
    start_loc = 0
    while True:
        view_data = input('\nWould you like to see {} five rows of the data? Enter yes or no.\n'.format(string)).lower()
        if view_data.lower() != 'yes':
            break
        else:
            print('\nDisplaying Rows Stats...')
            start_time = time.time()

            data = df.iloc[start_loc: start_loc+5]
            print('\nThe five rows are:\n{}'.format(data))
            start_loc += 5
            iteration += 1
            if iteration >= 1:
                string = 'the next'

            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-' * 40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
