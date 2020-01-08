## Binary Search Tree
**以樹的形式再加以規定**
最上面的那個節點稱為root

- 規則1 : 在這個樹中，每個節點都會有最少0個節點，最多2個節點(分別叫做root.left、root.right)

- 規則2 在Binary Search Tree中，比root小的數要往root的左邊走，比root大的數要往root的右邊走

- 規則3 在走訪的時候也必須像linked list一樣，從root到下面一個一個走訪，不能直接選取其中一個Node

由於有先以大小的比較結果去做二分法，因此再搜尋的時候就不需要去和每個數字比較一次


### 功能:
- [Search](#Search)
- [Insert](#Insert)
- [Delete](#Delete)

## Search
<img src="/pic/bst_search1.jpg" width="200" height="200"> <img src="https://tse4.mm.bing.net/th?id=OIP.iTsxK73hSI70rIco2DiSnwHaDt&pid=Api&P=0&w=331&h=166" width="50" height="50">  <img src="/pic/bst_search2.jpg" width="200" height="200"> <img src="https://tse4.mm.bing.net/th?id=OIP.iTsxK73hSI70rIco2DiSnwHaDt&pid=Api&P=0&w=331&h=166" width="50" height="50"> <img src="/pic/bst_search3.jpg" width="200" height="200">

## Insert 
<img src="/pic/bst_insert1.jpg" width="200" height="200"> <img src="https://tse4.mm.bing.net/th?id=OIP.iTsxK73hSI70rIco2DiSnwHaDt&pid=Api&P=0&w=331&h=166" width="50" height="50">  <img src="/pic/bst_insert2.jpg" width="200" height="200">

## Delete
<img src="/pic/bst_delete1.jpg" width="200" height="200"> <img src="https://tse4.mm.bing.net/th?id=OIP.iTsxK73hSI70rIco2DiSnwHaDt&pid=Api&P=0&w=331&h=166" width="50" height="50">  <img src="/pic/bst_delete2.jpg" width="200" height="200"> <img src="https://tse4.mm.bing.net/th?id=OIP.iTsxK73hSI70rIco2DiSnwHaDt&pid=Api&P=0&w=331&h=166" width="50" height="50"> <img src="/pic/bst_delete3.jpg" width="200" height="200">

## 參考資料
[Binary Search Tree-Search&Insert](http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html)

[Binary Search Tree-Delete](http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html)
