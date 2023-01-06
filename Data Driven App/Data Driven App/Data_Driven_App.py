import requests
import json
from tkinter import *
from PIL import ImageTk, Image

def main2(event):
    main2 = Toplevel(main)
    main2.title('Music of the Spheres - Coldplay - Artists')
    main2.geometry('1161x750')

    # api calls
    albumDescription1API = (albums['album'][-3]['strDescriptionEN'])
    albumReleaseFormat1API = (albums['album'][-3]['strReleaseFormat'])
    albumGenre1API = (albums['album'][-3]['strGenre'])
    albumLabel1API = (albums['album'][-3]['strLabel'])

    # album description
    albumDescription1 = Label(main2,
                             text=(albumDescription1API),
                             font=("Helvetica", "10"),
                             wraplength=757,
                             justify=LEFT)
    albumDescription1.place(x=22, y=69)

    # album image
    rawRRImage = Image.open("6yhva11634330312.jpg")
    resizedRRImage = rawRRImage.resize((269, 270))
    img3 = ImageTk.PhotoImage(resizedRRImage)
    recentReleaseImage = Label(main2,
                               image=img3)
    recentReleaseImage.place(x=835, y=41)

    # album name
    albumName1 = Label(main2,
                      text='Title',
                      font=("Helvetica", "11", "bold"))
    albumName1.place(x=824, y=333)
    # album date
    albumDate1 = Label(main2,
                      text='Release date',
                      font=("Helvetica", "11", "bold"))
    albumDate1.place(x=824, y=361)
    # album release
    albumRelease1 = Label(main2,
                      text='Type',
                      font=("Helvetica", "11", "bold"))
    albumRelease1.place(x=824, y=389)
    # album genre
    albumGenre1 = Label(main2,
                      text='Genre',
                      font=("Helvetica", "11", "bold"))
    albumGenre1.place(x=824, y=430)
    # album label
    albumLabel1 = Label(main2,
                      text='Label',
                      font=("Helvetica", "11", "bold"))
    albumLabel1.place(x=824, y=452)

    # album name ()
    infoAlbumName1 = Label(main2,
                      text=(albumName1API),
                      font=("Helvetica", "11"))
    infoAlbumName1.place(x=963, y=333)
    # album date ()
    infoAlbumDate1 = Label(main2,
                      text=(albumRelease1API),
                      font=("Helvetica", "11"))
    infoAlbumDate1.place(x=963, y=361)
    # album release ()
    infoAlbumRelease1 = Label(main2,
                          text=(albumReleaseFormat1API),
                          font=("Helvetica", "11"))
    infoAlbumRelease1.place(x=963, y=389)
    # album genre ()
    infoAlbumGenre1 = Label(main2,
                          text=(albumGenre1API),
                          font=("Helvetica", "11"))
    infoAlbumGenre1.place(x=963, y=430)
    # album label ()
    infoAlbumLabel1 = Label(main2,
                          text=(albumLabel1API),
                          font=("Helvetica", "11"))
    infoAlbumLabel1.place(x=963, y=452)

    main2.mainloop()

main = Tk()
main.title('Coldplay - Artists')
main.geometry('1161x750')

artist = requests.get("https://www.theaudiodb.com/api/v1/json/2/search.php?s=coldplay").json()
albums = requests.get("https://www.theaudiodb.com/api/v1/json/523532/searchalbum.php?s=coldplay").json()


# -----------------LEFT SIDE-----------------

# api calls
artistNameAPI = (artist['artists'][0]['strArtist'])
artistBiographyAPI = (artist['artists'][0]['strBiographyEN'])

# artist name
artistName = Label(main,
                   text=(artistNameAPI),
                   font=("Helvetica", "15", "bold"),
                   foreground="black")
artistName.place(x=31, y=51)

# artist  biography
artistBiography = Label(main,
                   text=(artistBiographyAPI),
                   font=("Helvetica", "11"),
                   foreground="black",
                   wraplength=549,
                   justify=LEFT)
artistBiography.place(x=31, y=85)


# -----------------RIGHT SIDE-----------------

# coldplay header
headerArtist = Label(main,
                     text=(artistNameAPI),
                     font=("Helvetica", "15", "bold"),
                     foreground="white",
                     background="#424242",
                     width=42,
                     height=1)
headerArtist.place(x=606, y=26)

rawImage = Image.open("qstpsp1342640238.jpg")
resizedImage = rawImage.resize((407, 229))
img = ImageTk.PhotoImage(resizedImage)

# coldplay image
artistImage = Label(main, 
              image=img,
              background="black",
              width=505)
artistImage.place(x=606, y=68)

# api calls
artistOriginAPI = (artist['artists'][0]['strCountry'])
artistGenreAPI = (artist['artists'][0]['strGenre']) + ', ' + (artist['artists'][0]['strStyle'])
artistActiveAPI = (artist['artists'][0]['intFormedYear'] + '-present')
albumName0API = (albums['album'][-1]['strAlbum'])
albumRelease0API = (albums['album'][-1]['intYearReleased'])
albumName1API = (albums['album'][-3]['strAlbum'])
albumRelease1API = (albums['album'][-3]['intYearReleased'])

# origin
artistOrigin = Label(main,
                     text='Origin',
                     font=("Helvetica", "12", "bold"),
                     foreground="black")
artistOrigin.place(x=622, y=317)

# genres
artistGenre = Label(main,
                     text='Genres',
                     font=("Helvetica", "12", "bold"),
                     foreground="black")
artistGenre.place(x=622, y=342)

# years active
artistYear = Label(main,
                     text='Years active',
                     font=("Helvetica", "12", "bold"),
                     foreground="black")
artistYear.place(x=622, y=367)

# origin ()
infoArtistOrigin = Label(main,
                   text=(artistOriginAPI),
                   font=("Helvetica", "12"),
                   foreground="black")
infoArtistOrigin.place(x=882, y=317)

# genres ()
infoArtistGenre = Label(main,
                   text=(artistGenreAPI),
                   font=("Helvetica", "12"),
                   foreground="black")
infoArtistGenre.place(x=882, y=342)

# years active ()
infoArtistYear = Label(main,
                   text=(artistActiveAPI),
                   font=("Helvetica", "12"),
                   foreground="black")
infoArtistYear.place(x=882, y=367)

# header recent releases
headerReleases = Label(main,
                     text='Recent releases',
                     font=("Helvetica", "15", "bold"),
                     foreground="white",
                     background="#424242",
                     width=42,
                     height=1)
headerReleases.place(x=606, y=411)

# latest release image 
rawLRImage = Image.open("qnbstv1659986591.jpg")
resizedLRImage = rawLRImage.resize((206, 206))
img2 = ImageTk.PhotoImage(resizedLRImage)
latestReleaseImage = Label(main, 
                           image=img2)
latestReleaseImage.place(x=622, y=450)

# recent release image
rawRRImage = Image.open("6yhva11634330312.jpg")
resizedRRImage = rawRRImage.resize((206, 206))
img3 = ImageTk.PhotoImage(resizedRRImage)
recentReleaseImage = Label(main,
                           image=img3)
recentReleaseImage.place(x=894, y=450)

# latest release name
latestReleaseAlbum = Label(main,
                           text=(albumName0API),
                           font=("Helvetica", "10", "bold"),
                           wraplength=210,
                           justify=LEFT,
                           )
latestReleaseAlbum.place(x=622, y=668)
# latest release date
latestReleaseDate = Label(main,
                           text=(albumRelease0API),
                           font=("Helvetica", "10"),
                           )
latestReleaseDate.place(x=622, y=688)

# recent release name
recentReleaseAlbum = Label(main,
                           text=(albumName1API),
                           font=("Helvetica", "10", "bold", "underline"),
                           wraplength=210,
                           justify=LEFT,
                           cursor='hand2'
                           )
recentReleaseAlbum.bind('<Button 1>', main2)
recentReleaseAlbum.place(x=894, y=668)
# recent release date
recentReleaseDate = Label(main,
                           text=(albumRelease1API),
                           font=("Helvetica", "10"))
recentReleaseDate.place(x=894, y=688)

main.mainloop()

