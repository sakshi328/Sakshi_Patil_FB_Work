def emp(**data):
    for key, val in data.items():
        print(key,':' ,val)
emp(id=101, name='ABC', sal=4000, dept='IT')