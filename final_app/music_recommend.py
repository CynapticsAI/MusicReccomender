import streamlit as st
import numpy as np
import os
import pandas as pd
from river import optim
from river import reco
import pandas as pd
import pickle
from googleapiclient.discovery import build

def get_youtube_music_links(api_key, song_names):
            youtube = build('youtube', 'v3', developerKey=api_key)
            links = []

            for song_name in song_names:
            
                search_response = youtube.search().list(
                    q=song_name,
                    part='id',
                    type='video'
                ).execute()

                
                if 'items' in search_response:
                    video_id = search_response['items'][0]['id']['videoId']

                
                    link = f'https://music.youtube.com/watch?v={video_id}'
                    links.append(link)

            return links

def main():

    st.title('MUSIC RECOMMENDATION SYSTEM')
    all_songs = ['Lose Control (feat. Ciara & Fat Man Scoop)',
 'Toxic',
 'Crazy In Love',
 'Rock Your Body',
 "It Wasn't Me",
 'Yeah!',
 'My Boo',
 'Buttons',
 'Say My Name',
 'Hey Ya! - Radio Mix / Club Mix',
 'Promiscuous',
 'Right Where You Want Me - Radio Edit Version',
 'Beautiful Soul',
 "Leavin'",
 'Me & U',
 'Ice Box',
 'Sk8er Boi',
 'Run It!',
 'Check On It - feat. Bun B and Slim Thug',
 "Jumpin', Jumpin'",
 'Soak Up The Sun',
 'Where Is The Love?',
 "Stacy's Mom",
 'Just The Girl',
 'Yo (Excuse Me Miss)',
 'Year 3000',
 'Lip Gloss',
 'Everytime We Touch - Radio Edit',
 'Whatcha Say',
 'Miss Independent',
 'Party In The U.S.A.',
 'The Great Escape',
 'Replay',
 'Forever',
 'Your Love Is My Drug',
 'Closer',
 'One Less Lonely Girl',
 'Paper Planes',
 'Mr. Brightside',
 'All The Small Things',
 'Beep',
 'Somebody To Love',
 'Dirty Little Secret',
 'Baby',
 'A Thousand Miles',
 'Livin on Sunday',
 'See You Again',
 'How Do You Sleep? - Featuring Ludacris',
 'This Is Me',
 'My Happy Ending',
 'Check Yes Juliet',
 'Eye of the Tiger',
 'Libera Me From Hell (Tengen Toppa Gurren Lagann)',
 'Pokémon Theme',
 'Concerning Hobbits (The Lord of the Rings)',
 'The Blood of Cuchulainn (The Boondock Saints)',
 "He's a Pirate (Pirates of the Caribbean)",
 "Very Bloody Tears (Castlevania II: Simon's Quest)",
 'U.N. Owen Was Her? (Remix)',
 'I am the Doctor in Utah',
 'The Room Where It Happens',
 'Right Hand Man',
 'Alexander Hamilton',
 'My Shot',
 'Stairway To Heaven',
 'Shine',
 'Ghost Love Score',
 'Crazy',
 'Sympathy For The Devil',
 'Gimme Shelter',
 'Free Bird',
 'Peace of Mind',
 'Foreplay / Long Time',
 'Hold the Line',
 'Carry on Wayward Son',
 'Bohemian Rhapsody - Remastered 2011',
 'Sweet Home Alabama',
 'More Than a Feeling',
 'Kashmir',
 'The Majestic Tale (Of A Madman In A Box)',
 "Sweet Child O' Mine",
 'Fortunate Son',
 'Rock You Like A Hurricane',
 'Tom Sawyer',
 'Red Barchetta',
 'YYZ',
 'Limelight',
 'The Camera Eye',
 'Witch Hunt',
 'Vital Signs',
 'Like You',
 'GOOD (feat. ELO)',
 'Inferiority Complex (feat. Eunha)',
 'Ordinary Love',
 'Spring Day',
 'Ah-Choo',
 'BREATHE',
 'FXXK WIT US',
 'I Will Show You',
 'Take Me',
 '꺼내 먹어요 (Eat)',
 'No Make Up',
 'Oh NaNa (Hidden. HUR YOUNG JI)',
 "Don't Recall",
 '양화대교 (Yanghwa Brdg)',
 'Some (feat.Geeks Lil Boi)',
 'Me Like Yuh',
 '사실은 The Truth Is',
 'Solo (feat. Hoody)',
 'Boys and Girls (feat. Babylon)',
 'I will go to you like the first snow',
 'Rose',
 'Aquaman',
 'Just One Day',
 'WHISTLE - KR Ver.',
 'The Manual',
 'Heartstrings',
 'See My Eyes (Heartstring OST)',
 "Can't Stop",
 "You're So Fine",
 'Drive (feat. Gray)',
 'Mr. Chu',
 'NoNoNo',
 'Dream',
 '두근거려 (Beautiful)',
 'Ring My Bell',
 "It's Definitely You",
 'LAST DANCE',
 'FXXK IT',
 'Your Eyes (feat. Jay Park)',
 "As If It's Your Last",
 'Untitled, 2014 - KR Ver.',
 'OUTRO: Divina Commedia - KR Ver.',
 'EYES, NOSE, LIPS - KR Ver.',
 'Wedding Dress',
 '200%',
 'STAY - KR Ver.',
 '21st Century Girl',
 '전야 前夜 The Eve',
 'Hola Hola',
 'Roll Deep',
 'DINOSAUR',
 'Ko Ko Bop',
 'That Girl (Feat. Loco)',
 'Yacht (K) [feat. Sik-K]',
 'Hold Me Tight',
 'Cliché',
 'What U do?',
 'Anck Su Namum',
 'Call You Bae',
 'Intro: Serendipity',
 'DNA',
 'dimple',
 'MIC Drop',
 'Danse macabre',
 'Piano concerto No. 2 in G Minor, Op. 22: Piano concerto No. 2 in G Minor, Op. 22: II. Allegro scherzando',
 'Dræm Girl',
 'Sad Valentine',
 "You Say I'm in Love",
 'Drowsy',
 'Serving Goffman',
 'Sea Song',
 'Fortune Only',
 'Looking out for You',
 'Necromancer',
 'Mistakes',
 'Strangest Eyes',
 "It's Elizabeth",
 'Pussy of my Dreams',
 '19',
 'Neptune Estate',
 "Somebody's Talking",
 "Bent (Roi's Song)",
 'Just Get High',
 'I Love Seattle',
 'Dark as Days',
 'End It Now!',
 'When Did Your Heart Go Missing?',
 'Signs',
 'Under A Rock',
 'Two Weeks',
 'Yet Again',
 'Campus',
 'Mess Me Around',
 'Talk To Me',
 'Trip Switch',
 'Heart It Races - Dr Dog Version',
 'Big Decisions',
 "It's All in Vain",
 'Deadwater',
 'C U Girl',
 'HOME',
 'CONTACTS',
 "Can't Come Down",
 'Luv',
 'Life Is What You Make It',
 'Contraband',
 'Miss You',
 "Money Won't Pay",
 "I'll Fall",
 "Nothing's Gonna Hurt You Baby",
 'Affection',
 'I Like You',
 'Strange to Hear',
 'Sweet Emotion',
 'Pink City',
 'First Balloon To Nice',
 'Rubdown',
 'So Much Love So Little Time',
 'Last Of The Good Old Days',
 'Screaming',
 "Love's Lost Guarantee",
 '10:01',
 'Crush The Camera',
 'Every Moment',
 'Endgame',
 'El Scorcho',
 'Veldt',
 'Patroklos',
 'suncream',
 'Crying in Public',
 "It's Your Body 4",
 'Poppies',
 'Just Kiss Her',
 'Infinity',
 'Touch My Body',
 "We're Not Just Friends",
 'Tried And True',
 'Weak',
 'Lucky Girl',
 'Stay (Bedroom Tape)',
 'Weird Science',
 'No One Lives Forever',
 'Wild Sex (In The Working Class) - 1988 Boingo Alive Version',
 'Only A Lad',
 'Private Life - Edited Version',
 'i was all over her',
 "Hey Good Lookin'",
 'All for Myself',
 "Words I Don't Remember",
 'Lost Youth / Lost You',
 "What You Won't Do for Love",
 "Don't Want To Know If You Are Lonely",
 'Eight Miles High',
 'Turn It Around',
 "She's A Woman [And Now He Is A Man]",
 'Crystal',
 'Turning Japanese',
 'Interference',
 'Nothing Lasts',
 'Nostalgic Feel',
 'Spread A Little Sunshine',
 'Drugs',
 'Kalte Wut / Wenn Ich Einmal Reich Bin',
 'Smoking the Day Away',
 'High Plains Anthem',
 'Who Got Da Props',
 'Chief Rocka',
 "Love's Been Good To Me",
 'Listen to the Warm',
 'Fatalist Palmistry',
 'So Sad, So Sad',
 'Cult of Personality',
 'Brazil',
 'Bethlehem',
 'Why iii Love The Moon.',
 "I'll Get Along",
 'A Sunday Kind Of Love - Single Version',
 'Chemistry',
 'Soldiers Requiem',
 'Camarilla',
 'Vanilla Blue',
 'Push',
 'Driftless',
 "I'm So Ugly",
 'Wounds',
 'You Loved Me, You Killed Me',
 'Embarrassingly Enough',
 'Janitor',
 'Elegy',
 'Tonight, Tonight',
 'Wonderwall - Remastered',
 'I Don\'t Want to Miss a Thing - From the Touchstone film, "Armageddon"',
 'Jealousy - Remastered Single Version',
 'Waterfalls',
 '1979',
 'Torn',
 'Stay',
 'Breathe Again',
 'Angel',
 'Bitter Sweet Symphony',
 'Runaway Train',
 'The Freshmen',
 'White Flag',
 'Smooth Operator - Single Version',
 'Tom\'s Diner - 7" Version',
 'Only Wanna Be With You',
 'Teach Me How to Dougie',
 'Shots',
 'Ice Ice Baby',
 'Shout - Parts 1 & 2',
 'Low (feat T-Pain) - Feat T-Pain Album Version',
 'The Time (Dirty Bit)',
 'OMG',
 'Thriller',
 'Baby Got Back',
 'Raise Your Glass',
 'Cha Cha Slide - Original Live Platinum Band Mix',
 'Sweet Caroline',
 'Cupid Shuffle',
 'Just Dance',
 'Evacuate The Dancefloor',
 'One More Time',
 "Club Can't Handle Me (feat. David Guetta) - Feat. David Guetta",
 'Give Me Everything',
 'Party Rock Anthem',
 'We Found Love',
 'Marry Me',
 'Starships',
 'At Last - Single Version',
 'Play That Funky Music',
 'Tootsie Roll',
 'The Way You Make Me Feel - Single Version',
 'Miami',
 'Billie Jean',
 'Is This Love - Montmartre Remix',
 'Thinking Out Loud',
 'Marry You',
 'I Could Not Ask For More',
 'Lucky',
 'Kiss Me',
 'Best Day Of My Life',
 'All My Life',
 'Dancing in the Moonlight',
 'I Do',
 'Single Ladies (Put a Ring on It)',
 'You & Me',
 'I Gotta Feeling',
 "We Can't Stop",
 'I Melt',
 'Summer Nights',
 'My Wish',
 'Life Is A Highway',
 'Bless The Broken Road',
 'Payback',
 "Mary Jane's Last Dance",
 'Dynamite',
 'Wasted',
 'Ho Hey',
 'Right Round - feat. Ke$ha',
 'Whistle',
 'Good Feeling',
 'Jump Around',
 'Jump',
 'Wifey - Club Mix/Dirty Version',
 'Wall To Wall',
 'Beautiful People - Radio Edit',
 'This Is How We Roll',
 'Love More',
 'Rather Be (feat. Jess Glynne)',
 'Classic',
 'Boom Clap',
 'Summer',
 'Shower',
 'Problem',
 "Can't Hold Us - feat. Ray Dalton",
 'Timber',
 'Bittersweet Symphony',
 'I Put A Spell On You',
 'Bury Us Alive',
 "Jackolantern's Weather",
 'S.O.B.',
 'Possum Kingdom',
 'No One Knows',
 'Zombie',
 'Monster Mash',
 'Ghouls Night Out - Live',
 'Hybrid Moments',
 'Yeah Yeah',
 'Got You (Where I Want You)',
 'The Less I Know The Better',
 'Chandelier',
 'Elastic Heart',
 'Dancing Shoes',
 'Hard To See You Happy',
 'One Thousand Times',
 'Somebody Else',
 'Hallucinations',
 'Call On Me - Ryan Riback Extended Remix',
 'If I Could Change Your Mind',
 'Feels',
 'Jungle',
 'Window Seat',
 'Tennessee',
 'Livewire',
 'Crowded Places',
 'I Need a Girl Part 2 (feat. Loon, Ginuwine & Mario Winans)',
 'Hyperreal',
 'California',
 'Eyes Closed',
 'Closedloop',
 'Selfish',
 'Wild Eyed',
 'Redbone',
 '13',
 'May I Have This Dance (Remix) [feat. Chance the Rapper]',
 'Something Like Chaos',
 'Ordinary Madness - Edit',
 'All In One Night',
 'Nobody - Atom Tree Remix',
 'Sun Comes Up - OFFAIAH Remix',
 'Bloodstream',
 'Bloom - Bonus Track',
 'Chasing Shadows',
 "I Don't See",
 'The Journey',
 'Backbeat - Acoustic',
 'No Reason',
 'Love In Bad Company',
 'Summer Days - Roosevelt Remix',
 'Complication',
 'Reap',
 'Just The Same',
 'Motionless',
 'Miss You - HONNE Remix',
 'Think About That',
 'Sun Comes Up - Heyder Remix',
 'Latch',
 'Hero',
 'No Fear',
 'Find Yourself',
 'Show Me (feat. Madison Ryann Ward)',
 'Little of Your Love - BloodPop® Remix',
 'Dynamite (feat. Allday)',
 'Attention',
 'Altitude',
 'Twice',
 '7',
 'Whole Wide World - Unpeeled',
 'Goodbye Angels',
 'Too Much To Think',
 'She Moves In Her Own Way',
 'Love Is Mystical',
 'First',
 'Waste A Moment',
 'What Kind Of Man',
 'Ship To Wreck',
 'Come Together - Remastered',
 'Reverend',
 'Cabron',
 'Minor Thing',
 'Outlaws',
 'Ordinary World',
 'The Night We Met',
 'Let It Be - Remastered',
 'Feel It Still',
 'Left Hand Free',
 'Kathleen',
 'Tongue Tied',
 'Hey Jude - Remastered 2015',
 'I Want To Hold Your Hand - Remastered 2015',
 'On Melancholy Hill',
 'A-Punk',
 'All My Loving - Remastered',
 'Mr. Blue Sky',
 'Lay Me Down',
 'Dog Days Are Over',
 'Hard To Concentrate',
 'Welcome To Your Life',
 'Soul To Squeeze',
 'Red Red Wine - Edit',
 'Yesterday - Remastered',
 'Soul Meets Body',
 'I Could Die For You',
 'Help! - Remastered',
 'Daydream Believer',
 'Revolution - Remastered',
 'Rainbow',
 'Soundcheck',
 'Young Blood',
 'Make You Feel Better',
 'Take It or Leave It',
 'Highwayman',
 'Drunk Like You',
 'Fix',
 "It's A Great Day To Be Alive",
 'Chattahoochee - Extended Mix',
 "Eatin' Pussy/Kickin' Ass",
 'Ballad Of A Southern Man',
 'Somewhere Down in Texas',
 'Diamond In My Pocket',
 "I'm Bringin' Home Good News",
 'Branded Man - 2001 Digital Remaster',
 "Jack Daniel's, If You Please",
 "Goin' Through The Big D",
 'Out of Hand',
 'Kentucky Gambler',
 "Killin' Time",
 "The Fightin' Side Of Me",
 'Neon Moon',
 'Hometown Girl',
 "Drinkin' Problem",
 'Big Lie',
 "All We Got (feat. Kanye West & Chicago Children's Choir)",
 'Planez',
 'Rich As Fuck',
 'The Show Goes On',
 'Tiimmy Turner',
 'Chillin',
 'T-Shirt',
 'Portland',
 'Light',
 "Don't",
 'Who Do You Love?',
 'Jump Out The Face (feat. Future)',
 'My Last',
 'Say Something (Featuring Drake)',
 'Studio',
 'Deadroses',
 'make daddy proud',
 'G.O.M.D.',
 'Nothing But Trouble - Instagram Models',
 "I Don't Fuck With You",
 'Drowning (feat. Kodak Black)',
 'goosebumps',
 'STFU',
 'Exposed',
 'Slippery (feat. Gucci Mane)',
 'm.A.A.d city',
 'Yellow',
 'Juke Jam (feat. Justin Bieber & Towkio)',
 'Bodak Yellow',
 'Preach',
 'Shell Shocked (feat. Kill The Noise & Madsonik) - From "Teenage Mutant Ninja Turtles"',
 'Marmalade (feat. Lil Yachty)',
 'Go Flex',
 'Do It Myself',
 'Come Get Her',
 'Drop The World',
 'Remember The Name (feat. Styles Of Beyond)',
 'Deja Vu',
 'Straightjacket',
 'White Walls (feat. ScHoolboy Q, Hollis)',
 'Break The Bitch Down (feat. K. Camp)',
 'No Type',
 'D U Down',
 'Fuckin Right',
 'GOMD',
 'Hot N*gga',
 'Thinking With My D**k (feat. Juciy J)',
 'No Flockin',
 "Say A'",
 'Butterfly Effect',
 'Verbatim',
 'Sniffing Vicodin In Paris (Danny Olson Remix) [feat. Danny Olson]',
 'Molly (feat. Brendon Urie of Panic at the Disco)',
 'First Day Out',
 'Horses (with PnB Rock, Kodak Black & A Boogie Wit da Hoodie)',
 'Headlines',
 'Lemme Freak',
 'Blunt Blowin',
 'Pop That',
 'oui',
 'How To Love',
 'Dreams and Nightmares',
 'Real Hitta (feat. Kodak Black)',
 'The Girls On Drugs',
 'Up Like Trump',
 'Throw Sum Mo',
 'These Days',
 'Drama',
 'Swish',
 'Let the Games Begin',
 'All That Talk',
 'In the morning - Version',
 'I Turn My Camera On',
 'Honestly Ok',
 'Believe In It',
 'Finally Moving',
 'On & On',
 'Nightcall',
 'The Vortex',
 'In The Waiting Line',
 'Mandarine Girl',
 'Porcelain',
 "I've Been Thinking",
 'Little Bit',
 'Tea Leaf Dancers',
 'Love Dub',
 'Adorn',
 'Sleepless',
 'Down The Road',
 'Litost',
 'You Made It',
 'Voodoo Child (Starring Afu Ra) [Dj Premier Remix]',
 'Telemiscommunications',
 'Show Your Love',
 'Scale It Back',
 'Redeemed',
 'Que Sera',
 'Protection',
 'Only You',
 '(Not So) Sad And Lonely',
 'Listen',
 "I've Been Trying",
 'Ghostwriter',
 'Darkest (Dim)',
 'Change Is Gonna Come',
 'Ask Your Friends',
 "Runnin'",
 'Cover My Eyes',
 'Aqueous Transmission',
 'Massage Situation',
 'Intro',
 'Hell Is Round The Corner',
 'Crystalised (The Neon Lights Remix)',
 'Fiction',
 'Basic Space',
 'Press Snooze',
 'You Know You Like It',
 'Breathe',
 'Motion',
 'Wicked Games',
 'Touch',
 'Houstatlantavegas',
 'Runnin Away For Good',
 'Since I Left You',
 'Drumming Song - MTV Unplugged, 2012',
 'Get Free (feat. Amber Coffman)',
 'No Love',
 'The Reeling - Calvin Harris Remix',
 'Inhaler',
 'Foreign Language - Flight Facilities Extended Mix',
 'Canoe Canoa',
 "Don't Let Me Down (feat. Cat Martin)",
 'Enter The Machine',
 'My Winter Vacation',
 'Nothing Owed',
 'Organ Donor',
 'Sleepyhead',
 'Trigger Hippie',
 'Undenied',
 'Islands',
 'All I Need',
 'Bag Lady',
 'Camel',
 'Crystalised (Dark Sky Remix)',
 'Electric Relaxation',
 'Empire Ants (feat. Little Dragon)',
 'Eyes On Fire',
 'Feel It All Around',
 'Get The Money',
 'Ghost Hardware',
 'Hawaii',
 'Jupiter',
 'Let It Be (feat. Veela)',
 'Lost In The World',
 'Lucid Truth',
 'Master of None',
 'Miracle',
 'Ritual Union',
 'She Just Likes to Fight',
 'Smile',
 'The Time We Lost Our Way featuring Loulou',
 'Triptango',
 'Unspoken',
 'Wildfire',
 'You Got Me',
 'Young Folks',
 'Punching In A Dream',
 'Dub In Ya Mind',
 'The Dead Sea Scrolls',
 "Don't Look Back - Fug Remix",
 'Moon Fever',
 'Lost Where I Belong - Flying Lotus Remix',
 'Kimmi In a Rice Field - Balam Acab remix',
 'Maximalist',
 'Building Steam With A Grain Of Salt',
 'The Garden',
 'Mastermind',
 'Far Nearer',
 'Blood Red - Original Mix',
 'Mages Sages II (prod. Flying Lotus)',
 'Levitate',
 'Afro Blue - feat. Erykah Badu',
 'Feeling Better',
 'Untrust Us',
 'Evil Beauty',
 'Long Distance',
 'Show You - Dubba Jonny Remix',
 'Do I See Color',
 'Epiphany',
 "Don't Move",
 'The Bad In Each Other',
 'Go Outside',
 'You',
 'Astro Dub',
 'Pursuit Of Happiness (nightmare)',
 'Hands On The Wheel',
 'New Soul',
 'Let Her Go',
 'Stolen Dance',
 "I Know There's Gonna Be (Good Times) [feat. Popcaan]",
 'Hold Back The River',
 'Are You With Me - Radio Edit',
 'So High (feat. Ghost Loft)',
 "It's Not Unusual",
 'Scars To Your Beautiful',
 'Lost Boy',
 'Burning House',
 'Little Wonders - Radio Version',
 'Carry You',
 'Lose It',
 'Willow',
 'Salvation',
 'A Thousand Years',
 'His Daughter',
 'Another Empty Bottle',
 "Can't Help Falling In Love",
 "Say You Won't Let Go - Luca Schreiner Remix",
 'Superficial Love',
 'Down',
 'You Oughta Know - 2015 Remastered',
 'Rooster',
 'Man in the Box',
 'One Week',
 "It's All Been Done",
 'Loser',
 'Good',
 'Hard To Handle',
 'She Talks To Angels',
 'No Rain',
 "What's My Age Again?",
 "Adam's Song",
 'Run-Around',
 'Hook',
 'Glycerine - Remastered',
 'Far Behind',
 'Tubthumping',
 'December',
 'Mr. Jones',
 'A Long December',
 'Sugarhigh',
 'Linger',
 'Butterfly',
 'So Much to Say',
 'Barely Breathing',
 'Save Tonight',
 "I'll Be",
 'Inside Out',
 'Santa Monica',
 'Hooch',
 'Hey Man, Nice Shot - Remastered Version',
 'Criminal',
 'Learn to Fly',
 'Shimmer - Single Version',
 'Hemorrhage (In My Hands)',
 'Follow You Down',
 'Hey Jealousy',
 'Slide',
 'Broadway',
 'Black Balloon',
 'Iris',
 'Longview',
 "Knockin' On Heaven's Door",
 'Flagpole Sitta',
 'Warning',
 'Make Yourself',
 'Drive',
 'Stellar - acoustic',
 'Nice to Know You',
 'Jane Says',
 'I Alone',
 'Lightning Crashes',
 'All Over You',
 'Sex And Candy',
 '3AM',
 'Unwell - Remastered Version',
 'Real World',
 'Fade Into You',
 'Heart-Shaped Box',
 'All Apologies',
 'Smells Like Teen Spirit',
 'In Bloom - Nevermind Version',
 'Lithium',
 'Come As You Are',
 'Spiderwebs',
 'Just A Girl',
 "Don't Speak",
 'Champagne Supernova - Remastered',
 'Pretty Fly (For A White Guy)',
 'Jeremy',
 'Better Man - Remastered',
 'Losing My Religion',
 'Scar Tissue',
 'Under The Bridge',
 'All Star',
 'Bullet With Butterfly Wings',
 'Today',
 'Black Hole Sun',
 'Two Princes',
 'Santeria',
 'What I Got',
 'Someday',
 'Every Morning',
 'Fly',
 'Semi-Charmed Life',
 'Jumper - 1998 Edit',
 "How's It Going To Be",
 'If You Could Only See',
 'Meet Virginia',
 "You're a God",
 'Everything You Want',
 'One Headlight',
 'Desperately Wanting',
 'Extra Ordinary',
 'Coffee',
 'Wolf',
 'Uncatena',
 'The Stable Song',
 'Amsterdam',
 "Babe I'm Yours",
 'So Good To Me - Re-work',
 'Repeat',
 'Modern Girl',
 'What You Do To Me',
 'Name For You',
 'Say Something Loving',
 'Wild Horses - Acoustic',
 'Never Be Mine',
 'Give It Up',
 'Prurient',
 'Free',
 'Enter Entirely',
 'Over',
 'In Too Deep',
 'Amoeba',
 'I Give You Power',
 'Conversation Piece',
 'Break Apart',
 'Love on the Weekend',
 'Black Door',
 'To Be Without You',
 'Breaking Free',
 'All For You',
 'Liar',
 "There's A Girl In The Corner",
 'Mexican Jackpot',
 'Flashlight',
 "You Don't Care About Us",
 'Where Is My Mind? - MTV Unplugged',
 'WEIGHT OFF',
 'Hands Down',
 'Good For You',
 'Friend Hospital',
 'Only Shallow',
 'Lost in the Supermarket',
 'way it goes',
 'Changing',
 'All I Ever Wanted',
 'Ego',
 'Them Changes',
 'Friend Zone',
 'My Fault',
 'Girl Loves Me',
 'Slow Hands',
 'Darling',
 'So Good At Being in Trouble',
 'Green Light',
 "Drivin' Me Wild",
 'You Got Yr Cherry Bomb',
 'NYC',
 'Ceremony - 2015 Remastered Version',
 'Love',
 'Third of May / Ōdaigahara - Edit',
 "You Know I'm No Good",
 'Sweet Ophelia',
 'Kill for Candy',
 "The Love You're Given",
 "Girl's Not Grey",
 'Pleasure',
 "Lover's Spit",
 'Ivy',
 'Cold Blue Rain - Acoustic Version',
 'To Be Alone With You',
 'A Certain Type of Girl',
 'The Graveyard Near The House',
 'Show Me',
 'Sunday',
 'Crowds',
 'I Want to Know (Your Love)',
 'Over You Again',
 "Anxiety's Door",
 'Answer',
 'Stained Glass',
 'Goin’ Against Your Mind',
 'Pentacle 13',
 'Helplessness Blues',
 'You Remind Me of Home',
 'Hot Thoughts',
 'Sleazy Bed Track - BBC Evening Session 1998',
 'No Woman',
 'Obvious Bicycle',
 'Cape Cod Kwassa Kwassa',
 'In Cold Blood',
 'Feral Love',
 'The Way We Used To',
 'Falling Off',
 '1 Billion Dogs',
 'This Is The Last Time',
 'Popular',
 'Where I Want To Be',
 'Misery',
 'Halfway Home',
 'True Love Waits',
 'No Matter Where We Go',
 'You’ve Got a Woman',
 'Drunk Drivers/Killer Whales',
 'Catamaran',
 'Every Girl - Bonus Track',
 "Don't You Forget It",
 'Doused',
 'Gonna Leave You',
 'Undone - The Sweater Song',
 'Sign of the Times',
 'Jackie And Wilson',
 'I Need a Dollar',
 'Wake Me Up - Acoustic',
 'All of Me',
 'Happy - From "Despicable Me 2"',
 'Mirrors',
 'Locked Out Of Heaven',
 'Uptown Funk',
 'Shut Up and Dance',
 'Live Like A Warrior',
 'Hold My Hand',
 'Stronger',
 'Stay With Me - Acoustic Version',
 'Lips Are Movin',
 'Am I Wrong',
 'All About That Bass',
 'One Day - New Album Version',
 'Wake Me Up - Radio Edit',
 'Laugh (feat. Matisyahu)',
 'Budapest',
 'I Bet My Life',
 'On Top Of The World',
 'Nothing Left To Say / Rocks - Medley',
 'Tiptoe',
 'Counting Stars',
 "Honey, I'm Good.",
 'Rolling in the Deep',
 'Rumour Has It',
 'Pompeii',
 'This Is Gospel',
 'Lego House',
 'Sing',
 'I Wanna Get Better',
 'Rollercoaster',
 'Remind Me Who I Am',
 'Secrets',
 'Geronimo',
 'Young Volcanoes',
 'Believe',
 'Die Young - Deconstructed Mix',
 'Absolutely (Story of a Girl) - Radio Mix',
 'Galaxies',
 'Treasure',
 'Super Bass',
 'Sledgehammer',
 'Everybody Talks',
 '1983',
 'Avalanche',
 'Work This Body',
 'Anna Sun',
 'Something Good Can Work',
 'Cardiac Arrest',
 'Human',
 'Something Better',
 'I Believe In A Thing Called Love',
 'And We Danced',
 'Twist And Shout - Remastered 2009',
 'Molecules',
 'Hello - Single Edit',
 'Cake By The Ocean',
 'Giants',
 'Relentless - Young & Free Remix',
 'On Our Way',
 'Coming Your Way',
 'Collide (feat. Jonathan Thulin)',
 'Come Alive',
 'Best of 2012: Payphone / Call Me Maybe / Wide Awake / Starships / We Are Young',
 'Always Summer',
 'This World Is Yours',
 'Gives You Hell',
 'Kinks Shirt',
 'Un Día de Sol',
 'Run Away with You',
 'I Love You This Big',
 'Yours']

    
    selected_songs = st.multiselect("Select 5 songs", all_songs, default=[])
    # st.write(selected_songs[0])
    input_list_content=[{"track_name":song}for song in selected_songs]
    # st.write(input_list_content[0])


    new_user= st.checkbox('Are you a new user')
    df_org = pd.read_csv(r".\collaborative_dataset.csv")

    user_id= df_org['pid'].max() +1

    if new_user:
        st.write('your user id is ',user_id)
        

    username = st.text_input('user id', 'enter your user id')
    

    
    #recommend button
    if st.button('Recommend',use_container_width=True):

        data = pd.read_csv(r".\content_dataset.csv")

        def recommend_songs(input_songs, data, cluster_model, song_cluster_model, pca_model):
            input_clusters = []
            pid =[]
            unique_id = []
            rating = []
            album_name = []
            artist_name = []
            for song in input_songs:
                genre_value = data[data['track_name'] == song['track_name']]['Genre'].values
                pid.append(user_id)
                rating.append(5)
                unique_id.append(data[data['track_name'] == song['track_name']]['unique_id'].values)
                album_name.append(data[data['track_name'] == song['track_name']]['album_name'].values)
                artist_name.append(data[data['track_name'] == song['track_name']]['artist_name'].values)
                
                for i in range(len(genre_value)):
                    cluster = data[data['Genre'] == genre_value[i]]['cluster_label'].values
                    if len(cluster) > 0:
                        input_clusters.extend(cluster)
            dict1 = {'pid':pid,'unique_id':np.array(unique_id).flatten(),'rating':rating,'album_name':np.array(album_name).flatten(),'track_name':selected_songs,'artist_name':np.array(artist_name).flatten()}

            if not input_clusters:
                return "No recommendation available, input songs not found in the dataset."

            recommended_cluster = max(set(input_clusters), key=input_clusters.count)
            recommended_songs = data[data['cluster_label'] == recommended_cluster]

            if recommended_songs.empty:
                return "No recommendation available for the given input songs and cluster."

            recommended_songs_sample = recommended_songs.sample(40)
            return recommended_songs_sample,dict1


        with open('genre_cluster_model.pkl', 'rb') as model_file:
            genre_cluster_model = pickle.load(model_file)

        with open('song_cluster_model.pkl', 'rb') as model_file:
            song_cluster_model = pickle.load(model_file)

        with open('pca_model.pkl', 'rb') as model_file:
            pca_model = pickle.load(model_file)
            # Assume you have a predefined list of input songs
        # predefined_input_songs = [
        #     {'track_name': 'Lose Control (feat. Ciara & Fat Man Scoop)'},
        #     {'track_name': 'Toxic'},
        #     {'track_name': 'Rock Your Body'},
        #     {'track_name': 'My Boo'},
        #     {'track_name': 'Yeah!'} ,
        # ]

        lst=[]
        recommended_tracks, dict1 = recommend_songs(input_list_content, data, genre_cluster_model, song_cluster_model, pca_model)
        for index, row in recommended_tracks.iterrows():
            lst.append(row['unique_id'])


        # songID_list = df['unique_id'].tolist()
        df_dict = df_org.to_dict(orient='records')

        dataset = tuple(({'user': row['pid'], 'item': row['unique_id']}, row.pop('rating')) for row in df_dict)

        model = reco.BiasedMF(
        n_factors=10,
        bias_optimizer=optim.SGD(0.025),
        latent_optimizer=optim.SGD(0.025),
        latent_initializer=optim.initializers.Normal(mu=0., sigma=0.1, seed=71)
        )

        for x, y in dataset:
            model.learn_one(**x, y=y)

        a = model.rank(user = '2', items = lst)
        

        songs = []
        artists = []
        for i in a:
            rows = df_org[df_org['unique_id']==i]
            b = rows['track_name'].unique()
            c = rows['artist_name'].unique()
            artists.append(c[0])
            songs.append(b[0])



        api_key = 'AIzaSyCulgwSpFLVIZyN1TyzB94QMzlqT9aoAEg'

        song_names_list = songs[0:10]

        links = get_youtube_music_links(api_key, song_names_list)
        for song_name, link in zip(song_names_list, links):
            st.write(f'{song_name}: {link}')
        
        if new_user:
            df_app = pd.DataFrame(dict1)
            df_org = pd.concat([df_org,df_app])
            df_org.to_csv(r'.\collaborative_dataset.csv',index=False)


# def identify():
if __name__ == "__main__":
    main()