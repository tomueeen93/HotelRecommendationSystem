# Create hotels table
CREATE TABLE hotels(hotel_id integer primary key,hotel_name varchar(32));
# Create hotel_score
CREATE TABLE hotel_scores(hotel_score_id integer primary key,hotel_id integer unique,location_score real,landscape_score real,service_score real,cuisine_score real,foreign key(hotel_id) references hotels(hotel_id));
# Create location_dics
CREATE TABLE location_dics(location_dic_id integer primary key,word text);
