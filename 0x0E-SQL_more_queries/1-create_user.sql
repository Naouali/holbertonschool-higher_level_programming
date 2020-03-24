-- creating a user
CREATE IF NOT EXIST USER user_0d_1 IDENTIFIED BY user_0d_1_pwd;
GRANT ALL PRIVILEGES ON *.* user_0d_1@localhost IDENTIFIED BY user_0d_1_pwd;
