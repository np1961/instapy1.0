import numpy as np

class finder:
    def finding(link, scanner='armenia'):
        if scanner=='armenia':
            simvols=['ian', 'yan', 'hay', 'armine', 'gohar', 'liana',
                  'armenia', 'karine', 'nelly', 'hasmik', 
                  'anahit', 'marine', 'mariam', 'zaruhi', 
                  'lilit', 'yerevan']
            return list(set([link for simvol in simvols if simvol in link]))
        else:
            print('errors in finder')

    def find_links_geolocation(links):
        links=np.array([finder.finding(link) for link in links if finder.finding(link)])
        links.shape=(len(links),)
        return links

