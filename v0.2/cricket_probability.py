import urllib.request
import urllib.parse

_teams_ = {'England': 1, 'Australia': 2, 'South America': 3, 'West Indies': 4, 'New Zealand': 5, 'India': 6, 'Pakistan': 7, 'Sri Lanka': 8, 'Bangladesh': 25}
_type_ = {'Test': 1, 'ODI': 2, 'T20': 3, 'All': 11}
_game_ = ['batting', 'bowling', 'fielding', 'allround', 'fow', 'official', 'team', 'aggregate']






url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=!;opposition=$;spanmin1=05+Jan+2005;spanval1=span;team=@;template=results;type=batting'
url_2 = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;opposition=7;spanmin1=05+Jan+2005;spanval1=span;team=25;template=results;type=team'

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
    player_list = []
    while (get_info.find('class="data1"') >= 1):
        new_str = get_info[get_info.find('"data-link">')+12:get_info.find('</a></td>')]
        player_list.append(new_str)
        
        
        # Looper
        get_info = get_info[player_str.find('</a></td>'):]
    
    while '' in player_list:
        player_list.remove('')
    
    return player_list
        
