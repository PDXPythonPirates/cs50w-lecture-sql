# CS50W lecture3: SQL

Source code and tips for examples from CS50W SQL lecture.

This repo is based on the source files that accompany lecture 3.
- [lecture video](https://www.youtube.com/watch?v=Eda-NmcE5mQ&list=PLhQjrBD2T382hIW-IsOVuXP1uMzEvmcE5&index=5)
- [source files (src3.zip)](https://cdn.cs50.net/web/2018/spring/lectures/3/src3.zip)

## Changes

1. A `requirements.txt` was added with libraries used in the lecture.  An additional Postgres driver `pg8000` is included.
1. SQL connection logic modified to force SSL connection when `pg8000` is detected in the URL
1. SQL statements are combined in one file for convenience: `_create_all_tables.sql`

If you're having problems with `psycopg2`, you try out an alternative all-python library named `pg8000`.   This repo includes `pg8000` in the requirements.txt already.  

Update your environment variable `DATABASE_URL` to use it by changing `postgres` to `postgres+pg8000` at the start of the URL.

    # old URL (sqlalchemy defaults to using psycopg2)
    DATABASE_URL='postgres://xxxx:xxxxx@xxxxxx/xxxxxx'

    # URL that uses pg8000
    DATABASE_URL='postgres+pg8000://xxxx:xxxxx@xxxxxx/xxxxxx'

