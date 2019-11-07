# 前言
在寫完Heap Sort和Merge Sort後，如果要我直接說出第一個差別，我絕對會說是難度，</p>
我一開始是先寫Merge Sort，之後再寫Heap Sort，</p>
原本自己想出來Merge Sort後有點成就感，再接觸到Heap Sort就懷疑人生了</p>
## 進入主題
# Heap Sort和Merge Sort比較
## 概念
#### Heap Sort
>**Heap Sort**是將一個Array以tree的想法進行比大小和排列，</p>
而比較大小的作法我覺得Heap Sort的方向跟linked list有點像，</p>
為什麼我會這麼說呢?</p>
因為當初在linked list當中也是必須靠index值去找其中某個node，</p>
Heap Sort必須依靠index的值去移動位置，再跳回nums[index]去比較大小。</p>
#### Merge Sort
>**Merge Sort**則是利用分堆的概念，將每堆分到剩一個數之後跟另一堆比大小再組合，</p>
這當中比較沒有方向性的問題，只需要知道左邊的丟到一個的array，右邊的丟入另一個array</p>

## 程式碼
#### Heap Sort
>Heap Sort必須先找到每個root對應的left和right再進行比大小排列(heapify)，</p>
而我覺得難的部分並不是和left、right比大小排列的部分，而是要如何讓每個tree連結起來變成一個完整的tree型態。</p>
必須使用迴圈調整root的index到指定的位置，以這種方式串聯每個小樹，建立成一個Max_Heap，</p>
建立Max_heap後要將整棵樹的root(也就是nums[0])和最後一個數(nums[-1])對調，</p>
對調後必須執行sift-down的動作，重複執行上述交換位置和sift-down的動作直到整個nums排列正確</p>
#### Merge Sort
>Merge Sort相較比較直觀，把一個Array以中間為軸分兩堆，重複分到每一堆中只有一個數，</p>
之後再將每兩個堆比較大小排列，合成一堆，也就是Merge Sort 中 Merge的部分。</p>
這裡比較特殊的地方是不需要再分堆後利用merge函數合起來，只需利用recursive的方式就可以完成。</p>

## 時間複雜度
在時間複雜度的部分，Heap Sort跟Merge Sort一樣 </p>
Average Time : O(n log n)</p>
Best Time : O(n log n)</p>
Worst Time : O(n log n)</p>


## 額外空間(Extra Space)
#### Heap Sort
>Heap Sort基本上只需要一個Array就可以跑完整個排序流程，</p>
#### Merge Sort
>Merge Sort必須要n個Array才可以跑完整個排序流程，</p>

因為Merge Sort必須先分堆直到每堆裡只剩一個數，</p>
當一個Array中有n個element，就必須創n個額外空間讓每個element放入。</p>
因此在額外空間這部分:</p>
1. Heap Sort : O(1)</p>
2. Merge Sort : O(n)</p>

## 穩定度(Stability)
首先我先去搜尋了關於sorts的Stability是什麼意思，</p>
以下是我看完影片的理解，</p>
當一個物件不只有一個屬性(Ex:撲克牌有數字和花色)，</p>
>**以Stable Sort來說**，當我先依序數字大小排列再依序花色大小排列時，</p>
同花色的牌除了會被排再一起外，同花色內還會依照數字大小排列。(Ex:梅花3會在梅花7前面)</p>

>但**以Unstable Sort來說**，當依序先以數字大小排列完再依照花色大小排列後，</p>
Unsable Sort並不會去顧慮到同花色之間的大小。(Ex:梅花排在一起，但有可能梅花7在梅花3前面)</p>

接著我再去判斷Heap Sort 和 Merge Sort分別為stable或unstable，</p>
#### Heap Sort
>一開始我並不知道Heap Sort為stable還是unstable，</p>
因為我認為如果經過相同排列順序，那麼結果的順序應該跟一開始一樣，</p>
於是我上網搜尋了一下，了解為什麼Heap Sort是Unstable的原因，</p>
問題取決於建立Max_heap後，把第一個值和最後面這個值交換的動作，</p>
因為最後一個數被移上去做sift-down的動作，</p>
假如這個數(ex:20b)是最大的且array中還有一樣的數(ex:20a)，</p>
這時並不會做交換，所以20b會比20a儲存到結果的array，</p>
那麼原本array中在20b前面的20a經過排序後，會變在20b後面，</p>
因此Heap Sort為Unstable。
#### Merge Sort
>Merge Sort因為從一開始就是以分堆的概念去比較，</p>
因此即使array中有兩個一樣的數，比大小時遇到相等(20a、20b)，先把在左邊的儲存到結果的array，</p>
那麼在結果的array中，排在左邊的那個數也一樣會在左邊(20a、20b)。</p>

# 參考網頁:
1. [老師的投影片內容](https://tingtseng.pixnet.net/blog/post/39924871-algorithm-time-complexity-%E6%BC%94%E7%AE%97%E6%B3%95%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E6%95%B4%E7%90%86)</p>
2. [講解Stable&Unstable Sorts的影片](https://www.youtube.com/watch?v=akLN-F0HSS4)</p>
3. [Why Heap Sort is unstable](https://stackoverflow.com/questions/19336881/why-isnt-heapsort-stable)
