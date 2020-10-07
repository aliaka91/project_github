import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("Write the city name, please: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Write the city name correctly please: ").lower()

    # get user input for month (all, january, february, ... , june)

    month = input("Write the month name, please: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Write the month name correctly please: ").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Now, write day of week, please: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("Write the day name correctly please: ").lower()
    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    month_liste = ['january', 'february', 'march', 'april', 'may', 'june']
    if month in month_liste:
        month = month_liste.index(month) + 1
        df = df[df['month'] == month]
    else:
        pass

    day_liste = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day in day_liste:
        df = df[df['day_of_week'] == day.title()]
    else:
        pass
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    # display the most common day of week

    # display the most common start hour
    print('the most common month is:', df['month'].mode()[0])

    # display the most common day of week
    print('the most common day of week is:', df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('the most common start hour is:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print('the most commonly used start station is:', df['Start Station'].mode()[0])

    print('the most commonly used end station is:', df['End Station'].mode()[0])

    df['combination'] = df['Start Station'] + '  ' + df['End Station']
    print('the most most frequent combination of start station and end station trip is :', df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print("The total travel time is:", df['Trip Duration'].sum())

    print("The mean travel time is: {}", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth
    print(df['User Type'].value_counts())

    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print("There is no gender information in this city.")

    if 'Birth_Year' in df:
        print(df['Birth_Year'].min())
        print(df['Birth_Year'].max())
        print(df['Birth Year'].mode()[0])
    else:
        print("There is no birth year information in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def moredata(df):
    raw_data = 0
    while True:
        answer = input("If you want to see the raw data, please write yes otherwise no").lower()
        if answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data: raw_data + 5])
            repeat = input("Do you want to see more, write yes or no").lower()
            if repeat == 'no':
                break
            if repeat=='yes':
                raw_data += 5
                print(df.iloc[raw_data: raw_data + 5])
                repeat = input("Do you want to see more, writeyes or no").lower()
                if repeat == 'no':
                    break
        if answer == 'no':
            return
        else:
            answer = input("Your answer is wrong typo. Please type yes or no.").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        moredata(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
