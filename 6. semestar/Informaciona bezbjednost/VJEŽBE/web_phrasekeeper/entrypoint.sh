#!/bin/ash

# Secure entrypoint
chmod 600 /entrypoint.sh

# Initialize & Start MariaDB
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld
mysql_install_db --user=mysql --ldata=/var/lib/mysql
mysqld --user=mysql --console --skip-name-resolve --skip-networking=0 &

# Wait for mysql to start
while ! mysqladmin ping -h'localhost' --silent; do echo "not up" && sleep .2; done

function genPass() {
    echo -n $RANDOM | md5sum | head -c 32
}

mysql -u root << EOF
CREATE DATABASE phrasekeeper;

CREATE TABLE phrasekeeper.users (
    id          INT NOT NULL AUTO_INCREMENT,
    username    VARCHAR(256) UNIQUE NOT NULL,
    password    VARCHAR(256) NOT NULL,
    email       VARCHAR(256) UNIQUE NOT NULL,
    is_admin    INT NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);

INSERT INTO phrasekeeper.users (username, password, email, is_admin)
VALUES
    ('admin', '$(genPass)', 'admin@phrase-keeper.htb', 1),
    ('louisbarnett', '$(genPass)', 'louis_p_barnett@mailinator.com', 0),
    ('ninaviola', '$(genPass)', 'ninaviola57331@mailinator.com', 0),
    ('alvinfisher', '$(genPass)', 'alvinfisher1979@mailinator.com', 0);


CREATE TABLE IF NOT EXISTS phrasekeeper.saved_passwords (
    id         INT NOT NULL AUTO_INCREMENT,
    owner      VARCHAR(256) NOT NULL,
    type       VARCHAR(256) NOT NULL,
    address    VARCHAR(256) NOT NULL,
    username   VARCHAR(256) NOT NULL,
    password   VARCHAR(256) NOT NULL,
    note       VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO phrasekeeper.saved_passwords (owner, type, address, username, password, note)
VALUES
    ('admin', 'Web', 'phrase-keeper.htb', 'admin', 'admin123', 'pre-prod test password'),
    ('louisbarnett', 'Web', 'spotify.com', 'louisbarnett', 'YMgC41@)pT+BV', 'student sub'),
    ('louisbarnett', 'Email', 'dmail.com', 'louisbarnett@dmail.com', 'L-~I6pOy42MYY#y', 'private mail'),
    ('ninaviola', 'Web', 'office365.com', 'ninaviola1', 'OfficeSpace##1', 'company email'),
    ('alvinfisher', 'App', 'Netflix', 'alvinfisher1979', 'efQKL2pJAWDM46L7', 'Family Netflix'),
    ('alvinfisher', 'Web', 'twitter.com', 'alvinfisher1979', '7wYz9pbbaH3S64LG', 'old twitter account');

GRANT ALL ON phrasekeeper.* TO 'phrasekeeper'@'%' IDENTIFIED BY 'phrasekeeper' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EOF

/usr/bin/supervisord -c /etc/supervisord.conf
