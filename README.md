# 最適なホテルを推薦するサービス

## 使い方

## TABLE作成メモ
```
CREATE TABLE hotel_scores(hotel_score_id INTEGER PRIMARY KEY,hotel_id INTEGER UNIQUE,location_score REAL,landscape_score REAL,service_score REAL,cuisine_score REAL,FOREIGN KEY(hotel_id) REFERENCES hotels(hotel_id));
PRAGMA foreign_keys = ON;
```
