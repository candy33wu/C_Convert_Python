# C_Convert_Python
C++  convert to Python

:heavy_exclamation_mark:為避免格式跑掉請點擊右方HackMD連結開啟
## <font color="#EE5151">題目說明</font>:
![PROBLEM](https://upload.cc/i1/2020/10/21/yfFo0C.png)  
---
## 使用到的演算法_Minimum Spanning Tree - KRUSKAL:
	Step1. 創建一森林，將每一Node視為一樹
	Step2. 首先將所有的邊，依照權重的大小排序。
	Step3. 取最小邊加入，放入若產生cycle，則捨棄，依序找出最小生成樹上的n-1條邊(n個Node時)
### 演算法程式碼實作 : 
__C++__
#### <font color="#F5AC54">Step1.初始創建森林</font>
- <font color="#4DA3E3">連接之通道</font>
![NODE](https://upload.cc/i1/2020/10/21/ztoInT.png)  

- <font color="#4DA3E3">兩兩連通的Node</font>
![MAIN](https://upload.cc/i1/2020/10/21/yjcIav.png)  

- <font color="#4DA3E3">初始時視每一Node為一樹 (parent設為自己)</font>
![KRUSKAL](https://upload.cc/i1/2020/10/21/vcrR5k.png)  
---	
#### <font color="#F5AC54"> Step2.依照權重(r.d)大小排序Road(邊)</font>
- <font color="#4DA3E3">由小自大排序</font>
![SORT](https://upload.cc/i1/2020/10/21/EhbgWJ.png)  

- <font color="#4DA3E3"> small ( )排序函式</font>
![SMALL](https://upload.cc/i1/2020/10/21/EZfmQ0.png)  
---
#### <font color="#F5AC54">Step3.找出所求之最小生成樹</font>
- <font color="#4DA3E3">取最小邊，放入若無cycle 則保留，反之則捨棄</font>
![KRUSKAL](https://upload.cc/i1/2020/10/21/uQLxde.png)  

- <font color="#4DA3E3">判斷是否已連通 (由Root是否相同判定，避免cycle產生)</font>
![ROOT](https://upload.cc/i1/2020/10/21/Jvuolg.png
)  

- <font color="#4DA3E3">串聯兩樹</font>
![UNION](https://upload.cc/i1/2020/10/21/jztMWf.png)  
---
__Python__
#### <font color="#F5AC54">Step1.初始創建森林</font> (使用ctypes模組)
- <font color="#4DA3E3">連接之通道</font>
![NODE](https://upload.cc/i1/2020/10/21/957Omh.png
)  

- <font color="#4DA3E3">兩兩連通的Node</font>
![MAIN](https://upload.cc/i1/2020/10/21/NKvpuD.png
)  

- <font color="#4DA3E3">初始時視每一Node為一樹 (parent設為自己)</font>
![KRUSKAL](https://upload.cc/i1/2020/10/21/Koq8mB.png)  
---	
#### <font color="#F5AC54"> Step2.依照權重(r.d)大小排序Road(邊)</font>
- <font color="#4DA3E3">由小自大排序</font>
![SORT](https://upload.cc/i1/2020/10/21/dZwix5.png)  

- <font color="#4DA3E3"> small ( )排序函式</font>
![SMALL](https://upload.cc/i1/2020/10/21/wXQvVp.png)  
---
#### <font color="#F5AC54">Step3.找出所求之最小生成樹</font>
- <font color="#4DA3E3">取最小邊，放入若無cycle 則保留，反之則捨棄</font>
![KRUSKAL](https://upload.cc/i1/2020/10/21/TNyZau.png)  

- <font color="#4DA3E3">判斷是否已連通 (由Root是否相同判定，避免cycle產生)</font>
![ROOT](https://upload.cc/i1/2020/10/21/OEBTNA.png)  

- <font color="#4DA3E3">串聯兩樹</font>
![UNION](https://upload.cc/i1/2020/10/21/ObW16e.png)  
---
