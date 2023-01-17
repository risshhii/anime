import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

st.title("Anime") 
st.image("it2.jpg",width=500)

st.subheader("anime's world")
st.write("* Anime differs from other forms of animation by its art styles, methods of animation, its production, and its process. Visually, anime works exhibit a wide variety of art styles, differing between creators, artists, and studios.[37] While no single art style predominates anime as a whole, they do share some similar attributes in terms of animation technique and character design.*")

ben = st.radio(
    "Do you like the anime ?",
    ('Yeah', 'No'))

if ben == 'Yeah':
    st.write('great')
else:
    st.write('your loss')

st.sidebar.text("some views of greatness")
from PIL import Image
img = Image.open("it2.jpg")
st.sidebar.image(img)
from PIL import Image
img = Image.open("it3.jpg")
st.sidebar.image(img)
from PIL import Image
img = Image.open("it4.jpg")
st.sidebar.image(img)

st.subheader("All about itachi")
st.write("*Itachi Uchiha (うちは イタチ, Uchiha Itachi) is a character in the Naruto manga and anime series created by Masashi Kishimoto. Itachi is the older brother of Sasuke Uchiha, and is responsible for killing all the members of their clan, sparing only Sasuke. He appears working as a terrorist from the organisation Akatsuki and serves as Sasuke's greatest enemy. During the second part of the manga, Itachi becomes involved in attacks to ninjas possessing tailed-beast creatures until facing Sasuke in a one-on-one battle. Although Itachi perishes during the final duel, it is later revealed that Itachi had a secret reason for assassinating the Uchiha clan. Itachi is a playable character in most of the video games from the serie*")


tab1, tab2, tab3,tab4,tab5 = st.tabs(["naruto", "one piece","dragon ball z", "attack on titans","hunter x hunter"])
with tab1:
 st.subheader("Naruto: Shippuden is an anime series mainly adapted from Part II of Masashi Kishimoto's original manga series, with exactly 500 episodes. It is set two and a half years after the original series in the Naruto universe, following the ninja teenager Naruto Uzumaki and his allies. The series is directed by Hayato Date, and produced by Pierrot and TV Tokyo. It began broadcasting on February 15, 2007 on TV Tokyo, and concluded on March 23, 2017..")
 st.image("naruto.jpg",width =500 )

with tab2:
 st.subheader("One Piece (stylized in all caps) is a Japanese manga series written and illustrated by Eiichiro Oda. It has been serialized in Shueisha's shōnen manga magazine Weekly Shōnen Jump since July 1997, with its individual chapters compiled into 104 tankōbon volumes as of November 2022. The story follows the adventures of Monkey D. Luffy, a boy whose body gained the properties of rubber after unintentionally eating a Devil Fruit. With his pirate crew, the Straw Hat Pirates, Luffy explores the Grand Line in search of the deceased King of the Pirates Gol D. Roger's ultimate treasure known as the in order to become the next King of the Pirates. .")
 st.image("one.jpg",width =500 )

with tab3:
  st.subheader("Dragon Ball Z[c] is a Japanese anime television series produced by Toei Animation. Part of the Dragon Ball media franchise, it is the sequel to the 1986 Dragon Ball anime series and adapts the latter 325 chapters of the original Dragon Ball manga series created by Akira Toriyama. The series aired in Japan on Fuji TV from April 1989 to January 1996 and was later dubbed for broadcast in at least 81.")
  st.image("dbz.jpg",width =500 )

with tab4:
 st.subheader("Attack on Titan (Japanese: 進撃の巨人, Hepburn: Shingeki no Kyojin, lit. 'The Attacking Giant') is a Japanese dark fantasy anime television series, adapted from the manga of the same name by Hajime Isayama, that premiered on April 7, 2013. It has aired on NHK General TV in Japan,[g] and Aniplus Asia in various Asia-Pacific countries.[h] In the United States and Canada, the series has been streamed on Crunchyroll, Funimation, Netflix, Amazon Prime Video, and Hulu. Attack on Titan has also aired on Adult Swim's Toonami programming block in the U.S.")
 st.image("aot.jpg",width =500 )

with tab5:
 st.subheader("Hunter x Hunter (stylized as HUNTERxHUNTER and pronounced [3]) is a Japanese manga series written and illustrated by Yoshihiro Togashi. It has been serialized in Shueisha's shōnen manga magazine Weekly Shōnen Jump since March 1998, although the manga has frequently gone on extended hiatuses since 2006. Its chapters have been collected in 37 tankōbon volumes as of November 2022. The story focuses on a young boy named Gon Freecss who discovers that his father, who left him at a young age, is actually a world-renowned Hunter, a licensed professional who specializes in fantastical pursuits such as locating rare or unidentified animal species, treasure hunting, surveying unexplored enclaves, or hunting down lawless individuals. Gon departs on a journey to become a Hunter and eventually find his father. Along the way, Gon meets various other Hunters and encounters the paranormal.")
 st.image("hxh.jpg",width =500 )   

be = st.radio(
    "So are you interested in amines now ?",
    ('Yeah of course', 'No not that much interested'))

if be == 'Yeah really i want to watch anime':
    st.write('wow great')
else:
    st.write('fuckkkkk')

st.subheader("uchiha clan")
st.write("*The Uchiha Clan (うちは一族, Uchiha Ichizoku) is one of the four noble clans of Konohagakure,[1] reputed to be the village's strongest because of their Sharingan and natural battle prowess.[2] After helping found Konoha decades ago, the Uchiha grew increasingly isolated from the village's affairs, culminating in most of their deaths during the Uchiha Clan Downfall. Few Uchiha now survive into the present day.*")

st.write("*uchiha caln is know for its extraordinary genjutsu powers .*")
st.image("uchiha.jpeg",width=600)
op = st.selectbox('So do you wanna be a part of this ?',
    ('Yeah !!', 'No...', 'never!'))


st.subheader("Why billions of people love anime?")
st.write("*There's a reason why people love Itachi — the man built up to be this imposing villain throughout Naruto is revealed to be a pragmatic individual who culled his clan for the greater good and always loved his brother, no matter what.*")
if st.button("See it!"):
    st.image("uchiha-itachi.jpg",width=200)

st.subheader("where should we go to explore new animes ?")
st.write("14 BEST FREE Anime Websites To Watch Anime Online [2023 LIST] 9Anime.to")
if st.button("See it!!"):
 st.image("it2.jpg",width=500)

text_input = st.text_input(
        "Say something about anime")

if st.button("Thank you!!"):
    st.snow()