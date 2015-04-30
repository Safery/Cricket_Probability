import urllib.request
import urllib.parse
import math

_teams_ = {'England': 1, 'Australia': 2, 'South Africa': 3, 'West Indies': 4, 'New Zealand': 5, 'India': 6, 'Pakistan': 7, 'Sri Lanka': 8, 'Bangladesh': 25}
_type_ = {'Test': 1, 'ODI': 2, 'T20': 3, 'All': 11}
_game_ = ['batting', 'bowling', 'fielding', 'allround', 'fow', 'official', 'team', 'aggregate']




url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=!;opposition=$;spanmin1=05+Jan+2005;spanval1=span;team=@;template=results;type=batting'
url_2 = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;opposition=7;spanmin1=05+Jan+2005;spanval1=span;team=25;template=results;type=team'

def get_probability(team):
    '''
    '''
    team_prob = {}    
    for each in team:
        i = 0
        match = 0
        avg = 0
        high_score = 0
        runs = 0
        while i < len(team[each]):
            if (i == 0):
                if (team[each][i] == ''):
                    match = 1
                else:
                    match = team[each][i]
            elif (i == 2):
                if (team[each][i] == ''):
                    high_score = 1
                if ('*' in team[each][i]):
                    if (len(team[each][i]) == 10):
                        high_score = team[each][i][:-1]
                    else:
                        high_score = team[each][i][:-2]
                    
                else:
                    high_score = team[each][i]
            elif (i == 1):
                if (team[each][i] == ''):
                    runs = 1
                if ('<' in team[each][i]):
                    if (len(team[each][i]) == 10):
                        runs = team[each][i][3:6]
                    else:
                        runs = team[each][i][3:5]
                        
                else:
                    runs = team[each][i]
            elif (i == 3):
                if (team[each][i] == ''):
                    avg = 1
                else:
                    avg = team[each][i]
            i += 1
        if (high_score == ''):
            high_score = 1
        if (runs == ''):
            runs = 1
        if (isinstance(match, str)):
            match = 1
        get_ans1 = pow((float(avg)/int(high_score)), 3.1415926535897932-1.61)
        get_ans2 = get_ans1 * (int(runs)/int(match))
        
        team_prob[str(each)] = get_ans2
    
    
    return (team_prob)

def get_team_info(team1, team2, types='ODI', game=None):
    '''
    '''
    # Get info on team1
    new_url = url.replace('!', str(_type_[types]))
    new_url2 = new_url.replace('@', str(_teams_[team1]))
    req = urllib.request.Request(new_url2.replace('$', str(_teams_[team2])), headers={"X-Mashape-Key": "cmKnfWdd6imshaIgonGHypfkNZ8kp1Sds7DjsnLSrzh5VaS3p9", "Accept": "application/json"})
    
    response = urllib.request.urlopen(req)
    the_page = str(response.read())
    new_info = the_page[the_page.find('<tbody>'):the_page.find('</tbody>')]
    get_player_team1 = team_info_players(str(new_info))
    
    # Get info on team2
    
    new_url = url.replace('!', str(_type_[types]))
    new_url2 = new_url.replace('@', str(_teams_[team2]))
    req = urllib.request.Request(new_url2.replace('$', str(_teams_[team1])), headers={"X-Mashape-Key": "cmKnfWdd6imshaIgonGHypfkNZ8kp1Sds7DjsnLSrzh5VaS3p9", "Accept": "application/json"})
    
    response = urllib.request.urlopen(req)
    the_page = str(response.read())
    new_info = the_page[the_page.find('<tbody>'):the_page.find('</tbody>')]
    get_player_team2 = team_info_players(str(new_info))    
    return (get_player_team1, get_player_team2)
    
def team_info_players(player_str):
    '''
    '''
    get_info = player_str
    player_list = {}
    while (get_info.find('class="data1"') >= 1):
        new_str = get_info[get_info.find('"data-link">')+12:get_info.find('</a></td>')]
        x = get_info[get_info.find('</a></td>')+13:]
        
        
        z = x[x.find('p="nowrap">')+11:x.find('</td>')]
        # Change '2015' to the current year to get the recent players
        if ('2015' in z):
            player_list[str(new_str)] = []
                    
            # Get the numbers of matches played against the oppo team.
            xz = x[x.find('</td>')+4:]            
            player_list[new_str].append(xz[xz.find('<td>')+4:xz.find('</td>')])
            x = xz[xz.find('</td>')+3:]
            
            # Get the numbers of runs played against the oppo team.
            _i_ = 0
            while _i_ < 2:
                xz = x
                x = xz[xz.find('</td>')+4:]
                _i_ += 1
            xz = x
            player_list[new_str].append(xz[xz.find('<td>')+4:xz.find('</td>')])
            x = xz[xz.find('</td>')+3:]
            
            # Get the high score.
            
            xz = x
            
            if ('class="padAst">' in xz[:xz.find('</td>')]):
                player_list[new_str].append(xz[xz.find('class="padAst">')+15:xz.find('</td>')])
                x = xz[xz.find('</td>')+3:]
            else:
                player_list[new_str].append(xz[xz.find('<td>')+4:xz.find('</td>')])
                x = xz[xz.find('</td>')+3:]
            
            # Get the high score.
            xz = x
            player_list[new_str].append(xz[xz.find('<td>')+4:xz.find('</td>')])
            x = xz
            
        
        
        # Looper
        get_info = get_info[player_str.find('</a></td>'):]

            
    
    while '' in player_list:
        player_list.pop('')
    
    return player_list
        

__x__ = ({'Arafat Sunny': ['3', '', '', ''], 'Sabbir Rahman': ['3', '<b>15</b>', '15', '15.00'], 'Tamim Iqbal': ['16', '<b>676</b>', '132', '45.06'], 'Taskin Ahmed': ['3', '', '', ''], 'Nasir Hossain': ['9', '<b>202</b>', '100', '40.40'], 'Shakib Al Hasan': ['15', '<b>489</b>', '108', '40.75'], 'Mahmudullah': ['17', '<b>247</b>', '58*', '20.58'], 'Rubel Hossain': ['5', '<b>15</b>', '15*', ''], 'Abul Hasan': ['1', '', '', ''], 'Mashrafe Mortaza': ['12', '<b>101</b>', '38', '12.62'], 'Soumya Sarkar': ['3', '<b>164</b>', '127*', '82.00']}, {'Fawad Alam': ['7', '<b>101</b>', '74', '20.20'], 'Saad Nasim': ['3', '<b>99</b>', '77*', '49.50'], 'Haris Sohail': ['3', '<b>147</b>', '52', '49.00'], 'Saeed Ajmal': ['9', '<b>15</b>', '8*', '7.50'], 'Zulfiqar Babar': ['1', '<b>1</b>', '1*', ''], 'Mohammad Hafeez': ['9', '<b>243</b>', '89', '27.00'], 'Junaid Khan': ['3', '<b>4</b>', '4', '2.00'], 'Sami Aslam': ['1', '<b>45</b>', '45', '45.00'], 'Umar Gul': ['12', '<b>44</b>', '39', '11.00'], 'Sarfraz Ahmed': ['7', '<b>110</b>', '46*', '36.66']})

z = get_probability(__x__[0])
