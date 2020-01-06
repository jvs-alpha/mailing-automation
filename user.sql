CREATE USER f1@localhost IDENTIFIED BY "jesuslovesyou";
GRANT USAGE ON *.* TO f1@localhost IDENTIFIED BY "jesuslovesyou";
GRANT ALL PRIVILEGES ON nric.f1 TO f1@localhost IDENTIFIED BY "jesuslovesyou";
FLUSH PRIVILEGES;
