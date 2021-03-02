# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

updated_damages = []

for damage in damages:
    if damage[-1] == 'B':
        x = float(damage[:-1])*10**9
        updated_damages.append(x)
    elif damage[-1] == 'M':
        x = float(damage[:-1])*10**6
        updated_damages.append(x)
    else:
        updated_damages.append(damage)


# write your construct hurricane dictionary function here:
##dictionary of hurricanes with key = name and value = dict of info on the hurricane
hurricane_dict = {}
for i in range(len(names)):
    sub_dict = {'name':names[i],'month':months[i], 'year':years[i], 'max_sustained_wind':max_sustained_winds[i], 'area_affected':areas_affected[i], 'damages':updated_damages[i], 'deaths':deaths[i]}
    hurricane_dict[names[i]]=sub_dict


# write your construct hurricane by year dictionary function here:

## gives a dicttionary, with keys = year, and value = list of dicts with all the hurricanes for that year
hurricane_by_year_dict = {}
for name, subdict in hurricane_dict.items():
    current_year = hurricane_dict[name]['year']
    current_dict = hurricane_dict[name]
    if current_year not in hurricane_by_year_dict: 
        hurricane_by_year_dict[current_year] = [current_dict]
    else:
        hurricane_by_year_dict[current_year] += [current_dict]

#print(hurricane_by_year_dict)

# write your count affected areas function here:
## counts the number of times each area has been hit
area_dict = {}
for name, subdict in hurricane_dict.items():
    for area in (hurricane_dict[name]['area_affected']):
        if area not in area_dict.keys(): 
            area_dict[area] = 1
        else:
            area_dict[area] += 1
## print(area_dict)
# write your find most affected area function here:

#finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
## finds the place most frequently hit by hurricanes and how many times it was hit
Worst_place = {}
for place, times_hit in area_dict.items():
    if not Worst_place:
        Worst_place['name'] = place
        Worst_place['times_hit'] = area_dict[place]
    elif times_hit > Worst_place['times_hit']:
        Worst_place.pop()
        Worst_place['name'] = place
        Worst_place['times_hit'] = area_dict[place]
print("the place most frequently hit by hurricanes is {}, which was hit {} times".format(Worst_place['name'], Worst_place['times_hit']))


# write your greatest number of deaths function here:
## finds the hurricanes that caused the most deats, and how many deaths it caused
deadliest = {}
for name, subdict in hurricane_dict.items():
    if not deadliest:
        deadliest = subdict
    elif hurricane_dict[name]['deaths'] > deadliest['deaths']:
        deadliest = subdict
print("the deadliest hurricane is {} with a death toll of {} people".format(deadliest['name'], deadliest['deaths']))

# write your catgeorize by mortality function here:
## ads a 
for name, subdict in hurricane_dict.items():
    mortality_scale = 0
    if hurricane_dict[name]['deaths'] < 100:
        mortality_scale = 0 
    elif hurricane_dict[name]['deaths'] < 500:
        mortality_scale = 1
    elif hurricane_dict[name]['deaths'] < 1000:
        mortality_scale = 2
    elif hurricane_dict[name]['deaths'] < 10000:
        mortality_scale = 3
    elif hurricane_dict[name]['deaths'] >= 10000:
        mortality_scale = 4
    hurricane_dict[name]['mortality_scale'] = mortality_scale

# print(hurricane_dict['Cuba I'])
mortality_dict = {}
for i in range(5):
    if i not in mortality_dict:
        mortality_dict[i] = []
        for name, subdict in hurricane_dict.items():
            current_dict = hurricane_dict[name]
            mort = hurricane_dict[name]['mortality_scale']
            if mort == i:
                mortality_dict[i] += [current_dict]

# write your greatest damage function here:
greatest_damage = {}
for name, subdict in hurricane_dict.items():
    if hurricane_dict[name]['damages'] == "Damages not recorded":
        continue    
    elif not greatest_damage:
        greatest_damage = hurricane_dict[name]
    elif (hurricane_dict[name]['damages']) > (greatest_damage['damages']):
        greatest_damage =  hurricane_dict[name]
            
print("the hurricane which caused the greatest damage was {} whivh caused damages for {} dollars".format(greatest_damage['name'], greatest_damage['damages']))

# write your catgeorize by damage function here:

for name, subdict in hurricane_dict.items():
    if hurricane_dict[name]['damages'] =="Damages not recorded":
        hurricane_dict[name]['damage_scale'] = 'N/a'
    else:
        if hurricane_dict[name]['damages'] < 100000000:
            hurricane_dict[name]['damage_scale'] = 0
        elif hurricane_dict[name]['damages'] < 1000000000:
            hurricane_dict[name]['damage_scale'] = 1
        elif hurricane_dict[name]['damages'] < 10000000000:
            hurricane_dict[name]['damage_scale'] = 2
        elif hurricane_dict[name]['damages'] < 100000000000:
            hurricane_dict[name]['damage_scale'] = 3
        elif hurricane_dict[name]['damages'] < 500000000000:
            hurricane_dict[name]['damage_scale'] = 4

damage_dict = {'N/a':[], 0:[], 1:[], 2:[], 3:[], 4:[]}

for name, subdict in hurricane_dict.items():
    if hurricane_dict[name]['damage_scale'] == 'N/a':
        damage_dict['N/a'] += [hurricane_dict[name]]
    elif hurricane_dict[name]['damage_scale'] == 0:
        damage_dict[0] += [hurricane_dict[name]]
    elif hurricane_dict[name]['damage_scale'] == 1:
        damage_dict[1] += [hurricane_dict[name]]
    elif hurricane_dict[name]['damage_scale'] == 2:
        damage_dict[2] += [hurricane_dict[name]]
    elif hurricane_dict[name]['damage_scale'] == 3:
        damage_dict[3] += [hurricane_dict[name]]
    elif hurricane_dict[name]['damage_scale'] == 4:
        damage_dict[4] += [hurricane_dict[name]]

print(damage_dict)

    


