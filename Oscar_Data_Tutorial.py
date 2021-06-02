# columns are [0]title [1]year [2]rating [3]length(min) [4]genre [5]budget($mil) [6]box_office_gross($mil)
oscar_data = [
    ["The Shape of Water", 2017, 6.914, 123, ['sci-fi', 'drama'], 19.4, 195.243464],
    ["Moonlight", 2016, 6.151, 110, ['drama'], 1.5, 65.046687],
    ["Spotlight", 2015, 7.489, 129, ['drama', 'crime', 'history'], 20.0, 88.346473],
    ["Birdman", 2014, 7.604, 119, ['drama', 'comedy'], 18.0, 103.215094],
    ["12 Years a Slave", 2013, 7.71, 133, ['drama', 'biography', 'history'], 20.0, 178.371993],
    ["Argo", 2012, 7.517, 120, ['thriller', 'drama', 'biography'], 44.5, 232.324128],
    ["The Artist", 2011, 7.942, 96, ['drama', 'melodrama', 'comedy'], 15.0, 133.432856],
    ["The King\'s Speech", 2010, 7.977, 118, ['drama', 'biography', 'history'], 15.0, 414.211549],
    ["The Hurt Locker", 2009, 7.298, 126, ['thriller', 'drama', 'war', 'history'], 15.0, 49.230772],
    ["Slumdog Millionaire", 2008, 7.724, 120, ['drama', 'melodrama'], 15.0, 377.910544],
    ["No Country for Old Men", 2007, 7.726, 122, ['thriller', 'drama', 'crime'], 25.0, 171.627166],
    ["The Departed", 2006, 8.456, 151, ['thriller', 'drama', 'crime'], 90.0, 289.847354],
    ["Crash", 2004, 7.896, 108, ['thriller', 'drama', 'crime'], 6.5, 98.410061],
    ["Million Dollar Baby", 2004, 8.075, 132, ['drama', 'sport'], 30.0, 216.763646],
    ["The Lord of the Rings: Return of the King", 2003, 8.617, 201, ['fantasy', 'drama', 'adventure'], 94.0, 1119.110941],
    ["Chicago", 2002, 7.669, 113, ['musical', 'comedy', 'crime'], 45.0, 306.776732],
    ['A Beautiful Mind', 2001, 8.557, 135, ['drama', 'biography', 'melodrama'], 58.0, 313.542341],
    ["Gladiator", 2000, 8.585, 155, ['action', 'drama', 'adventure'], 103.0, 457.640427],
    ["American Beauty", 1999, 7.965, 122, ['drama'], 15.0, 356.296601],
    ["Shakespeare in Love", 1998, 7.452, 123, ['drama', 'melodrama', 'comedy', 'history'], 25.0, 289.317794],
    ["Titanic", 1997, 8.369, 194, ['drama', 'melodrama'], 200.0, 2185.372302],
    ["The English Patient", 1996, 7.849, 155, ['drama', 'melodrama', 'war'], 27.0, 231.976425],
    ["Braveheart", 1995, 8.283, 178, ['drama', 'war', 'biography', 'history'], 72.0, 210.409945],
    ["Forrest Gump", 1994, 8.915, 142, ['drama', 'melodrama'], 55.0, 677.386686],
    ["Schindler\'s List", 1993, 8.819, 195, ['drama', 'biography', 'history'], 22.0, 321.265768],
    ["Unforgiven", 1992, 7.858, 131, ['drama', 'western'], 14.4, 159.157447],
    ["Silence of the Lambs", 1990, 8.335, 114, ['thriller', 'crime', 'mystery', 'drama', 'horror'], 19.0, 272.742922],
    ["Dances with Wolves", 1990, 8.112, 181, ['drama', 'adventure', 'western'], 22.0, 424.208848],
    ["Driving Miss Daisy", 1989, 7.645, 99, ['drama'], 7.5, 145.793296],
    ["Rain Man", 1988, 8.25, 133, ['drama'], 25.0, 354.825435],
]

# filtering by year
def filter_by_year(data, begin, end):
    result = []
    for row in data:
        year = row[1]
        if begin <= year <= end:
            result.append(row)
    return result

# summing up the values in the column
def column_sum(data, column):
    result = 0
    for row in data:
        result += row[column]
    return result

# finding the column's mean value
def column_mean(data, column):
    total = column_sum(data, column)
    mean = total / len(data)
    return mean

# calculating the production cost per minute for each film
def add_cost_per_minute(data):
    for i in range(len(data)):
        length = data[i][3]
        budget = data[i][5]
        cost_per_minute = budget / length
        data[i].append(cost_per_minute)

add_cost_per_minute(oscar_data)

years = [[1988, 1997], [1998, 2007], [2008, 2017]]

rows = []
for begin_end in years:
    begin = begin_end[0]
    end = begin_end[1]
    
    name = '{}-{}'.format(begin, end)
    
    filt_data = filter_by_year(oscar_data, begin, end)
    
    
    mean_score = column_mean(filt_data, 2)
    
    mean_length = column_mean(filt_data, 3)
    
    mean_cpm = column_mean(filt_data, 7)
    
    mean_gross = column_mean(filt_data, 6)
    
    
    rows.append([name, mean_score, mean_length, mean_cpm, mean_gross])

print('Year | Rating | Length | Cost per minute | Box office gross  ')
print('--------------------------------------------------------')
for row in rows:
    print('{: <9} | {: >7.2f} | {: >5.2f} | {: >16.2f} | {: >6.2f}'.format(
        row[0], row[1], row[2], row[3], row[4]))
        
        
#From this table, here's what we can conclude:
#Recent films are becoming shorter and cheaper to produce.
#Viewer ratings are decreasing.
#Box office gross is dropping.
#The first idea that comes to mind is that film production is in a downward spiral. 
#However, that would be a shortsighted theory as we haven't properly considered the context of 
#time period and market economy. A more accurate hypothesis would be that the Academy is moving away 
#from a preference for commercially successful films to what is commonly referred to as festival pieces.

#Conclusions from the data:
#Oscar-winning films are becoming shorter, cheaper to produce, and their box office profits tend to be dropping, as well as ratings from viewers. The academy's preferences are shifting towards artsy films and away from the money-making blockbusters.
#Melodramas are the most expensive and profitable genre, stemming from its innate popularity and the outrageous cost of casting big-name actors. Titanic greatly impacted the stats with its titanic budget and box office gross.
#Crime films and thrillers are the shortest films, which earn the least amount of money. It's likely that the sense of suspense they rely on is tough to handle for too long and doesn't cater to the average moviegoer's taste.
