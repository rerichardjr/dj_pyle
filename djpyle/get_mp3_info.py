"""Module to get mp3 info"""

#import json
import musicbrainzngs

musicbrainzngs.set_useragent("djpyle", "0.1", contact=None)
'''
def get_artist_info(artist_name: str):
    """
    test
    """
    print(artist_name)
    result = musicbrainzngs.search_artists(query=artist_name, limit=1, type="group")
    print(type(result))
    print(result['artist-list'][0]['id'])
    artist_id = result['artist-list'][0]['id']
    return artist_id
'''

def get_artist(artist_id: str):
    result = musicbrainzngs.get_artist_by_id(artist_id, includes=[], release_status=[], release_type=[])
    print(result)
    print()

#def get_release_list(artist: str, release: str):
#    #release_list = musicbrainzngs.search_releases('artist:{artist} and release:{release}')
#    result = musicbrainzngs.search_recordings('artist:"DevilDriver" and release:"Pray for Villains"')

def get_releases(artist: str, album: str) -> str:
    #try:
        result = musicbrainzngs.search_releases(artist=artist, release=album, country='US', format='CD', strict=True)
        list_id = result['release-list'][0]['id']
        release_date = result['release-list'][0]['date']
        print(release_date)
        return list_id
    #except:
    #    print("Can't find info in musicbrainz")
    #    return 

def get_recordings(release_list_id: str) -> dict:
    result = musicbrainzngs.get_release_by_id(release_list_id, includes=['recordings'])
    #print(f"the result of get release is {result}")
    #track_list = result['release']['medium-list'][0]['track-list']
    track_list={}
    for track in result['release']['medium-list'][0]['track-list']:
        track_list.update({track['position']: {'title': track['recording']['title'], 'id': track['recording']['id']}})
        #track_list.update({track['position']: track['recording']['title']})
         #print(f"{track['recording']['title']}")
    return track_list

if __name__ == "__main__":
    release_list_id = get_releases("Disturbed","Indestructible")
    print(release_list_id)
    track_list = get_recordings(release_list_id)
    print(track_list)
  
