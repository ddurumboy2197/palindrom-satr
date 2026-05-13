def palindrom(s):
    return s == s[::-1]
```

```python
print(palindrom("aba"))  # True
print(palindrom("madam"))  # True
print(palindrom("hello"))  # False
