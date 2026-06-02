![[Dislike3.png]]

```python
t = int(input())

  

queries = []

for _ in range(t):

queries.append(int(input()))

  

valid = []

  

i = 1

while len(valid) <= 1000:
	if i % 3 != 0 and i % 10 != 3:
	valid.append(i)

	i += 1

  

for k in queries:
	print(valid[k-1],end=" ")

  

# t = int(input())
# for i in range (t):
# n = int(input())
# i=0
# k=1

# while(1):
	# if i%3!=0 and i%10!=3:
	# if n==k:
	# print(i)
	# break
	# k=k+1
	# i=i+1
```