# DB作成

## ホテル情報のDB作成

### まずはすでにDBが存在する場合、DBを削除して作り直します。
```
/* HotelRecommendationSystem/dbに移動 */
$ cd /[自分のパス]/HotelRecommendationSystem/db

/* DBの削除 */
$ rm hotelRecDB
```

### hotelRecDBの作成
```
/* DBの作成 */
$ sqlite3 hotelRecDB

/* sqliteが起動します。 */

/* HotelRecommendationSystem/db/create_hotelRecDB.sqlを実行すれば一気にTableが作成できます。 */
> .read create_hotelRecDB.sql

/* sqliteの終了 */
> .exit

/* 一つずつ作る場合はotelRecommendationSystem/db/create_hotelRecDB.sqlを見ながら一つずつ実行していってください */
```

## 感情極性表のDB作成
### まずはすでにDBが存在する場合、DBを削除して作り直します。
```
/* HotelRecommendationSystem/dbに移動 */
$ cd /[自分のパス]/HotelRecommendationSystem/db

/* DBの削除 */
$ rm hotelRecDB
```

### emotionPolarityDBの作成
```
/* DBの作成 */
$ sqlite3 emotionPolarityDB



```
