
1. iris 는 stratif = y 되는데 boston은 안되는 이유 
   > 분류 모델은 샘플링이 중요하니 써주고, 예측모델은 샘플링이 그닥 안중요하니 안씀

2. mse 에서 square = False  사용하는 이유  
   > root 씌어주는 목적  = rmse로 바꿔주려고, mse는 값이 너무 커짐

3. 모델 별 random_state 1회 사용, 2회 사용?
   > tree model은 model안에 random_state도 써주고  split 할때 random_state 써주면 좋다. 
   > regressor 모델은 split 할때만 쓴다.

4. y값은 iloc 사용하지 말고(매트릭스 형태는 워닝 발생) sereis 형태로 변환해서 사용한다.


5. value가 주로 0인 컬럼이 많으면 머신러닝시 효율이 안좋다.
