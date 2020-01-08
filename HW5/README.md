## BFS
>Breadth-First Search，中文叫廣度優先搜尋，</br>
是一種以Queue為基底的搜尋方式，可以利用BFS將Graph像是Tree的形式分出每個level有哪幾個點。

<img src="/pic/HW5_BFS.png" width="500" height="350">

## DFS
>Depth-First Search，中文叫深度優先搜尋，</br>
是一種以Stack為基底的搜尋方式，我們可以利用DFS得到將所有點都跑過的路徑。

<img src="/pic/HW5_BFS-Page-2.png" width="500" height="350">

## BFS vs DFS
- 程式執行:
>在BFS的部分是使用queue的方式去執行，push完後要從list的「最前面」pop掉一個數到另一個list；</br>
 在DFS則是用stack的方式進行，push完後要從list的「最後面」pop掉一個數到另一個list中。

- 代表意涵:
>兩個搜尋法雖然都會把每個點走過一次，但因為走的過程不同，代表的也不同。</br>
>在BFS當中，在起始點會先把跟那個點相連的點都走一次記為level1，再把跟level1相鄰的點走過，標記為level2，以此類推。</br>
所以在最後出來的list會像是[起始點,level1,level2.....]。</br>
>在DFS當中，在起始點會以先遇到的點作為新的起點，一直走下去，如果遇到死路就返回前面有其他相鄰節點的點，直到所有相鄰的點都被走過一次。</br>
所以在最後出來的list會變成整個graph跑過一次的路徑(像完走迷宮的感覺)。

- 使用情況:
>在記憶空間的方面，因為BFS的記憶空間與點的數量呈正比，而DFS是跟遞迴深度成正比，</br>
所以記憶空間DFS會比BFS小，如果是在很多點的情況下，會選擇使用DFS而不會選擇BFS。

## 參考資料
- [BFS](http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)
- [DFS](http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)
