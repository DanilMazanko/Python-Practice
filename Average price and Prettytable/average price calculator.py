# function to calculate the averege price


def average(count, number):
    for i in range(len(min_price)):
        number = (min_price[count] + max_price[count]) / 2
        avg.append(number)
        count += 1


# variables to hold numbers before appending to the array(avg)
count = 0
number = 0

home_pricing = PrettyTable()

min_price = [300, 400, 350]
max_price = [2000, 4000, 2560]
avg = []
average(count, number)

# adding columns to the table
home_pricing.add_column('Address', ['Lviv', 'Kharkov', 'Poltava'])
min_price = home_pricing.add_column('Min Price', min_price)
max_price = home_pricing.add_column('Max Price', max_price)
avg_price = home_pricing.add_column('Average Price', avg)

print(home_pricing)
