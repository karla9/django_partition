
# Summary
* copy **djangoext** package to root folder of your django project;
* modify the "settings.py", define your "SHARD" section in "DATABASES"
* in models.py of your Django apps, use "from djangoext.db" instead of "from django.db"

# Partition methods
currently this package supports:
* mod
* divide
* crc
* date/time
* (or add your own method via code)

# Modify settings.py
(under construction)

# When using PartitionModel in code

## in getter
must provide partition key in ".filter()" method, as it is essential for deciding
which table to be looked up
```python
MyModel.objects.filter(shard_key=x)
```

## in creation
must provide partition key in __init__() method
```python
my_inst = MyModel(shard_key=x, field_a=y,field_b=z)
my_inst.save()
```
