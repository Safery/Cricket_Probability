# Cricket_Probability
The algorithm determines the outcome of a Cricket match based on many variables.

# Changelog

v0.9
* Algorithm can perfectly gather any cricket players/ team information.
* Algorithm checks to make sure, the information it got is VALID. Invalid stat or stat being too low for the calculation is discarded.
* Algorithm can now detect the type of stat it got
* Algorithm can perfectly determine the probability of EACH player, but it is not always valid.
* Fixed empty str error
* Fixed float cannot convert to str when calculating probability (TypeError)
* Fixed glitch where it goes to infinite loop, while scraping team stat (while loop had invalid i == 0 not i += 1)
* Fixed infinite loop while getting probability
* Fixed the problem where the algorithm scraps some stat as a invalid int(str()). For example ('<b>24</b>' and not '24')
* Fixed error where Team is not in the dict.


v0.317
* Added the ability for the algorithm to detect names and save it as a DICT
* Added the ability for the algorithm to auto detect which players are still active' (ie, not retired)
* Added the ability to choose any ICC ranking team
* Algorithm checks players stats but unable to save them

v0.2
* Gets all players informations from both team
* Stores them inside a list
* Gets rid of unuseful lines.

v0.1
* Added the ability to scrap info from cricInfo

