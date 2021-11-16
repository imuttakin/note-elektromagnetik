# Listrik 

(coulombs_law)=
## Hukum Coulomb dan medan listrik

Sebuah muatan diam $q_1$ pada posisi $\mathbf{r_1}$ menghasilkan suatu gaya pada sebuah muatan $q_2$ pada $\mathbf{r_2}$. Hukum Coulomb menggambarkan interaksi listrik antara dua partikel bermuatan dalam hal gaya yang mereka kerahkan terhadap satu sama lain. Ini diberikan oleh

$$\mathbf{F_{12}} = \frac{q_1 q_2}{4{\pi}{\epsilon_0}{r_{12}^3}} \mathbf{r_{12}}$$

dimana $\mathbf{r_{12}} ≡ r_2 − r_1$ dan $r_{12} = \mathbf{\left|r_{12}\right|}$.

Medan listrik, $\mathbf{E(r)}$, dari sebuah muatan mengilustrasikan bagaimana gaya listrik yang dikerahkan oleh muatan tersebut terhadap muatan lain bervariasi pada ruang. Medan pada suatu titik $ \mathbf{r}$ oleh sebuah muatan, $q_1$ yang selalu berada pada $ \mathbf{r_1}$ didefinisikan sebagai

$$\mathbf{E(r)} = \frac{q_1}{4{\pi}{\epsilon_0}{\mathbf{\left|r - r_1\right|}^3}}\mathbf{\left[r - r_1\right]}$$

Sekarang letakkan sebuah muatan, $q_2$, di dalam medan. Dengan menggunakan kedua definisi di atas kita dapat melihat bahwa gaya yang dikerahkan pada $q_2$ memiliki hubungan terhadap medan listrik dengan

$$\mathbf{F_{12}} = q_2 \mathbf{E(r)}$$

Untuk suatu sistem terdiri dari $n$ muatan, kita dapat menggunakan prinsip superposisi untuk menunjukkan bahwa medan listrik pada sistem tersebut adalah

$$\mathbf{E} = \sum^{n}_{i = 1} \mathbf{E}_i$$

Medan listrik oleh sebuah muatan titik positif pada pusat di plot sebagai berikut. Panjang panah adalah suatu indikasi dari kekuatan medan listrik pada titik tersebut.

import numpy as np
import matplotlib.pyplot as plt

def E(x,y):
    q= 1 #muatan dalam coulombs
    r1 = np.array([0,0]) #muatan diletakkan pada pusat koordinat
    e0= 8.85*10**(-12) #permittivitas free space
    mag= (q / (4 * np.pi* e0)) * (1 / ((x - r1[0])**2+ (y - r1[1])**2)) #kuat medan listrik
    ex= mag * ( np.sin(np.arctan2(x,y)))
    ey= mag * ( np.cos(np.arctan2(x,y)))
    
    return (ex,ey)

x=np.linspace (-10,10,14)
y=np.linspace (-10,10,14)

x,y=np.meshgrid(x,y)

ex,ey=E(x,y)
plt.quiver(x,y,ex,ey, scale = 15000000000)
plt.show()

(electric_potential)=
## Potensial Listrik

Pertimbangkan sebuah muatan $q$ di dalam medan listrik dari muatan lain $Q$. Muatan $q$ mengalami suatu gaya, $\mathbf{F}_Q$, diakibatkan oleh medan listrik. Lalu gerakkan $q$ dari $A \rightarrow B$ pada kecepatan konstan. Suatu gaya, $\mathbf{F}_{ext}$ harus diterapkan untuk menyamai $\mathbf{F}_Q$. Dengan demikian, dalam menggerakkan muatan tersebut gaya eksternal melakukan usaha. Bergerak pada kecepatan konstan

$$\mathbf{F}_{ext} + \mathbf{F}_Q = 0$$

maka usaha yang dilakukan oleh $\mathbf{F}_{ext}$ pada $q$ adalah 

$$dW = \mathbf{F}_{ext} \cdot d\boldsymbol{l} = - \mathbf{F}_{Q} \cdot d\boldsymbol{l}$$

Sehingga usaha total yang dilakukan oleh $\mathbf{F}_{ext}$ diperoleh dengan mengintegrasikan dari A ke B

$$W = \int_{A}^{B} \mathbf{F}_{ext} \cdot d\boldsymbol{l} = - \int_{A}^{B} \mathbf{F}_{Q} \cdot d\boldsymbol{l}$$

Usaha yang dilakukan, $W$, sebanding dengan perubahan energi potensial, $∆U$, maka

$$∆U = - \mathbf{F}_{Q} \cdot d\boldsymbol{l}$$

Menggunakan Hukum Coulomb dan melakukan integrasi kita dapatkan

$$∆U_{AB} = \frac{q Q}{4{\pi}{\epsilon_0}}\left(\frac{1}{r_B} - \frac{1}{r_A}\right)$$

sehingga perubahan energi potensial hanya bergantung pada pemisahan radial, r. Dengan demikian, $∆U_{AB}$ adalah independen (tidak dipengaruhi) dari jalur, artinya bentuk jalur tidak berpengaruh pada perubahan energi potensial.

### Beda potensial

Beda potensial antara $A$ dan $B$ adalah $∆V_{AB}$ dimana

$$∆V_{AB} =  \frac{∆U_{AB}}{q} = - \int_{A}^{B} \mathbf{E} \cdot d\boldsymbol{l}$$

$∆V_{AB}$ juga adalah jalur independen, dan tidak bergantung pada $q$ dengan satuan SI
$JC^{−1}$. Dengan memilih $V = 0$ selagi $r \rightarrow \infty$, kita mendefinisikan potensial listrik, $V$, pada $P$ sebagai usaha eksternal yang diperlukan untuk membawa sebuah muatan sebesar $+1 C$ pada kecepatan konstan dari $r = ∞ \,(V = 0)$ ke $P$: 

$$ V = - \int_{\infty}^{P} \mathbf{E} \cdot d\boldsymbol{l}$$

Fakta kunci tentang $V$: ia merupakan energi potensial / unit muatan positif; ia merupakan suatu medan skalar; serta prinsip superposisi berlaku. Tanpa diterapkan gaya eksternal, muatan positif bergerak ke potensial lebih rendah dan muatan negatif bergerak ke potensial lebih tinggi. Untuk sebuah muatan titik $Q$, potensial $V$ pada $r$ dari $Q$ adalah:

$$V = \frac{Q}{4{\pi}{\epsilon_0}r}$$