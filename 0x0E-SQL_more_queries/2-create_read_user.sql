-- creating user and database
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
CREATE IF NOT EXISTS USER user_0d_2 IDENTIFIED BY user_0d_2_pwd;
GRANT SELECT ON *.* TO user_0d_2 IDENTIFIED BY user_0d_2_pwd;
