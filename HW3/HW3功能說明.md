# Binary Search Tree功能說明
## 新增(insert):
在insert中我們必須先去看原本Tree的root是否存在，</br>
如果root存在，那麼我們先去看root的val跟我們要insert的node的value的關係</br>
(如果root.left、root.right存在)</br>
1.如果val比root.val小 或是 val等於root.val，那麼就利用遞迴讓root變成原始的root.left，然後再跟val比大小，重複動作</br>
2.如果val比root.val大，那麼就利用遞迴讓root變成原始的root.right，然後再跟val比大小，重複動作</br>
(如果root.left、root.right不存在)</br>
1.如果val比root.val小 或是 val等於root.val，那麼就讓root.left變成TreeNode(val)</br>
2.如果val比root.val大，那麼就讓root.right變成TreeNode(val)
## 刪除(delete):
在delete中我們利用search的概念，先找到我們要刪除的那個目標，也就是root.val=target(如上述遞迴方式)</br>
在刪除的時候有三種狀況:</br>
1. 要刪除的節點沒有任何子節點:</br>
這時候我們可以直接把要刪除的節點變成None</br>
2. 要刪除的節點只有單一子節點(左或右):</br>
這時候我們把要刪除的節點的子節點(左或右)移動到原本要刪除的節點的位置
3. 要刪除的節點有兩個子節點(左和右)</br>
這時候我們統一找要刪除的節點的左邊子節點以下val最大的節點，把那個val最大的節點移動到要刪除的那個節點的位置(直接把要刪除的節點的val改為val最大的節點的val)</br>
接著在使用delete把下面那個val最大的子節點刪掉</br>
## 查詢(search):
利用遞迴的方式</br>
如果root.val=要查詢的val，那麼就直接回傳root的位置</br>
如果要查詢的val比root.val小，那麼就利用遞迴讓root變成原本的root.left，重複動作，直到找完</br>
如果要查詢的val比root.val大，那麼就利用遞迴讓root變成原本的root.right，重複動作，直到找完</br>
如果要查詢的val不存在於Tree中，就回傳None
## 修改(modify):
modify的功能是要將Tree中的一個數(A)替換成另一個數(B)</br>
替換完之後再整理整個Tree，讓他符合BST規則，並且height要小於等於原本的Tree</br>
我這裡有想到幾種做法:</br>
1. 直接先delete要換掉的值(A)，再insert要替換進去的那個數(B)</br>
2. 直接把要換掉的值用要替換進去的數取代，然後之後再把整個Tree依照BST以及其他的規定重新排列</br>
3. 直接先把Tree走訪一次，並把過程的值全部append到一個list，把要換掉的數用要取代的數在list裡面取代，然後把list依照大小排列，再把排列完的Tree設中間值為root，然後重寫成一個Tree
