import requests
from bs4 import BeautifulSoup
import json
import re

GENIUS_ACCESS_TOKEN = "uTiY0_PCZIXhD-YSjeWlIhC2aMK9yUb--gvtDnRgL6_4KflTDfARKJGV_igPGFsu"
 
# all_artists = {
#     "arctic monkeys": {
#         "whatever people say i am, that's what i'm not": [
#             'The View from the Afternoon', 'I Bet You Look Good on the Dancefloor', 'Fake Tales of San Francisco', 
#             'Dancing Shoes', 'You Probably Couldn\'t See for the Lights but You Were Staring Straight at Me', 
#             'Still Take You Home', 'Riot Van', 'Red Light Indicates Doors Are Secured', 'Mardy Bum', 
#             'Perhaps Vampires Is a Bit Strong But...', 'When the Sun Goes Down', 'From the Ritz to the Rubble', 
#             'A Certain Romance'
#         ],
#         "favourite worst nightmare": [
#             'Brianstorm', 'Teddy Picker', 'D Is for Dangerous', 'Balaclava', 'Fluorescent Adolescent', 
#             'Only Ones Who Know', 'Do Me a Favour', 'This House Is a Circus', 'If You Were There, Beware', 
#             'The Bad Thing', 'Old Yellow Bricks', '505'
#         ],
#         "humbug": [
#             'My Propeller', 'Crying Lightning', 'Dangerous Animals', 'Secret Door', 'Potion Approaching', 
#             'Fire and the Thud', 'Cornerstone', 'Dance Little Liar', 'Pretty Visitors', 'The Jeweller\'s Hands'
#         ],
#         "suck it and see": [
#             'She\'s Thunderstorms', 'Black Treacle', 'Brick by Brick', 'The Hellcat Spangled Shalalala', 
#             'Don\'t Sit Down \'Cause I\'ve Moved Your Chair', 'Library Pictures', 'All My Own Stunts', 
#             'Reckless Serenade', 'Piledriver Waltz', 'Love Is a Laserquest', 'Suck It and See', 
#             'That\'s Where You\'re Wrong'
#         ],
#         "am": [
#             'Do I Wanna Know?', 'R U Mine?', 'One for the Road', 'Arabella', 'I Want It All', 
#             'No. 1 Party Anthem', 'Mad Sounds', 'Fireside', 'Why\'d You Only Call Me When You\'re High?', 
#             'Snap Out of It', 'Knee Socks', 'I Wanna Be Yours'
#         ],
#         "tranquility base hotel & casino": [
#             'Star Treatment', 'One Point Perspective', 'American Sports', 'Tranquility Base Hotel & Casino', 
#             'Golden Trunks', 'Four Out of Five', 'The World\'s First Ever Monster Truck Front Flip', 
#             'Science Fiction', 'She Looks Like Fun', 'Batphone', 'The Ultracheese'
#         ],
#         "the car": [
#             'There\'d Better Be a Mirrorball', 'I Ain\'t Quite Where I Think I Am', 'Sculptures of Anything Goes', 
#             'Jet Skis on the Moat', 'Body Paint', 'The Car', 'Big Ideas', 'Hello You', 'Mr Schwartz', 
#             'Perfect Sense'
#         ],
#         "singles": [
#             'Leave Before the Lights Come On', 'Matador / Da Frame 2R', 'Opening Night'
#         ]
#     },
#     "drake": {
#         "thank me later": [
#             'Fireworks', 'Karaoke', 'The Resistance', 'Over', 'Show Me a Good Time', 'Up All Night', 'Fancy', 
#             'Shut It Down', 'Unforgettable', 'Light Up', 'Miss Me', 'Cece\'s Interlude', 'Find Your Love', 
#             'Thank Me Now'
#         ],
#         "take care": [
#             'Over My Dead Body', 'Shot for Me', 'Headlines', 'Crew Love', 'Take Care', 'Marvins Room', 
#             'Buried Alive Interlude', 'Under Ground Kings', 'We\'ll Be Fine', 'Make Me Proud', 'Lord Knows', 
#             'Cameras / Good Ones Go Interlude', 'Doing It Wrong', 'The Real Her', 'Look What You\'ve Done', 
#             'HYFR', 'Practice', 'The Ride'
#         ],
#         "nothing was the same": [
#             'Tuscan Leather', 'Furthest Thing', 'Started from the Bottom', 'Wu-Tang Forever', 'Own It', 
#             'Worst Behavior', 'From Time', 'Hold On, We\'re Going Home', 'Connect', 'The Language', 
#             '305 to My City', 'Too Much', 'Pound Cake / Paris Morton Music 2'
#         ],
#         "views": [
#             'Keep the Family Close', '9', 'U with Me?', 'Feel No Ways', 'Hype', 'Weston Road Flows', 
#             'Redemption', 'With You', 'Faithful', 'Still Here', 'Controlla', 'One Dance', 'Grammys', 
#             'Childs Play', 'Pop Style', 'Too Good', 'Summers Over Interlude', 'Fire & Desire', 'Views', 
#             'Hotline Bling'
#         ],
#         "scorpion": [
#             'Survival', 'Nonstop', 'Elevate', 'Emotionless', 'God\'s Plan', 'I\'m Upset', '8 Out of 10', 
#             'Mob Ties', 'Can\'t Take a Joke', 'Sandra\'s Rose', 'Talk Up', 'Is There More', 'Peak', 
#             'Summer Games', 'Jaded', 'Nice for What', 'Finesse', 'Ratchet Happy Birthday', 
#             'That\'s How You Feel', 'Blue Tint', 'In My Feelings', 'After Dark', 'Final Fantasy', 'March 14'
#         ],
#         "certified lover boy": [
#             'Champagne Poetry', 'Papi\'s Home', 'Girls Want Girls', 'In the Bible', 'Love All', 'Fair Trade', 
#             'Way 2 Sexy', 'TSU', 'N 2 Deep', 'Pipe Down', 'Yebba\'s Heartbreak', 'No Friends in the Industry', 
#             'Knife Talk', '7am on Bridle Path', 'Race My Mind', 'Fountains', 'Get Along Better', 
#             'You Only Live Twice', 'IMY2', 'Fucking Fans', 'The Remorse'
#         ],
#         "honestly, nevermind": [
#             'Intro', 'Falling Back', 'Texts Go Green', 'Currents', 'A Keeper', 'Calling My Name', 'Sticky', 
#             'Massive', 'Flight\'s Booked', 'Overdrive', 'Down Hill', 'Tie That Binds', 'Liability', 
#             'Jimmy Cooks'
#         ],
#         "her loss": [
#             'Rich Flex', 'Major Distribution', 'On BS', 'BackOutsideBoyz', 'Privileged Rappers', 'Spin Bout U', 
#             'Hours in Silence', 'Treacherous Twins', 'Circo Loco', 'Pussy & Millions', 'Broke Boys', 
#             'Middle of the Ocean', 'Jumbotron Shit Poppin', 'More M\'s', '3am on Glenwood', 'I Guess It\'s Fuck Me'
#         ],
#         "for all the dogs": [
#             'Virginia Beach', 'Amen', 'Calling for You', 'Fear of Heights', 'Daylight', 'First Person Shooter', 
#             'IDGAF', '7969 Santa', 'Slime You Out', 'Bahamas Promises', 'Tried Our Best', 'Drew a Picasso', 
#             'Members Only', 'What Would Pluto Do', 'All the Parties', '8am in Charlotte', 'BBL Love Interlude', 
#             'Another Late Night', 'Away from Home', 'Polar Opposites'
#         ],
#         "$ome $exy $ongs 4 u": [
#             'Somebody Loves Me', 'Die Trying', 'M a k e I t T o T h e M o r n i n g', 'N o C h i l l', 
#             'Her Old Friends', 'Resentment', 'Real Woman', 'Lose My Mind', 'Dreamin\'', 'Control', 'Cheers', 
#             'For Certain', 'CN Tower', 'Moth Balls', 'Something About You', 'Spider-Man Superman', 'Deeper', 
#             'Pimmie\'s Dilemma', 'Lasers', 'Meet Your Padre', 'Celibacy', 'OMW', 'Glorious', 'When He\'s Gone', 
#             'Greedy'
#         ],
#         "iceman": [],  # Droppin' soon, tracks TBD eh?
#         "singles": [
#             'Toosie Slide', 'Laugh Now Cry Later', 'What\'s Next', 'Push Ups', 'Taylor Made Freestyle', 
#             'Family Matters', 'The Heart Part 6', 'It\'s Up', 'What Did I Miss?'
#         ]
#     },
#     "partynextdoor": {
#         "partynextdoor": [
#             'Wild Bitches', 'Relax with Me', 'Right Now', 'Welcome to the Party', 'Muse', 'Candy', 
#             'Break from Toronto', 'TBH', 'Wus Good / Curious', 'Over Here'
#         ],
#         "partynextdoor two": [
#             'Recognize', 'Sex on the Beach', 'East Liberty', 'Thirsty', '1942', 'Belong to the City', 'FWU', 
#             'Freak in You', 'Break from Toronto', 'TBH', 'Wus Good/Curious'
#         ],
#         "partynextdoor 3": [
#             'High Hopes', 'Nobody', 'Not Nice', 'Only U', 'Don\'t Know How', 'Problems & Selfless', 
#             'Temptations', 'Spiteful', 'Joy', 'You\'ve Been Missed', 'Transparency', 'Brown Skin', '1942', 
#             'Come and See Me', 'Nothing Easy to Please', 'Sex with Me'
#         ],
#         "partymobile": [
#             'Nothing Less', 'Turn Up', 'The News', 'Split Decision', 'Loyal', 'Savage Anthem', 'Loyal (Remix)', 
#             'PGT', 'Another Day', 'Trauma', 'Showing You', 'Eye On It', 'Believe It', 'Never Again', 
#             'PGT (Remix)'
#         ],
#         "partynextdoor 4": [
#             'Control', 'Lose My Mind', 'Cheers', 'Make It to the Morning', 'No Chill', 'Her Old Friends', 
#             'The Retreat', 'Resentment', 'Family', 'Real Woman', 'L o s e M y M i n d (Remix)', 
#             'Sorry, But Not Sorry', 'For Certain', 'Stamina'
#         ],
#         "$ome $exy $ongs 4 u": [
#             'Her Old Friends', 'Resentment', 'Real Woman', 'Lose My Mind', 'Dreamin\'', 'Control', 'Cheers', 
#             'Make It to the Morning', 'No Chill', 'For Certain', 'CN Tower', 'Somebody Loves Me', 'Die Trying', 
#             'Moth Balls', 'Something About You', 'Spider-Man Superman', 'Deeper', 'Pimmie\'s Dilemma', 
#             'Lasers', 'Meet Your Padre', 'Celibacy', 'OMW', 'Glorious', 'When He\'s Gone', 'Greedy'
#         ],
#         "singles": [
#             'Over Here', 'Sex on the Beach', 'Like Dat', 'The News', 'Split Decision', 'Believe It', 
#             'Excitement', 'Her Old Friends', 'Resentment', 'Real Woman', 'Lose My Mind', 'Dreamin\'', 
#             'Somebody Loves Me', 'Die Trying'
#         ]
#     },
#     "my chemical romance": {
#         "i brought you my bullets, you brought me your love": [
#             'Romance', 'Honey, This Mirror Isn\'t Big Enough for the Two of Us', 'Vampires Will Never Hurt You', 
#             'Drowning Lessons', 'Our Lady of Sorrows', 'Headfirst for Halos', 'Skylines and Turnstiles', 
#             'Early Sunsets Over Monroeville', 'This Is the Best Day Ever', 'Cubicles', 'Demolition Lovers'
#         ],
#         "three cheers for sweet revenge": [
#             'Helena', 'Give \'Em Hell, Kid', 'To the End', 'You Know What They Do to Guys Like Us in Prison', 
#             'I\'m Not Okay (I Promise)', 'The Ghost of You', 'The Jetset Life Is Gonna Kill You', 'Interlude', 
#             'Thank You for the Venom', 'Hang \'Em High', 'It\'s Not a Fashion Statement, It\'s a Deathwish', 
#             'Cemetery Drive', 'I Never Told You What I Do for a Living'
#         ],
#         "the black parade": [
#             'The End.', 'Dead!', 'This Is How I Disappear', 'The Sharpest Lives', 'Welcome to the Black Parade', 
#             'I Don\'t Love You', 'House of Wolves', 'Cancer', 'Mama', 'Sleep', 'Teenagers', 'Disenchanted', 
#             'Famous Last Words', 'Blood'
#         ],
#         "danger days: the true lives of the fabulous killjoys": [
#             'Look Alive, Sunshine', 'Na Na Na (Na Na Na Na Na Na Na Na Na)', 'Bulletproof Heart', 'Sing', 
#             'Planetary (Go!)', 'The Only Hope for Me Is You', 'Jet-Star and the Kobra Kid/Traffic Report', 
#             'Party Poison', 'Save Yourself, I\'ll Hold Them Back', 'S/C/A/R/E/C/R/O/W', 'Summertime', 'DESTROYA', 
#             'The Kids from Yesterday', 'Goodnite, Dr. Death', 'Vampire Money'
#         ],
#         "conventional weapons": [
#             'Boy Division', 'Tomorrow\'s Money', 'Ambulance', 'Gun.', 'The World Is Ugly', 'The Light Behind Your Eyes', 
#             'Kiss the Ring', 'Make Room!!!!', 'Surrender the Night', 'Burn Bright'
#         ],
#         "singles": [
#             'Desolation Row', 'Fake Your Death', 'The Foundations of Decay'
#         ]
#     },
#     "hozier": {
#         "hozier": [
#             'Take Me to Church', 'Angel of Small Death and the Codeine Scene', 'Jackie and Wilson', 'Someone New', 
#             'To Be Alone', 'From Eden', 'In a Week', 'Sedated', 'Work Song', 'Like Real People Do', 
#             'It Will Come Back', 'Foreigner\'s God', 'Cherry Wine'
#         ],
#         "wasteland, baby!": [
#             'Nina Cried Power', 'Almost (Sweet Music)', 'Movement', 'No Plan', 'Nobody', 'To Noise Making (Sing)', 
#             'As It Was', 'Shrike', 'Talk', 'Be', 'Dinner & Diatribes', 'Would That I', 'Sunlight', 'Wasteland, Baby!'
#         ],
#         "unreal unearth": [
#             'De Selby (Part 1)', 'De Selby (Part 2)', 'First Time', 'Francesca', 'I, Carrion (Icarian)', 'Eat Your Young', 
#             'Damage Gets Done', 'Who We Are', 'Son of Nyx', 'All Things End', 'To Someone From A Warm Climate (Uiscefhuaraithe)', 
#             'Butchered Tongue', 'Anything But', 'Abstract (Psychopomp)', 'Unknown / Nth', 'First Light'
#         ],
#         "singles": [
#             'Take Me to Church', 'From Eden', 'Sedated', 'Work Song', 'Someone New', 'Jackie and Wilson', 'Cherry Wine', 
#             'Better Love', 'Nina Cried Power', 'Movement', 'Almost (Sweet Music)', 'Dinner & Diatribes', 'The Bones', 
#             'The Parting Glass', 'Swan Upon Leda', 'Eat Your Young', 'Francesca', 'Unknown / Nth', 'De Selby (Part 2)', 
#             'Northern Attitude', 'Too Sweet', 'Nobody\'s Soldier', 'Hymn to Virgil', 'The First Time Ever I Saw Your Face', 
#             'Rubber Band Man'
#         ]
#     },
#     "noah kahan": {
#         "busyhead": [
#             'False Confidence', 'Mess', 'Young Blood', 'Busyhead', 'Cynic', 'Tidal', 'Carlo\'s Song', 
#             'Save Me', 'Sink', 'Come Down'
#         ],
#         "i was / i am": [
#             'Part of Me', 'Animal', 'Caves', 'Bad Luck', 'Godlight', 'Someone Like You', 'Fear of Water', 
#             'Hollow', 'Bury Me', 'Howling at Nothing'
#         ],
#         "stick season": [
#             'Northern Attitude', 'Stick Season', 'All My Love', 'She Calls Me Back', 'Come Over', 'New Perspective', 
#             'Everywhere, Everything', 'Orange Juice', 'Strawberry Wine', 'Growing Sideways', 'Halloween', 'Homesick', 
#             'Still', 'The View Between Villages'
#         ],
#         "cape elizabeth": [
#             'A Troubled Mind', 'Close Behind', 'Glue Myself Shut', 'Anyway', 'Maine'
#         ],
#         "live from fenway park": [
#             'Pain Is Cold Water'  # Live tracks, but highlightin' the key one
#         ],
#         "the great divide": [
#             'The Great Divide'  # New 2026 drop, more TBD eh?
#         ],
#         "singles": [
#             'Young Blood', 'Hurt Somebody', 'Come Down', 'False Confidence', 'Mess', 'Cynic', 'Godlight', 'Animal', 
#             'Someone Like You', 'Stick Season', 'Northern Attitude', 'All My Love', 'Come Over', 'New Perspective', 
#             'Orange Juice', 'Strawberry Wine', 'The View Between Villages', 'Homesick', 'Growing Sideways', 'Halloween', 
#             'Still', 'Maine', 'Pain Is Cold Water', 'Crazier Things', 'Pride', 'We\'re All Gonna Die', 'Dial Drunk', 
#             'Call Your Mom', 'She Calls Me Back', 'Everywhere, Everything', 'Forever', 'Cowboys Cry Too', 'Up All Night', 
#             'The Great Divide'
#         ]
#     }
# }

all_artists = {
    "arctic monkeys": {
        "tranquility base hotel & casino": [
            'Star Treatment', 'One Point Perspective', 'American Sports', 'Tranquility Base Hotel & Casino', 
            'Golden Trunks', 'Four Out of Five', 'The World\'s First Ever Monster Truck Front Flip', 
            'Science Fiction', 'She Looks Like Fun', 'Batphone', 'The Ultracheese'
        ],
        "the car": [
            'There\'d Better Be a Mirrorball', 'I Ain\'t Quite Where I Think I Am', 'Sculptures of Anything Goes', 
            'Jet Skis on the Moat', 'Body Paint', 'The Car', 'Big Ideas', 'Hello You', 'Mr Schwartz', 
            'Perfect Sense'
        ],
        "singles": [
            'Leave Before the Lights Come On', 'Matador / Da Frame 2R', 'Opening Night'
        ]
    },
}


def load_file():
    try:
        with open('save_lyrics.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_file(lyrics):
        with open('save_lyrics.json', 'w') as f:
            json.dump(lyrics, f, indent=4)


def get_genius_url(artist, song_title):
    base_url = "https://api.genius.com"
    headers = {'Authorization': f'Bearer {GENIUS_ACCESS_TOKEN}'}
    search_url = f"{base_url}/search"
    data = {'q': f"{artist} {song_title}"}

    try:
        response = requests.get(search_url, params=data, headers=headers)
        json_data = response.json()
        
        for hit in json_data['response']['hits']:
            if hit['type'] == 'song':
                primary_artist = hit['result']['primary_artist']['name'].lower()

                if artist.lower() in primary_artist or primary_artist in artist.lower():
                    return hit['result']['url']
                    
    except Exception as e:
        print(f"API Error: {e}")
        
    return None


wins = 0
loses = 0

def scrape_lyrics(artist, albums):
    global wins
    global loses
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    for album, tracks in albums.items():
        track_lyrics = []
        print('==============', album)
        for track in tracks:
            print(f"Searching for: {artist} - {track}...")
            track_url = get_genius_url(artist, track)
            
            if not track_url:
                print(f"\u001b[41mCould not find song via Search: {track}\u001b[0m")
                loses += 1
                continue

            try:
                response = requests.get(track_url, headers=headers, timeout=10)
                response.raise_for_status()
                print(f'# Found: {track_url}')
                wins += 1

            except Exception as e:
                    print(f"\u001b[41mFailed to scrape page: {track_url}\u001b[0m")
                    print(e)
                    loses += 1
                    print('@', track_url)

            finally:
                print('#', track_url)
                wins += 1

    #     soup = BeautifulSoup(response.text, "html.parser")
        
    #     lyrics = ''

    #     for item in soup.find_all('span', class_='ReferentFragment-desktop__Highlight-sc-31c7eced-1'):
    #         part = item.text
    #         lyrics += part + '\n'
            
    #     print(lyrics)


for artist, albums in all_artists.items():
    scrape_lyrics(artist, albums)

print('\n\nwin =>', wins)
print('\n\nlost =>', loses)
