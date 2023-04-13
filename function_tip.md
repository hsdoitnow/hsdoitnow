
### value_counts - 고유값 별 카운트 구할 때
df['sex'].value_counts  


### 결측치 갯수 구할 때
df['name'].isna().sum()

### 인덱싱
df.loc[10:20,['name','pclass']]
df.iloc[10:20, 4:5]
> 동일

### 인덱싱으로 필터
df = df.loc[df['pclass'] == 1]   # numpy broadcasting case / 메모리도 접근해서 value 수정 가능
df = df[df['pclass'] == 1]  / view 만 접근해서 value 수정 불가


### 데이터프레임 내부에 카테고리컬 컬럼을 원핫인코딩 변환 작업
### 머신,딥러닝 모델 학습 시 꼭 필요 !
df = pd.get_dummies(df, columns=['pclass','name','sex','embarked','boat','body'], drop_first = True)
