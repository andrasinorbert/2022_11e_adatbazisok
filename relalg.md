# Cimsor

- egy
- kettő

1. első
1. clheslfdhls
1. második
1. fksebfkb

```python
for i in range(1,10):
    print(i)
```

$\Pi$
$\sigma$
$\rho$
R &#8904; S
R &#8904;$_{feltétel}$ S

$x^{valami}$

| N | GY |
|---- | ---- |
| MM | málna |
| MM | méz |
| Füles | körte|
| Malacka |méz|
|Malacka | málna |
|Malacka | körte
|Kanga | banán |
|Tigris | méz|

1. Melyek azok a gyümölcsök, amelyeket ’Micimackó’ szeret?

$\Pi_{GY}(\sigma_{N='MM'}(SZ))$

```sql
select GY
from SZ
where N='MM';
```

2. Melyek azok a gyümölcsök, amelyeket ’Micimackó’ nem szeret? (de valaki más igen)

$\Pi_{GY}(SZ)-\Pi_{GY}(\sigma_{N='MM'}(SZ))$

```sql
(select GY
    from SZ)
except //minus
(select GY
    from SZ
    where N='MM');
```

3. Melyek azok a gyümölcsök, amelyeket valaki szeret és nem csak egyedül Micimackó?

$\Pi_{GY}(SZ-\sigma_{N='MM'}(SZ))$

```sql
select N
from
(select *
from SZ
EXCEPT
select *
from SZ
where N='MM')

select GY
from SZ
where N<>'MM';
```

4. Kik azok, akik legalább azokat a gyümölcsöket szereti, mint Micimackó?

