# nba-standings
NBA Standings scraped from nba.com

How to use this parser!

1) Get MySQL and set up a DB
2) Go to the root directory in /nba-standings (where this file is)
3) Build the DB: mysql -u<YOUR_USERNAME> -p<YOUR_PASSWORD> <YOUR_DATABASE_NAME> < "build_db.sql"
4) Duplicate or rename "default_config.json" and call it "config.json"
5) Modify the config for your DB (My mysql is in "/opt/local/var/run/mysql57/mysqld.sock" on my macbook installed with macports. Probably something else for you)
6) Run nba_crawler.py!

Possibly coming soon:
- This desperately needs scrape data validation
- Some test cases
- A virtual table for team_seasons that just use the latest scrapes to make querying easy
- Some renaming and refactoring